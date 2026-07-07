# design-skill.md

# CareerFit AI React UI Design Skill

## 1. 목적

이 문서는 CareerFit AI의 React UI를 일관된 기준으로 만들기 위한 디자인 가이드이다.

CareerFit AI는 취업·공모전 데이터 기반 포트폴리오 코치 서비스이며, 주요 사용자는 대학생이다.

디자인 톤은 다음을 지향한다.

- 전문적이지만 딱딱하지 않음
- 대학생이 부담 없이 사용할 수 있음
- 취업·진로 서비스답게 신뢰감이 있음
- 결과를 빠르게 이해할 수 있음
- 복잡한 기능보다 명확한 입력과 결과 전달을 우선함

---

## 2. 컬러 팔레트

Tailwind CSS 기본 색상 체계를 우선 사용한다.  
별도 커스텀 컬러를 남발하지 않는다.

### Primary

주요 버튼, 핵심 강조, 브랜드 포인트에 사용한다.

```text
bg-blue-500
hover:bg-blue-600
text-blue-600
focus:ring-blue-500