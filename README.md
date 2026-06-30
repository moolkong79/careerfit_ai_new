# CareerFit AI

> 취업·공모전 데이터 기반 맞춤형 AI 포트폴리오 코치

## 프로젝트 개요

[본인이 작성한 문제 정의 한 단락]

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
- [ ] 2일차: 
  - Python 가상환경을 설정하고 FastAPI 백엔드 서버 실행 환경을 구성함
  - 서버 상태 확인용 `/health` 엔드포인트를 구현함
  - 취업 공고 목업 데이터를 반환하는 `/jobs` 엔드포인트를 구현함
  - 사용자 스킬과 목표 직무를 분석하는 `/analyze` 목업 엔드포인트를 구현함
  - Gemini 2.5 Flash-Lite API 연결 및 `MOCK_MODE` 환경변수 설정을 추가함
- [ ] 2일차: FastAPI 서버 구축 및 Gemini API 연결
- [ ] 3일차: 데이터 파이프라인 구축
- [ ] 4일차: RAG 기반 서비스 + React UI
- [ ] 5일차: Docker + 포트폴리오 완성