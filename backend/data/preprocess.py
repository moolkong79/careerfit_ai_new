# backend/data/preprocess.py

# 데이터 전처리 파이프라인
# 실행: backend/ 폴더에서 python data/preprocess.py

import pandas as pd
import sqlite3
import json
import os
from datetime import date


# ─── 1. 파일 경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JOBS_CSV = os.path.join(BASE_DIR, "jobs.csv")
DB_PATH = os.path.join(BASE_DIR, "careerfit.db")
RAG_JSON = os.path.join(BASE_DIR, "rag_documents.json")


# ─── 2. CSV 읽기
def load_data(filepath: str) -> pd.DataFrame:
    """
    CSV 파일을 읽어 DataFrame으로 반환합니다.
    인코딩 오류가 발생하면 cp949로 재시도합니다.
    """
    try:
        df = pd.read_csv(filepath, encoding="utf-8")
        print(f"✅ 파일 읽기 성공 (UTF-8): {filepath}")
    except UnicodeDecodeError:
        df = pd.read_csv(filepath, encoding="cp949")
        print(f"✅ 파일 읽기 성공 (CP949): {filepath}")

    print(f"   행 수: {len(df)}, 열 수: {len(df.columns)}")
    print(f"   컬럼: {df.columns.tolist()}")

    return df


# ─── 3. 값 정리
def clean_value(value) -> str:
    """
    NaN 값을 빈 문자열로 바꾸고, 모든 값을 문자열로 변환합니다.
    ChromaDB metadata 값 타입을 str로 맞추기 위함입니다.
    """
    if pd.isna(value):
        return ""
    return str(value).strip()


# ─── 4. RAG 문서 변환
def convert_to_rag_documents(df: pd.DataFrame) -> list:
    """
    채용공고 DataFrame을 RAG용 문서 리스트로 변환합니다.
    """
    rag_documents = []

    for idx, row in df.iterrows():
        deadline = clean_value(row.get("deadline", ""))
        company = clean_value(row.get("company", ""))
        title = clean_value(row.get("title", ""))
        job_type = clean_value(row.get("job_type", ""))

        job_id = clean_value(row.get("id", ""))
        if not job_id:
            job_id = f"job_{idx + 1}"

        metadata = {
            "id": job_id,
            "company": company,
            "title": title,
            "job_type": job_type,
            "deadline": deadline,
            "source": "jobs.csv",

            "deadline_month": deadline[5:7] if len(deadline) >= 7 and deadline[4] == "-" else "",
            "is_startup": "true" if "스타트업" in company else "false",
            "first_saved_date": date.today().isoformat(),
        }

        page_content = (
            f"회사명: {company}\n"
            f"공고명: {title}\n"
            f"직무유형: {job_type}\n"
            f"마감일: {deadline}\n"
        )

        rag_documents.append({
            "page_content": page_content,
            "metadata": metadata,
        })

    return rag_documents


# ─── 5. 실행
if __name__ == "__main__":
    df_jobs = load_data(JOBS_CSV)

    print()
    print("=== 처음 3행 미리보기 ===")
    print(df_jobs.head(3).to_string())

    rag_documents = convert_to_rag_documents(df_jobs)

    with open(RAG_JSON, "w", encoding="utf-8") as f:
        json.dump(rag_documents, f, ensure_ascii=False, indent=2)

    print()
    print(f"✅ RAG 문서 저장 완료: {RAG_JSON}")
    print(f"   문서 수: {len(rag_documents)}")