# .env 파일에 있는 비밀값을 읽기 위한 도구
from dotenv import load_dotenv

# 컴퓨터 환경변수에서 값을 꺼내기 위한 기본 도구
import os

# HuggingFace 모델에게 요청을 보내는 도구
from huggingface_hub import InferenceClient


# 1. .env 파일 읽기
# 요리 비유: 비밀 재료 보관함(.env)을 여는 단계
load_dotenv()


# 2. .env 안에 있는 HUGGINGFACE_TOKEN 꺼내기
# 요리 비유: 주방 출입 카드(HUGGINGFACE_TOKEN)를 꺼내는 단계
token = os.getenv("HUGGINGFACE_TOKEN")


# 3. 토큰이 없으면 에러 내기
# 요리 비유: 출입 카드가 없으면 주방에 못 들어가는 것과 같음
if not token:
    raise RuntimeError("HUGGINGFACE_TOKEN이 .env 파일에 없습니다.")


# 4. HuggingFace 모델에게 요청할 클라이언트 만들기
# 요리 비유: 주문을 전달해주는 직원을 준비하는 단계
client = InferenceClient(
    token=token,
    provider="auto"
)


# 5. 모델에게 질문 보내기
# 요리 비유: 요리사에게 '이 요리를 만들어주세요'라고 주문하는 단계
response = client.chat.completions.create(
    model="google/gemma-2-2b-it",
    messages=[
        {
            "role": "user",
            "content": "오목 게임에서 이기는 방법을 초보자에게 쉽게 설명해줘."
        }
    ],
    max_tokens=200
)


# 6. 모델이 준 답변 출력하기
# 요리 비유: 완성된 음식을 접시에 담아 보여주는 단계
print(response.choices[0].message.content)