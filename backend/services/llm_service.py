# backend/services/llm_service.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()

MOCK_MODE = os.getenv("MOCK_MODE", "true").lower() == "true"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY", "")
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN", "")

LLM_MODEL = os.getenv("LLM_MODEL", "gemini-2.5-flash-lite")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")


def build_rag_prompt(query: str, context_docs: list) -> str:
    """
    사용자 질문 + RAG 검색 문서로 LLM 프롬프트를 구성합니다.
    """
    if context_docs:
        context_text = "\n\n".join([
            f"[공고 {i + 1}]\n"
            f"{doc['text']}\n"
            f"출처: {doc['metadata'].get('company', '')} — {doc['metadata'].get('title', '')}\n"
            f"직무유형: {doc['metadata'].get('job_type', '')}\n"
            f"마감일: {doc['metadata'].get('deadline', '')}\n"
            f"검색거리: {doc.get('distance', '')}"
            for i, doc in enumerate(context_docs)
        ])

        context_section = f"""
[참고 데이터 — 실제 취업·공모전 공고]
{context_text}

위 데이터를 반드시 근거로 사용해 답변하세요.
답변에서 어떤 공고를 참고했는지 명시하세요.
"""
    else:
        context_section = """
[참고 데이터 없음]
관련 공고를 찾지 못했습니다. 일반적인 커리어 조언을 제공합니다.
"""

    return f"""당신은 취업·공모전 전문 커리어 코치입니다.
다음 지원자 정보와 참고 데이터를 바탕으로 맞춤형 조언을 한국어로 제공하세요.

[지원자 정보]
{query}

{context_section}

[답변 형식]
1. 현재 역량 평가 (2문장 이내)
2. 추천 공고 또는 공모전 (1~2개, 이유 포함)
3. 부족한 역량 및 준비 방향 (3가지 이내)

간결하고 실용적으로 작성하세요."""


def _build_sources(context_docs: list) -> list:
    """
    프론트엔드에 반환할 출처 목록을 구성합니다.
    """
    return [
        {
            "company": doc["metadata"].get("company", ""),
            "title": doc["metadata"].get("title", ""),
            "job_type": doc["metadata"].get("job_type", ""),
            "deadline": doc["metadata"].get("deadline", ""),
            "deadline_month": doc["metadata"].get("deadline_month", ""),
            "is_startup": doc["metadata"].get("is_startup", ""),
            "distance": doc.get("distance", 0),
        }
        for doc in context_docs
    ]


def _generate_with_gemini(prompt: str) -> str:
    """
    Gemini API 호출.
    """
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY가 설정되지 않았습니다.")

    import google.generativeai as genai

    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(LLM_MODEL)

    response = model.generate_content(prompt)
    return response.text


def _generate_with_mistral(prompt: str) -> str:
    """
    Mistral API 호출.
    """
    if not MISTRAL_API_KEY:
        raise ValueError("MISTRAL_API_KEY가 설정되지 않았습니다.")

    url = "https://api.mistral.ai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": LLM_MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
        "temperature": 0.3,
    }

    response = requests.post(url, headers=headers, json=payload, timeout=60)
    response.raise_for_status()

    data = response.json()
    return data["choices"][0]["message"]["content"]


def _generate_with_huggingface(prompt: str) -> str:
    """
    HuggingFace InferenceClient 호출.

    LLM_MODEL 예:
    huggingface:meta-llama/Llama-3.2-3B-Instruct
    """
    if not HUGGINGFACE_TOKEN:
        raise ValueError("HUGGINGFACE_TOKEN이 설정되지 않았습니다.")

    try:
        from huggingface_hub import InferenceClient
    except ImportError:
        raise ImportError("huggingface_hub가 설치되어 있지 않습니다. pip install huggingface_hub 실행 필요")

    model_id = LLM_MODEL.replace("huggingface:", "", 1)

    client = InferenceClient(
        model=model_id,
        token=HUGGINGFACE_TOKEN,
    )

    response = client.chat_completion(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        max_tokens=700,
        temperature=0.3,
    )

    return response.choices[0].message.content


def _generate_with_ollama(prompt: str) -> str:
    """
    로컬 Ollama 호출.

    LLM_MODEL 예:
    ollama:llama3.2:3b
    """
    model_name = LLM_MODEL.replace("ollama:", "", 1)

    url = f"{OLLAMA_BASE_URL}/api/generate"

    payload = {
        "model": model_name,
        "prompt": prompt,
        "stream": False,
    }

    response = requests.post(url, json=payload, timeout=120)
    response.raise_for_status()

    data = response.json()
    return data.get("response", "")


def _generate_answer(prompt: str) -> str:
    """
    LLM_MODEL 값에 따라 사용할 Provider를 선택합니다.
    """
    if LLM_MODEL.startswith("gemini"):
        return _generate_with_gemini(prompt)

    if LLM_MODEL.startswith("mistral"):
        return _generate_with_mistral(prompt)

    if LLM_MODEL.startswith("huggingface:"):
        return _generate_with_huggingface(prompt)

    if LLM_MODEL.startswith("ollama:"):
        return _generate_with_ollama(prompt)

    raise ValueError(f"지원하지 않는 LLM_MODEL입니다: {LLM_MODEL}")


def get_llm_response(query: str, context_docs: list) -> dict:
    """
    RAG 문서와 함께 LLM 응답을 생성합니다.
    """
    sources = _build_sources(context_docs)

    if MOCK_MODE:
        return {
            "answer": (
                f"[MOCK 응답]\n"
                f"질문: {query}\n"
                f"사용 모델 설정: {LLM_MODEL}\n"
                f"참고 문서 수: {len(context_docs)}개\n"
                f"MOCK_MODE=false 설정 시 실제 LLM 응답을 받습니다."
            ),
            "sources": sources,
        }

    try:
        prompt = build_rag_prompt(query, context_docs)
        answer = _generate_answer(prompt)

        return {
            "answer": answer,
            "sources": sources,
        }

    except Exception as e:
        error_msg = str(e)

        if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
            return {
                "answer": "[API 한도 초과] MOCK_MODE=true 로 전환하고 계속하세요.",
                "sources": sources,
            }

        return {
            "answer": f"[LLM 오류] {error_msg}",
            "sources": sources,
        }