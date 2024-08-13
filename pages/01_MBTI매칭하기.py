import streamlit as st

# 앱 제목 및 이미지
st.title('✨ MBTI 성격 유형 분석 🤖')
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/MBTI-I-E.png/800px-MBTI-I-E.png", 
         caption="MBTI 성격 유형", use_column_width=True)

# 사용자로부터 이름 입력받기
name = st.text_input('먼저, 당신의 이름을 알려주세요! 👤')

# 사용자에게 환영 메시지 표시
st.write("안녕하세요, " + (name if name else "친구") + "님! 오늘은 당신의 MBTI 성격 유형을 알아보고,")
st.write("당신과 가장 잘 맞는 유형과 그렇지 않은 유형을 살펴볼 거에요. 😄")

# MBTI 유형 선택박스
mbti = st.selectbox('당신의 MBTI를 선택해주세요! 📊', 
                    ['INTJ', 'INTP', 'ENTJ', 'ENTP', 
                     'INFJ', 'INFP', 'ENFJ', 'ENFP', 
                     'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ', 
                     'ISTP', 'ISFP', 'ESTP', 'ESFP'])

# MBTI 설명과 궁합을 미리 정의한 딕셔너리
mbti_info = {
    'INTJ': {
        'description': 'INTJ는 독립적이고 전략적 사고를 잘하는 성격 유형으로, 창의적이고 혁신적인 아이디어를 발전시키는 데 능숙합니다.',
        'good_match': 'ENTP, ENFP',
        'bad_match': 'ISFP, ESFP'
    },
    'INTP': {
        'description': 'INTP는 논리적이고 분석적인 사고를 중시하며, 복잡한 문제 해결에 능합니다. 새로운 아이디어를 탐구하는 것을 좋아합니다.',
        'good_match': 'ENTJ, ESTJ',
        'bad_match': 'ISFJ, ESFJ'
    },
    'ENTJ': {
        'description': 'ENTJ는 리더십이 강하고 목표 지향적인 성격 유형으로, 큰 그림을 그리고 이를 실현하는 데 능숙합니다.',
        'good_match': 'INTP, ISTP',
        'bad_match': 'INFP, ISFP'
    },
    'ENTP': {
        'description': 'ENTP는 창의적이고 재치 있는 성격 유형으로, 다양한 관점에서 문제를 해결하며 새로운 도전을 즐깁니다.',
        'good_match': 'INFJ, INTJ',
        'bad_match': 'ISFJ, ISTJ'
    },
    'INFJ': {
        'description': 'INFJ는 직관적이고 이상주의적인 성격 유형으로, 사람들을 이해하고 돕는 데 깊은 만족을 느낍니다.',
        'good_match': 'ENFP, ENTP',
        'bad_match': 'ESTP, ESTJ'
    },
    'INFP': {
        'description': 'INFP는 매우 이상주의적이며, 자신의 가치를 중요시하고 타인을 이해하려는 성향이 강합니다.',
        'good_match': 'ENFJ, ENTJ',
        'bad_match': 'ESTJ, ESTP'
    },
    'ENFJ': {
        'description': 'ENFJ는 따뜻하고 외향적인 성격 유형으로, 다른 사람들과 깊은 인간관계를 맺는 데 능숙합니다.',
        'good_match': 'INFP, ISFP',
        'bad_match': 'ISTP, INTP'
    },
    'ENFP': {
        'description': 'ENFP는 활기차고 창의적인 성격 유형으로, 새로운 가능성을 탐구하고 사람들과의 관계를 중시합니다.',
        'good_match': 'INFJ, INTJ',
        'bad_match': 'ISTJ, ISFJ'
    },
    'ISTJ': {
        'description': 'ISTJ는 신중하고 책임감이 강한 성격 유형으로, 현실적이고 체계적인 접근을 중요시합니다.',
        'good_match': 'ESTP, ESFP',
        'bad_match': 'ENFP, ENTP'
    },
    'ISFJ': {
        'description': 'ISFJ는 매우 헌신적이고 실용적인 성격 유형으로, 사람들을 돕는 것을 즐기며 책임감을 중시합니다.',
        'good_match': 'ESFP, ESTP',
        'bad_match': 'ENTP, ENFP'
    },
    'ESTJ': {
        'description': 'ESTJ는 실용적이고 조직적인 성격 유형으로, 명확한 구조와 규칙을 선호하며 목표를 향해 나아갑니다.',
        'good_match': 'ISTP, INTP',
        'bad_match': 'INFP, ISFP'
    },
    'ESFJ': {
        'description': 'ESFJ는 사교적이고 협조적인 성격 유형으로, 타인의 필요를 이해하고 조화를 이루는 것을 중시합니다.',
        'good_match': 'ISFP, ISTP',
        'bad_match': 'INTP, INFP'
    },
    'ISTP': {
        'description': 'ISTP는 논리적이고 분석적인 성격 유형으로, 문제를 해결하고 실제적인 결과를 얻는 것을 선호합니다.',
        'good_match': 'ESTJ, ENTJ',
        'bad_match': 'ENFJ, ESFJ'
    },
    'ISFP': {
        'description': 'ISFP는 조용하고 감성적인 성격 유형으로, 자신의 내면의 가치와 조화를 이루며 생활합니다.',
        'good_match': 'ESFJ, ENFJ',
        'bad_match': 'ENTJ, ESTJ'
    },
    'ESTP': {
        'description': 'ESTP는 활동적이고 즉흥적인 성격 유형으로, 현재의 순간을 즐기고 새로운 경험을 추구합니다.',
        'good_match': 'ISTJ, ISFJ',
        'bad_match': 'INFJ, INFP'
    },
    'ESFP': {
        'description': 'ESFP는 사교적이고 즐거움을 추구하는 성격 유형으로, 삶을 즐기고 다른 사람들과의 교류를 중시합니다.',
        'good_match': 'ISFJ, ISTJ',
        'bad_match': 'INTJ, INFJ'
    },
}

# 버튼을 누르면 MBTI 설명과 궁합 정보 출력
if st.button('MBTI 분석하기'):
    if mbti in mbti_info:
        st.write(f'💡 {name}님! 당신의 MBTI 유형은 **{mbti}**입니다.')
        st.write('🔍 **특성 설명:** ' + mbti_info[mbti]['description'])
        st.write('💘 **궁합이 잘 맞는 유형:** ' + mbti_info[mbti]['good_match'])
        st.write('💔 **궁합이 잘 안 맞는 유형:** ' + mbti_info[mbti]['bad_match'])
    else:
        st.write('해당 MBTI 유형에 대한 정보가 없습니다.')

# 마지막으로, 사용자가 MBTI 유형에 대한 추가 정보를 원할 경우 링크 제공
st.write('더 많은 정보를 원하시나요? [여기](https://www.16personalities.com)에서 더 자세히 알아보세요!')
