import streamlit as st
import google.generativeai as genai

st.title("산지크림 포스팅 생성기")

gemini_key = st.text_input("Gemini API 키", type="password")

st.divider()

restaurant_name = st.text_input("식당 이름")
address = st.text_input("주소")
menu_info = st.text_area("메뉴/가격")
my_visit = st.text_area("내 방문 내용")
other_reviews = st.text_area("참고 리뷰 (복붙)")

if st.button("포스팅 생성"):
    if not gemini_key:
        st.error("Gemini API 키를 입력해주세요.")
    else:
        genai.configure(api_key=gemini_key)
        model = genai.GenerativeModel("gemini-2.0-flash")
        
        prompt = f"""
너는 산지크림 블로그 작가야. 아래 정보로 네이버 블로그 포스팅을 써줘.

식당명: {restaurant_name}
주소: {address}
메뉴/가격: {menu_info}
내 방문 내용: {my_visit}
참고 리뷰: {other_reviews}

규칙:
1. 제목 후보 4개 (SEO 키워드 앞배치)
2. 상세정보 블록 (위치/영업시간/전화/주차/편의시설/꿀팁)
3. 본문 (산지크림 말투로, 섹션마다 emoji+소제목)
4. 총평 (✔️ 체크리스트 형식, 짧게)
5. 해시태그 30개
"""
        
        with st.spinner("포스팅 생성 중..."):
            response = model.generate_content(prompt)
            st.markdown(response.text)
