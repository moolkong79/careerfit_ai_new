# backend/routers/analyze.py

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from services.rag_service import search_documents
from services.llm_service import get_llm_response

router = APIRouter()


class AnalyzeRequest(BaseModel):
    major: str
    skills: List[str]
    job_type: str


class AnalyzeResponse(BaseModel):
    answer: str
    sources: List[dict]


@router.post("/analyze", response_model=AnalyzeResponse, tags=["Analyze"])
def analyze_career(request: AnalyzeRequest):
    """
    RAG 기반 역량 분석:
    사용자 입력 → ChromaDB 검색 → LLM 답변 생성 → sources 반환
    """
    query = (
        f"전공: {request.major}, "
        f"보유 스킬: {', '.join(request.skills)}, "
        f"관심 직무: {request.job_type}"
    )

    context_docs = search_documents(
        query=query,
        n_results=3
    )

    result = get_llm_response(
        query=query,
        context_docs=context_docs
    )

    return AnalyzeResponse(
        answer=result["answer"],
        sources=result["sources"]
    )