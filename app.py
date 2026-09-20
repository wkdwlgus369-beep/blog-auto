import streamlit as st
import openai
import hashlib
import hmac
import base64
import time
import requests

st.title("산지크림 포스팅 생성기")

openai_key = st.text_input("OpenAI API 키", type="password")
naver_customer_id = st.text_input("네이버 고객 ID")
naver_access_key = st.text_input("네이버 Access License", type="password")
naver_secret_key = st.text_input("네이버 Secret Key", type="password")

st.divider()

restaurant_name = st.text_input("식당 이름")
address = st.text_input("주소")
menu_info = st.text_area("메뉴/가격")
my_visit = st.text_area("내 방문 내용")
other_reviews = st.text_area("참고 리뷰 (복붙)")

if st.button("포스팅 생성"):
    if not openai_key:
        st.error("OpenAI API 키를 입력해주세요.")
    else:
        client = openai.OpenAI(api_key=openai_key)
        
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
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
            result = response.choices[0].message.content
            st.markdown(result)
