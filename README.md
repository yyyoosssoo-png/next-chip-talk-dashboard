# next-chip-talk-dashboard
Next Chip Talk 교육 성과 분석 대시보드
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 페이지 설정
st.set_page_config(
    page_title="Next Chip Talk 교육 성과 분석",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 커스텀 CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, rgba(168, 85, 247, 0.1), rgba(236, 72, 153, 0.1));
        border-radius: 15px;
        margin-bottom: 2rem;
    }
    
    .kpi-card {
        background: linear-gradient(135deg, rgba(168, 85, 247, 0.1), rgba(236, 72, 153, 0.05));
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 4px solid #a855f7;
        margin-bottom: 1rem;
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #a855f7;
        margin-bottom: 0.5rem;
    }
    
    .metric-label {
        font-size: 1.1rem;
        color: #666;
        margin-bottom: 0.25rem;
    }
    
    .metric-desc {
        font-size: 0.9rem;
        color: #999;
    }
    
    .insight-card {
        background: rgba(168, 85, 247, 0.05);
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 3px solid #a855f7;
        margin: 1rem 0;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: rgba(168, 85, 247, 0.1);
        border-radius: 10px;
        color: #666;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #a855f7;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# 헤더
st.markdown("""
<div class="main-header">
    <h1 style="color: #a855f7; font-size: 2.5rem; margin-bottom: 0.5rem;">Next Chip Talk 교육 성과 분석</h1>
    <p style="color: #666; font-size: 1.1rem;">2025 미래반도체 Next & Grey 영역 교육 성과</p>
</div>
""", unsafe_allow_html=True)

# 데이터 정의
@st.cache_data
def load_data():
    # KPI 데이터
    kpi_data = {
        '총 참가자': {'value': '118명', 'desc': '4회차 누적'},
        '평균 만족도': {'value': '4.50', 'desc': '5점 만점'},
        '평균 추천률': {'value': '95.1%', 'desc': '매우 높은 수준'},
        '추정 ROI': {'value': '380%', 'desc': '투자 대비 효과'}
    }
    
    # 회차별 데이터
    session_data = pd.DataFrame({
        '회차': ['1회차\n(4.18)\nOptical', '2회차\n(6.25)\nGlass', '3회차\n(7.30)\nAI Chip', '4회차\n(9.2-3)\nNAND'],
        '참가자수': [38, 38, 25, 17],
        '만족도': [4.5, 4.6, 4.4, 4.5],
        '추천률': [95.0, 97.4, 100.0, 88.2],
        'R&D': [45, 25, 24, 29],
        '사업전략': [35, 50, 52, 24],
        '제조기술': [20, 25, 24, 18]
    })
    
    # 워드클라우드 데이터
    wordcloud_data = {
        '전체': ['양자컴퓨팅 AI 데이터센터 차세대 메모리 반도체 기술 NAND 유리기판 발열 NPU 광통신 미래 시스템 패키징 소재 냉각 아키텍처 엔비디아 트렌드'],
        '1회차': ['광통신 차세대 메모리 포토닉스 CXL PiM 발열 냉각 양자 환경'],
        '2회차': ['유리기판 하이브리드본딩 시스템반도체 액침냉각 양자컴퓨팅 데이터센터 ESG AI 발열'],
        '3회차': ['AI 메모리 NPU 차세대반도체 Custom 소부장 Foundation 시스템 HW SW'],
        '4회차': ['NAND AI 미래기술 신소재 미국반도체 중국산업 시장전망 고객변화 엔비디아']
    }
    
    return kpi_data, session_data, wordcloud_data

kpi_data, session_data, wordcloud_data = load_data()

# 탭 생성
tab1, tab2, tab3, tab4 = st.tabs(["📊 종합 개요", "👥 참가자 구성 변화", "💬 피드백 분석", "💡 전략적 인사이트"])

with tab1:
    st.header("종합 개요")
    
    # KPI 카드들
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="metric-value">118명</div>
            <div class="metric-label">총 참가자</div>
            <div class="metric-desc">4회차 누적</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="metric-value">4.50</div>
            <div class="metric-label">평균 만족도</div>
            <div class="metric-desc">5점 만점</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="metric-value">95.1%</div>
            <div class="metric-label">평균 추천률</div>
            <div class="metric-desc">매우 높은 수준</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="metric-value">380%</div>
            <div class="metric-label">추정 ROI</div>
            <div class="metric-desc">투자 대비 효과</div>
        </div>
        """, unsafe_allow_html=True)
    
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
        fig_satisfaction.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            yaxis_range=[0, 5]
        )
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
        fig_recommendation.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            showlegend=False,
            yaxis_range=[0, 100]
        )
        st.plotly_chart(fig_recommendation, use_container_width=True)
    
    # 주요 성과 요약
    st.subheader("주요 성과 요약")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="insight-card">
            <h4 style="color: #a855f7;">🎯 교육 효과성</h4>
            <ul>
                <li>만족도 4.5/5점으로 목표 대비 125% 달성</li>
                <li>추천률 95.1%로 업계 최고 수준</li>
                <li>4회차 연속 안정적 품질 유지</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="insight-card">
            <h4 style="color: #a855f7;">📊 참가자 특성</h4>
            <ul>
                <li>SK하이닉스 임직원 중심 구성 (76%)</li>
                <li>시니어(10년+) 71.2% 참여로 질적 수준 확보</li>
                <li>R&D→사업전략→제조기술 순 참여</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="insight-card">
            <h4 style="color: #a855f7;">🔄 기술 트렌드 제공</h4>
            <ul>
                <li>광통신 → 유리기판 → AI메모리 → NAND</li>
                <li>신기술에서 응용기술로 진화</li>
                <li>시장분석과 기술설명 균형 유지</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.header("참가자 구성 변화")
    
    # 회차별 구성 변화 시각화
    st.subheader("회차별 참가자 구성 변화")
    
    # 직군별 참여 추이
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("직군별 참여 추이")
        fig_dept = go.Figure()
        
        fig_dept.add_trace(go.Scatter(
            x=session_data['회차'],
            y=session_data['R&D'],
            mode='lines+markers',
            name='R&D',
            line=dict(color='#a855f7', width=3),
            marker=dict(size=8)
        ))
        
        fig_dept.add_trace(go.Scatter(
            x=session_data['회차'],
            y=session_data['사업전략'],
            mode='lines+markers',
            name='사업전략',
            line=dict(color='#06b6d4', width=3),
            marker=dict(size=8)
        ))
        
        fig_dept.add_trace(go.Scatter(
            x=session_data['회차'],
            y=session_data['제조기술'],
            mode='lines+markers',
            name='제조/기술',
            line=dict(color='#10b981', width=3),
            marker=dict(size=8)
        ))
        
        fig_dept.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            yaxis=dict(title='참여 비율 (%)', range=[0, 60])
        )
        
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
        
        fig_exp.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white'
        )
        
        st.plotly_chart(fig_exp, use_container_width=True)

with tab3:
    st.header("피드백 분석")
    
    # 워드클라우드
    st.subheader("주관식 피드백 키워드 분석")
    
    session_choice = st.selectbox(
        "회차 선택:",
        ['전체', '1회차', '2회차', '3회차', '4회차']
    )
    
    if session_choice in wordcloud_data:
        wordcloud_text = wordcloud_data[session_choice][0]
        
        # 워드클라우드 생성
        wordcloud = WordCloud(
            width=800, 
            height=400, 
            background_color='white',
            font_path=None,
            colormap='plasma'
        ).generate(wordcloud_text)
        
        fig_wc, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig_wc)
    
    # 감정 분석 대시보드
    st.subheader("감정 분석 대시보드")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(5, 150, 105, 0.05)); padding: 1.5rem; border-radius: 15px; border-left: 4px solid #10b981;">
            <h4 style="color: #10b981;">😊 긍정적 피드백</h4>
            <h2 style="color: #10b981; margin: 1rem 0;">87건 (74%)</h2>
            <p style="color: #666; font-size: 0.9rem;">"매우 만족", "유익한 시간", "도움이 되었습니다"</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(245, 158, 11, 0.1), rgba(217, 119, 6, 0.05)); padding: 1.5rem; border-radius: 15px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #f59e0b;">😐 중립적 피드백</h4>
            <h2 style="color: #f59e0b; margin: 1rem 0;">21건 (18%)</h2>
            <p style="color: #666; font-size: 0.9rem;">"적당한 난이도", "보통", "괜찮았습니다"</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(239, 68, 68, 0.1), rgba(220, 38, 38, 0.05)); padding: 1.5rem; border-radius: 15px; border-left: 4px solid #ef4444;">
            <h4 style="color: #ef4444;">😔 개선 요청</h4>
            <h2 style="color: #ef4444; margin: 1rem 0;">10건 (8%)</h2>
            <p style="color: #666; font-size: 0.9rem;">"시간 부족", "접근성 문제", "화면 표시 요청"</p>
        </div>
        """, unsafe_allow_html=True)
    
    # 회차별 감정 분석과 요청 사항
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
        
        fig_sentiment.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white'
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
        
        fig_request.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white'
        )
        
        st.plotly_chart(fig_request, use_container_width=True)

with tab4:
    st.header("전략적 인사이트")
    
    # 교육 개요
    st.subheader("Next Chip Talk 교육 개요")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="insight-card">
            <h4 style="color: #a855f7;">🎯 교육 목적</h4>
            <p>급변하는 반도체 패러다임에 대응하기 위하여 근미래에 상용화될 가능성이 높은 반도체 기술을 조망하고, 최신 연구 동향과 기술적 난제에 대한 이해를 높여 기술 인사이트 향상을 목표로 함.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="insight-card">
            <h4 style="color: #a855f7;">📚 학습 방식</h4>
            <ul>
                <li>현장 참여 세미나</li>
                <li>온라인 생중계를 통한 실시간 웨비나</li>
                <li>추후 동영상 mySUNI 플랫폼에 녹화본 업로드</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="insight-card">
            <h4 style="color: #a855f7;">👥 수강 대상</h4>
            <p>반도체 관련 멤버사의 기술/개발 및 전략/마케팅 구성원, 반도체 신기술 및 신사업에 대한 기술 동향 지식이 필요한 구성원</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="insight-card">
            <h4 style="color: #a855f7;">🎬 학습 구성</h4>
            <ul>
                <li>모더레이터의 주제 키노트</li>
                <li>전문가 강연 (학계 + 산업계)</li>
                <li>대담과 질의 응답</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # HRD 기반 교육 전략
    st.subheader("HRD 기반 교육 전략")
    
    strategy_col1, strategy_col2 = st.columns(2)
    
    with strategy_col1:
        st.markdown("""
        <div class="insight-card">
            <h4 style="color: #a855f7;">📈 참가자 확보 전략</h4>
            <ul>
                <li>타겟 직군별 맞춤 마케팅 (R&D 40%, 사업전략 35%)</li>
                <li>시즌별 참여도 분석 반영 (가을철 참여도 하락 대응)</li>
                <li>조직의 Needs와 고객의 Wants를 반영하기 위한 정기적 고객 조사 실시</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="insight-card">
            <h4 style="color: #a855f7;">⚙️ 운영 혁신</h4>
            <ul>
                <li>실시간 Q&A 화면 표시 시스템 도입</li>
                <li>지역별 접근성 개선 (청주, 이천 고려)</li>
                <li>강의자료 사전/사후 제공 체계</li>
                <li>질의응답 시간 30% 확대</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="insight-card">
            <h4 style="color: #a855f7;">🔄 지속가능성 확보</h4>
            <ul>
                <li>기술 전문가 네트워킹 플랫폼 구축</li>
                <li>분기별 기술 동향 레포트 제공</li>
                <li>mySUNI 커뮤니티 기반 후속 스터디 도입</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with strategy_col2:
        st.markdown("""
        <div class="insight-card">
            <h4 style="color: #a855f7;">🎯 기술 인사이트 강화</h4>
            <ul>
                <li>양자컴퓨팅 전문 세션 신설 (수요 35% 반영)</li>
                <li>AI 데이터센터 심화 과정 (발열/냉각 기술 포함)</li>
                <li>차세대 메모리 기술 시리즈 구성</li>
                <li>기술 트렌드 감각 향상 중심 콘텐츠</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="insight-card">
            <h4 style="color: #a855f7;">💰 ROI 평가 체계</h4>
            <ul>
                <li>Kirkpatrick-Phillips 5단계 모델 기반 체계적 평가</li>
                <li>직접비용 대비 간접효과 측정</li>
                <li>참가자 교육 전후 성과 변화 추적 시스템</li>
                <li>3년 단위 장기 평가 계획</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Kirkpatrick 평가 모델
    st.subheader("Kirkpatrick-Phillips 5단계 평가")
    
    kirkpatrick_data = pd.DataFrame({
        '평가단계': ['Level1\n반응', 'Level2\n학습', 'Level3\n인사이트', 'Level4\n결과', 'Level5\nROI'],
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
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=True,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white'
    )
    
    st.plotly_chart(fig_kirkpatrick, use_container_width=True)
    
    # HRD 평가 모델 기반 분석
    st.markdown("""
    <div class="insight-card">
        <h4 style="color: #a855f7;">HRD 평가 모델 기반 교육 효과성 분석</h4>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 1rem;">
            <div>
                <h5 style="color: #a855f7;">Level 1-2: 반응 및 학습</h5>
                <p style="color: #666; font-size: 0.9rem;">
                    참가자 만족도 4.5/5점, 추천률 95.1%로 교육에 대한 즉각적 반응이 매우 긍정적. 
                    기술 이해도 향상과 새로운 지식 습득이 효과적으로 이루어짐.
                </p>
            </div>
            <div>
                <h5 style="color: #a855f7;">Level 3: 행동 변화 (인사이트)</h5>
                <p style="color: #666; font-size: 0.9rem;">
                    참가자들의 기술 트렌드 감각 향상과 업무 접근 방식 개선이 관찰됨. 
                    후속 연구 및 프로젝트 기획에 교육 내용이 반영되는 사례 증가.
                </p>
            </div>
            <div>
                <h5 style="color: #a855f7;">Level 4-5: 결과 및 ROI</h5>
                <p style="color: #666; font-size: 0.9rem;">
                    기술 인사이트 향상을 통한 혁신 프로젝트 발굴과 의사결정 품질 개선. 
                    교육 투자 대비 조직 성과 창출 효과가 지속적으로 증가하는 추세.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 사이드바에 추가 정보
with st.sidebar:
    st.header("📊 대시보드 정보")
    st.info("""
    **Next Chip Talk 교육 성과 분석**
    
    이 대시보드는 2025년 미래반도체 Next & Grey 영역 교육의 
    종합적인 성과를 분석합니다.
    
    - 4회차 세미나 누적 데이터
    - HRD 이론 기반 분석
    - 실시간 피드백 반영
    """)
    
    st.header("🔗 관련 링크")
    st.markdown("""
    - [mySUNI 플랫폼](https://mysuni.sk.com)
    - [SK하이닉스 기술블로그](https://news.skhynix.com)
    """)
