import streamlit as st

st.set_page_config(
    page_title='공동교육과정',
    page_icon=' '
)

menu = st.sidebar.selectbox('MENU',['BMI 지수 계산기','원의 넓이 계산기'])

if menu == 'BMI 지수 계산기':
    st.subheader('BMI 지수 계산기')

키 = st.number_input('키를 입력하세요.(m)', step=1)
체중 = st.number_input('몸무게를 입력하세요.(kg)', step=1)
btn = st.button('계산하기')
if btn:
    st.write('당신의 BMI지수는',체중/(키*키),'입니다.')
    if 체중/(키*키) > 20:
        st.write('저체중')
    elif 20 <체중/(키*키)<24:
        st.write('정상')


elif menu == '원의 넓이 계산기':
    st.subheader('원의 넓이 계산기')


elif menu == '시험평균 등급 계산기':
    st.subheader('시험평균 등급 계산기')
    국어 = int(input("국어점수를 입력하세요."))
    수학 = int(input("수학점수를 입력하세요."))
    영어 = int(input("영어점수를 입력하세요."))
    평균 = (국어 + 수학 + 영어) / 3
    if 평균 >= 90:
        print("A")
    elif 평균 >= 80:
        print("B")
    elif 평균 >= 70:
        print("C")
    else:
        print("D")


