import streamlit as st

st.title('첫 웹앱 만들기🤖')
name = st.text_input('이름을 입력해주세요!👨🏻‍💻')
menu = st.selectbox('좋아하는 음식을 선택해주세요!', ['떡볶이', '순대', '어묵', '김말이'])
if st.button('인사말 생성하기'):
    st.write(f'{name}님! 당신이 좋아하는 음식은 {menu}이군요! 저도 좋아해요!')
