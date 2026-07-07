# CareerFit AI

> 취업·공모전 데이터 기반 맞춤형 AI 포트폴리오 코치

## 프로젝트 개요

[CareerFit AI는 사용자의 전공, 보유 스킬, 관심 직무를 입력받아 취업 준비 방향과 추천 직무 데이터를 제공하는 AI 기반 커리어 코칭 서비스입니다. 저는 전자전기컴퓨터공학부 학생으로서 AI 분석가 직무에 관심이 있으며, Python, SQL, 머신러닝, 딥러닝, 데이터 분석 역량을 중심으로 취업 준비를 하고 있습니다. 이 프로젝트는 직무 공고 데이터와 공모전 데이터를 활용하여 개인 맞춤형 포트폴리오 준비 방향을 제안하는 것을 목표로 합니다.]

## 기술 스택


| 영역     | 기술                       |
| ------ | ------------------------ |
| 백엔드    | Python, FastAPI          |
| AI API | Gemini 2.5 Flash-Lite    |
| 데이터    | Pandas, SQLite, ChromaDB |
| 프론트엔드  | React, Vite              |
| 실행 환경  | Docker                   |


## 🏗 아키텍처

```text
사용자 입력
  ↓
React/Vite Frontend
  ↓
FastAPI /analyze API
  ↓
ChromaDB RAG 검색
  ↓
Gemini LLM 답변 생성
  ↓
AI 분석 결과 + 참고 공고 sources 반환


진행 현황

- [x] 1일차: 프로젝트 기획 및 개발 환경 세팅
- [x] 2일차: FastAPI 서버 구축 및 Gemini API 연결
  - Python 가상환경을 설정하고 FastAPI 백엔드 서버 실행 환경을 구성함
  - 서버 상태 확인용 `/health` 엔드포인트를 구현함
  - 취업 공고 목업 데이터를 반환하는 `/jobs` 엔드포인트를 구현함
  - 사용자 스킬과 목표 직무를 분석하는 `/analyze` 목업 엔드포인트를 구현함
  - Gemini 2.5 Flash-Lite API 연결 및 `MOCK_MODE` 환경변수 설정을 추가함
- [x] 3일차: 데이터 파이프라인 구축  

:- `backend/data/jobs.csv` 파일 생성  

- AI 분석가 직무에 맞는 취업 공고 데이터 3개 추가  
- `company`, `title`, `required_skills`, `preferred_skills`, `description`, `job_type`, `deadline` 컬럼 구조 설계  
- Pandas를 활용하여 `jobs.csv` 데이터 로딩 및 행/열 정보 확인  
- 향후 RAG 검색에 활용할 직무 데이터 기반 마련

- [x] 4일차: RAG 기반 서비스 + React UI  
- ChromaDB metadata 확장 설계 및 적용  
 - `deadline_month`: 마감월 필터링용 metadata  
 - `is_startup`: 스타트업 공고 필터링용 metadata  
 - `first_saved_date`: 공고 최초 저장일 추적용 metadata  
  
- `backend/data/preprocess.py`를 수정하여 `jobs.csv` 데이터를 RAG 문서 형식으로 변환  
 - `rag_documents.json` 생성  
 - 각 문서에 `page_content`와 `metadata` 포함  
  
- ChromaDB 저장 및 검색 테스트 구현  
 - `backend/data/test_search.py` 작성  
 - RAG 문서를 ChromaDB 컬렉션에 저장  
 - 질문 기반 유사도 검색 테스트  
 - metadata filter 검색 테스트  
  
- RAG 검색 서비스 구현  
 - `backend/services/rag_service.py` 생성  
 - `search_documents()` 함수 구현  
 - `job_type` metadata filter 기능 추가  
 - `deadline_month`, `is_startup` 기반 검색 확장 가능 구조 마련  
  
- LLM 응답 서비스와 RAG 연결  
 - `backend/services/llm_service.py` 수정  
 - ChromaDB 검색 결과를 Gemini 프롬프트에 포함  
 - `answer`와 `sources`를 함께 반환하는 구조 구현  
 - MOCK_MODE를 통해 API 한도 초과 상황에서도 테스트 가능하도록 구성  
  
- `/analyze` API를 RAG 기반 분석 라우터로 개선  
 - 사용자 입력값을 기반으로 ChromaDB 검색 수행  
 - 검색된 공고 데이터를 바탕으로 AI 분석 결과 생성  
 - FastAPI Swagger UI에서 `/analyze` 테스트 완료  
  
- React + Vite 프론트엔드 구축  
 - `frontend/` 프로젝트 생성  
 - Tailwind CSS 설정  
 - `App.jsx`에서 `/analyze` API fetch 연결  
  
- React 컴포넌트 구현  
 - `InputForm.jsx`: 전공, 보유 스킬, 관심 직무 입력 폼  
 - `ResultCard.jsx`: AI 분석 결과 출력 카드  
 - `SourceCard.jsx`: 참고한 공고 출처 카드  
  
- 브라우저 통합 테스트 진행  
 - FastAPI 서버: `http://localhost:8000`  
 - React 개발 서버: `http://localhost:5173`  
 - 프론트엔드 입력 → 백엔드 `/analyze` 호출 → RAG 검색 → AI 분석 결과 출력 흐름 확인  
  
- 하네스 및 문서화 작업  
 - `harness/MAIN_HARNESS.md` 추가  
 - `harness/skills/design-skill.md` 작성  
 - `docs/MODEL_BENCHMARK.md` 작성  

- [ ] 5일차: Docker + 포트폴리오 완성
- FastAPI 백엔드 Dockerfile 작성
- `.dockerignore` 작성으로 불필요한 파일 제외
- `requirements.txt` 최종 정리
- Docker 이미지 빌드 테스트
- Docker 컨테이너 실행 후 `/health` 응답 확인
- `/analyze` API Docker 환경에서 호출 테스트
- Docker Desktop / WSL 실행 환경 문제 해결
- Render 백엔드 배포 흐름 확인
- React 프론트엔드 Render 연결 준비
- `VITE_API_BASE_URL` 기반 프론트엔드 API 주소 관리 구조 추가
- `FRONTEND_ORIGINS` 기반 FastAPI CORS 설정 개선
- 프론트엔드 Dockerfile 및 `.dockerignore` 작성
- Render 프론트엔드 Docker 배포 문서 작성
- README 최종화
- CHECKLIST, EVAL_QUESTIONS, 개인 회고 문서 정리
- GitHub 최종 커밋 및 main 브랜치 반영
```

