from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class AnalyzeRequest(BaseModel):
    user_skills: List[str]
    target_job: str

@router.post("/analyze", tags=["Analyze"])
def analyze_profile(request: AnalyzeRequest):
    """
    사용자의 보유 스킬과 목표 직무를 간단히 분석하는 엔드포인트.
    현재는 목업 분석 결과를 반환한다.
    """
    return {
        "target_job": request.target_job,
        "user_skills": request.user_skills,
        "message": "분석이 완료되었습니다.",
        "recommendation": [
            "목표 직무와 관련된 핵심 스킬을 더 보강하세요.",
            "프로젝트 경험을 포트폴리오에 정리하세요.",
            "채용 공고의 required_skills와 본인 스킬을 비교해보세요."
        ]
    }
