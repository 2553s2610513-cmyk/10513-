import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="헬스 코칭 앱",
    page_icon="💪",
    layout="centered"
)

# 제목
st.title("💪 AI 헬스 코칭 앱")

st.write("운동 목표를 입력하면 간단한 코칭을 제공합니다.")

# 사용자 입력
user_input = st.text_area(
    "운동 고민 또는 목표 입력",
    placeholder="예: 살을 빼고 싶어요"
)

# 버튼
if st.button("코칭 받기"):

    if user_input.strip() == "":
        st.warning("내용을 입력해주세요.")

    else:

        # 간단 규칙 기반 코칭
        if "살" in user_input or "다이어트" in user_input:
            advice = "유산소 운동과 식단 조절을 함께 진행하는 것이 중요합니다."

        elif "근육" in user_input or "벌크업" in user_input:
            advice = "단백질 섭취와 점진적 중량 증가를 꾸준히 실천해보세요."

        elif "복근" in user_input:
            advice = "체지방 감량과 코어 운동을 병행하는 것이 효과적입니다."

        elif "러닝" in user_input:
            advice = "무리한 속도보다 꾸준한 거리와 호흡 유지가 중요합니다."

        elif "운동" in user_input:
            advice = "주 3~4회 규칙적인 운동 습관부터 시작해보세요."

        else:
            advice = "충분한 수면과 꾸준한 운동 습관이 가장 중요합니다."

        st.success("헬스 코칭 결과")
        st.write(advice)

# 하단 문구
st.caption("Made with Streamlit 💪")
