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


## 진행 현황

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
- [ ] 4일차: RAG 기반 서비스 + React UI
- [ ] 5일차: Docker + 포트폴리오 완성