from fastapi import APIRouter, HTTPException

router = APIRouter()

# 목업 데이터: 3일차에 실제 CSV 데이터로 교체한다
MOCK_JOBS = [
    {
        "id": 1,
        "company": "네오테크AI",
        "title": "AI 모델 개발자",
        "required_skills": ["Python", "PyTorch", "딥러닝"],
        "preferred_skills": ["TensorFlow", "MLOps"],
        "description": "이미지, 텍스트, 센서 데이터를 활용한 AI 모델을 개발합니다. 모델 학습, 성능 평가, 추론 속도 개선 업무를 수행하며 서비스 적용을 위한 실험을 진행합니다.",
        "deadline": "2026-08-31"
    },
    {
        "id": 2,
        "company": "한빛모빌리티",
        "title": "자율주행 AI 엔지니어",
        "required_skills": ["Python", "컴퓨터 비전", "OpenCV"],
        "preferred_skills": ["ROS", "C++"],
        "description": "카메라와 센서 데이터를 분석하여 자율주행 인식 모델을 개발합니다. 차선, 객체, 보행자 인식 알고리즘을 개선하고 실제 주행 데이터 기반으로 모델 성능을 검증합니다.",
        "deadline": "2026-08-31"
    },
    {
        "id": 3,
        "company": "메디인텔리전스",
        "title": "머신러닝 엔지니어",
        "required_skills": ["Python", "머신러닝", "SQL"],
        "preferred_skills": ["Docker", "AWS"],
        "description": "의료 및 헬스케어 데이터를 활용한 예측 모델을 개발합니다. 데이터 전처리, 모델 학습, API 연동을 통해 AI 기능이 실제 서비스에서 동작하도록 구현합니다.",
        "deadline": "2026-08-31"
    }
]

@router.get("/jobs", tags=["Jobs"])
def get_jobs():
    """
    취업 공고 목록을 반환하는 엔드포인트.
    현재는 목업 데이터를 반환하며, 3일차에 실제 데이터로 교체한다.
    """
    return {
        "count": len(MOCK_JOBS),
        "jobs": MOCK_JOBS
    }

@router.get("/jobs/{job_id}", tags=["Jobs"])
def get_job_by_id(job_id: int):
    """
    특정 공고의 상세 정보를 반환한다.
    """
    for job in MOCK_JOBS:
        if job["id"] == job_id:
            return job

    raise HTTPException(
        status_code=404,
        detail=f"공고 ID {job_id}를 찾을 수 없습니다."
    )
