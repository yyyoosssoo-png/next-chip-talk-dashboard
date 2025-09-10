import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# 페이지 설정
st.set_page_config(
    page_title="Next Chip Talk 교육 성과 분석",
    page_icon="🔬",
    layout="wide"
)

# 헤더
st.title("🔬 Next Chip Talk 교육 성과 분석")
st.markdown("### 2025 미래반도체 Next & Grey 영역 교육 성과")
st.markdown("---")

# 데이터 정의
@st.cache_data
def load_data():
    session_data = pd.DataFrame({
        '회차': ['1회차\n(4.18)', '2회차\n(6.25)', '3회차\n(7.30)', '4회차\n(9.2-3)'],
        '참가자수': [38, 38, 25, 17],
        '만족도': [4.5, 4.6, 4.4, 4.5],
        '추천률': [95.0, 97.4, 100.0, 88.2],
        'R&D': [45, 25, 24, 29],
        '사업전략': [35, 50, 52, 24],
        '제조기술': [20, 25, 24, 18]
    })
    return session_data

session_data = load_data()

# 탭 생성
tab1, tab2, tab3, tab4 = st.tabs(["📊 종합 개요", "👥 참가자 구성", "💬 피드백 분석", "💡 전략 인사이트"])

with tab1:
    st.header("종합 개요")
    
    # KPI 카드들
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("총 참가자", "118명", "4회차 누적")
    
    with col2:
        st.metric("평균 만족도", "4.50", "5점 만점")
    
    with col3:
        st.metric("평균 추천률", "95.1%", "매우 높은 수준")
    
    with col4:
        st.metric("추정 ROI", "380%", "투자 대비 효과")
    
    # 차트들
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("회차별 만족도 추이")
        fig_satisfaction = px.line(
            session_data, 
            x='회차', 
            y='만족도',
            markers=True,
            color_discrete_sequence=['#a855f7']
        )
        fig_satisfaction.update_layout(yaxis_range=[0, 5])
        st.plotly_chart(fig_satisfaction, use_container_width=True)
    
    with col2:
        st.subheader("회차별 추천률 변화")
        fig_recommendation = px.bar(
            session_data,
            x='회차',
            y='추천률',
            color='회차',
            color_discrete_sequence=['#a855f7', '#ec4899', '#06b6d4', '#10b981']
        )
        fig_recommendation.update_layout(showlegend=False, yaxis_range=[0, 100])
        st.plotly_chart(fig_recommendation, use_container_width=True)

with tab2:
    st.header("참가자 구성 변화")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("직군별 참여 추이")
        fig_dept = go.Figure()
        
        fig_dept.add_trace(go.Scatter(
            x=session_data['회차'],
            y=session_data['R&D'],
            mode='lines+markers',
            name='R&D',
            line=dict(color='#a855f7', width=3)
        ))
        
        fig_dept.add_trace(go.Scatter(
            x=session_data['회차'],
            y=session_data['사업전략'],
            mode='lines+markers',
            name='사업전략',
            line=dict(color='#06b6d4', width=3)
        ))
        
        fig_dept.add_trace(go.Scatter(
            x=session_data['회차'],
            y=session_data['제조기술'],
            mode='lines+markers',
            name='제조/기술',
            line=dict(color='#10b981', width=3)
        ))
        
        fig_dept.update_layout(yaxis_title='참여 비율 (%)', yaxis_range=[0, 60])
        st.plotly_chart(fig_dept, use_container_width=True)
    
    with col2:
        st.subheader("경력별 참여 분포")
        
        experience_data = ['10년 이상', '5-10년', '5년 미만']
        experience_values = [71.2, 18.5, 10.3]
        
        fig_exp = px.pie(
            values=experience_values,
            names=experience_data,
            color_discrete_sequence=['#a855f7', '#ec4899', '#06b6d4']
        )
        
        st.plotly_chart(fig_exp, use_container_width=True)

with tab3:
    st.header("피드백 분석")
    
    # 감정 분석 대시보드
    st.subheader("감정 분석 대시보드")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("😊 긍정적 피드백", "87건 (74%)", "매우 만족, 유익한 시간")
    
    with col2:
        st.metric("😐 중립적 피드백", "21건 (18%)", "적당한 난이도, 보통")
    
    with col3:
        st.metric("😔 개선 요청", "10건 (8%)", "시간 부족, 접근성 문제")
    
    # 키워드 분석 (워드클라우드 대신 텍스트로)
    st.subheader("주요 피드백 키워드")
    st.info("🔍 **주요 키워드**: 양자컴퓨팅, AI, 데이터센터, 차세대 메모리, 반도체, 기술 트렌드, NAND, 유리기판, 발열 해결, NPU, 광통신, 미래 시스템")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("회차별 감정 분석")
        
        sentiment_data = pd.DataFrame({
            '회차': session_data['회차'],
            '긍정': [85, 92, 78, 65],
            '중립': [12, 6, 18, 25],
            '개선요청': [3, 2, 4, 10]
        })
        
        fig_sentiment = px.bar(
            sentiment_data.melt(id_vars=['회차'], var_name='감정', value_name='비율'),
            x='회차',
            y='비율',
            color='감정',
            color_discrete_map={'긍정': '#10b981', '중립': '#f59e0b', '개선요청': '#ef4444'}
        )
        
        st.plotly_chart(fig_sentiment, use_container_width=True)
    
    with col2:
        st.subheader("주요 요청 사항 분포")
        
        request_labels = ['양자컴퓨팅', 'AI/데이터센터', '차세대 메모리', '발열 해결', '기타']
        request_values = [35, 25, 20, 15, 5]
        
        fig_request = px.pie(
            values=request_values,
            names=request_labels,
            color_discrete_sequence=['#a855f7', '#ec4899', '#06b6d4', '#10b981', '#f59e0b']
        )
        
        st.plotly_chart(fig_request, use_container_width=True)

with tab4:
    st.header("전략적 인사이트")
    
    # 교육 개요
    st.subheader("📚 Next Chip Talk 교육 개요")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🎯 교육 목적**
        - 급변하는 반도체 패러다임에 대응
        - 근미래 상용화 가능 기술 조망
        - 최신 연구 동향과 기술적 난제 이해
        - 기술 인사이트 향상
        
        **📚 학습 방식**
        - 현장 참여 세미나
        - 온라인 생중계 실시간 웨비나
        - mySUNI 플랫폼 녹화본 업로드
        """)
    
    with col2:
        st.markdown("""
        **👥 수강 대상**
        - 반도체 관련 멤버사 기술/개발 구성원
        - 전략/마케팅 구성원
        - 반도체 신기술 동향 지식 필요 구성원
        
        **🎬 학습 구성**
        - 모더레이터의 주제 키노트
        - 전문가 강연 (학계 + 산업계)
        - 대담과 질의 응답
        """)
    
    # HRD 기반 교육 전략
    st.subheader("🚀 HRD 기반 교육 전략")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **📈 참가자 확보 전략**
        - 타겟 직군별 맞춤 마케팅
        - 시즌별 참여도 분석 반영
        - 정기적 고객 조사 실시
        
        **⚙️ 운영 혁신**
        - 실시간 Q&A 화면 표시 시스템
        - 지역별 접근성 개선
        - 강의자료 사전/사후 제공
        
        **🔄 지속가능성 확보**
        - 기술 전문가 네트워킹 플랫폼
        - 분기별 기술 동향 레포트
        - mySUNI 커뮤니티 기반 스터디
        """)
    
    with col2:
        st.markdown("""
        **🎯 기술 인사이트 강화**
        - 양자컴퓨팅 전문 세션 신설
        - AI 데이터센터 심화 과정
        - 차세대 메모리 기술 시리즈
        
        **💰 ROI 평가 체계**
        - Kirkpatrick-Phillips 5단계 모델
        - 직접비용 대비 간접효과 측정
        - 교육 전후 성과 변화 추적
        """)
    
    # Kirkpatrick 평가 모델
    st.subheader("📊 Kirkpatrick-Phillips 5단계 평가")
    
    kirkpatrick_data = pd.DataFrame({
        '평가단계': ['Level1 반응', 'Level2 학습', 'Level3 인사이트', 'Level4 결과', 'Level5 ROI'],
        '현재수준': [95, 83, 75, 60, 75],
        '2025목표': [98, 90, 85, 80, 85]
    })
    
    fig_kirkpatrick = go.Figure()
    
    fig_kirkpatrick.add_trace(go.Scatterpolar(
        r=kirkpatrick_data['현재수준'],
        theta=kirkpatrick_data['평가단계'],
        fill='toself',
        name='현재 수준',
        line_color='#a855f7'
    ))
    
    fig_kirkpatrick.add_trace(go.Scatterpolar(
        r=kirkpatrick_data['2025목표'],
        theta=kirkpatrick_data['평가단계'],
        fill='toself',
        name='2025 목표',
        line_color='#ec4899',
        line_dash='dash'
    ))
    
    fig_kirkpatrick.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=True
    )
    
    st.plotly_chart(fig_kirkpatrick, use_container_width=True)
    
    st.success("""
    **🎯 HRD 평가 모델 기반 분석 결과**
    
    - **Level 1-2 (반응 및 학습)**: 참가자 만족도 4.5/5점, 추천률 95.1%로 매우 긍정적
    - **Level 3 (행동 변화)**: 기술 트렌드 감각 향상과 업무 접근 방식 개선 관찰
    - **Level 4-5 (결과 및 ROI)**: 혁신 프로젝트 발굴과 의사결정 품질 개선 효과
    """)

# 사이드바
st.sidebar.header("📊 대시보드 정보")
st.sidebar.info("""
**Next Chip Talk 교육 성과 분석**

이 대시보드는 2025년 미래반도체 
Next & Grey 영역 교육의 
종합적인 성과를 분석합니다.

- 4회차 세미나 누적 데이터
- HRD 이론 기반 분석
- 실시간 피드백 반영
""")
