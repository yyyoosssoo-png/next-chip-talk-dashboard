import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime

# 페이지 설정
st.set_page_config(
    page_title="Next Chip Talk 교육 성과 분석",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 커스텀 CSS 스타일
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Noto+Sans+KR:wght@300;400;500;600;700&display=swap');
    
    /* 전체 앱 배경 */
    .stApp {
        background: linear-gradient(135deg, #000000 0%, #0a0a1a 30%, #1a1a2e 70%, #0a0a1a 100%);
        color: #ffffff;
    }
    
    /* 메인 컨테이너 */
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 1400px;
    }
    
    /* 헤더 스타일 */
    .header-container {
        text-align: center;
        padding: 2rem 0;
        margin-bottom: 2rem;
        background: rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.12);
    }
    
    .main-title {
        font-family: 'Orbitron', monospace;
        font-size: 2.5rem;
        font-weight: 600;
        color: #ffffff;
        text-shadow: 0 5px 15px rgba(255, 255, 255, 0.1);
        margin-bottom: 0.5rem;
    }
    
    .sub-title {
        font-size: 1.2rem;
        color: #b8b9ff;
        font-weight: 300;
        margin-bottom: 1rem;
    }
    
    .accent-line {
        width: 120px;
        height: 4px;
        background: linear-gradient(90deg, #a855f7, #ec4899, #06b6d4);
        margin: 0 auto;
        border-radius: 2px;
        box-shadow: 0 0 20px rgba(168, 85, 247, 0.5);
    }
    
    /* KPI 카드 스타일 */
    .kpi-card {
        background: rgba(255, 255, 255, 0.08);
        padding: 1.5rem;
        border-radius: 20px;
        text-align: center;
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.12);
        margin: 0.5rem 0;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .kpi-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, #a855f7, #ec4899, #06b6d4);
    }
    
    .kpi-value {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #a855f7, #ec4899, #06b6d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .kpi-label {
        font-size: 1.1rem;
        color: #e5e7eb;
        margin-bottom: 0.3rem;
        font-weight: 500;
    }
    
    .kpi-desc {
        font-size: 0.9rem;
        color: #9ca3af;
        opacity: 0.8;
    }
    
    /* 차트 컨테이너 */
    .chart-container {
        background: rgba(255, 255, 255, 0.08);
        padding: 1.5rem;
        border-radius: 20px;
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.12);
        margin: 1rem 0;
    }
    
    /* 인사이트 카드 */
    .insight-card {
        background: rgba(255, 255, 255, 0.06);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #a855f7;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.08);
    }
    
    .insight-title {
        color: #a855f7;
        font-weight: 600;
        font-size: 1.1rem;
        margin-bottom: 1rem;
    }
    
    /* 탭 스타일 */
    .stTabs [data-baseweb="tab-list"] {
        background: rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 8px;
        backdrop-filter: blur(20px);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 12px;
        color: #d1d5db;
        font-weight: 500;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #a855f7, #ec4899) !important;
        color: white !important;
    }
    
    /* 메트릭 스타일 오버라이드 */
    [data-testid="metric-container"] {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.12);
        padding: 1rem;
        border-radius: 20px;
        backdrop-filter: blur(20px);
    }
    
    [data-testid="metric-container"] > div {
        color: #ffffff;
    }
    
    /* 사이드바 숨기기 */
    .css-1d391kg {
        display: none;
    }
    
    /* 텍스트 색상 */
    .stMarkdown, .stText {
        color: #ffffff;
    }
    
    /* 로고 스타일 */
    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 1rem;
    }
    
    .logo-fallback {
        font-family: 'Orbitron', monospace;
        font-size: 3rem;
        font-weight: 300;
        color: #ffffff;
        letter-spacing: 0.2em;
        text-shadow: 0 0 20px rgba(168, 85, 247, 0.5);
    }
    
    /* 감정 분석 카드들 */
    .sentiment-positive {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.2), rgba(16, 185, 129, 0.1));
        border-left: 4px solid #10b981;
    }
    
    .sentiment-neutral {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.2), rgba(245, 158, 11, 0.1));
        border-left: 4px solid #f59e0b;
    }
    
    .sentiment-negative {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.2), rgba(239, 68, 68, 0.1));
        border-left: 4px solid #ef4444;
    }
    
    /* HRD 섹션 */
    .hrd-section {
        background: linear-gradient(135deg, rgba(168, 85, 247, 0.2), rgba(236, 72, 153, 0.2));
        padding: 2rem;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(20px);
        margin: 2rem 0;
    }
    
    .hrd-title {
        font-size: 1.8rem;
        font-weight: 600;
        text-align: center;
        color: #ffffff;
        margin-bottom: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# 로고 및 헤더
st.markdown("""
<div class="header-container">
    <div class="logo-container">
        <div class="logo-fallback">nct</div>
    </div>
    <h1 class="main-title">Next Chip Talk 교육 성과 분석</h1>
    <p class="sub-title">2025 미래반도체 Next & Grey 영역 교육 성과</p>
    <div class="accent-line"></div>
</div>
""", unsafe_allow_html=True)

# 데이터 정의
@st.cache_data
def load_data():
    session_data = pd.DataFrame({
        '회차': ['1회차\n(4.18)', '2회차\n(6.25)', '3회차\n(7.30)', '4회차\n(9.2-3)'],
        '주제': ['Optical Interconnection', 'Glass Substrate', 'AI Chip 메모리 시스템', 'AI X 차세대 NAND'],
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
tab1, tab2, tab3, tab4 = st.tabs(["📊 종합 개요", "👥 참가자 구성 변화", "💬 피드백 분석", "💡 전략적 인사이트"])

with tab1:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown("## 📊 종합 개요")
    
    # KPI 카드들
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-value">118명</div>
            <div class="kpi-label">총 참가자</div>
            <div class="kpi-desc">4회차 누적</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-value">4.50</div>
            <div class="kpi-label">평균 만족도</div>
            <div class="kpi-desc">5점 만점</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-value">95.1%</div>
            <div class="kpi-label">평균 추천률</div>
            <div class="kpi-desc">매우 높은 수준</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-value">380%</div>
            <div class="kpi-label">추정 ROI</div>
            <div class="kpi-desc">투자 대비 효과</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ROI 상세 분석
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown("### 💰 ROI 380% 상세 분석")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("직접비용 비중", "40%", "강사료, 운영비")
    with col2:
        st.metric("간접비용 비중", "60%", "참가자 시간, 기회비용")
    with col3:
        st.metric("일반교육 ROI", "150%", "업계 평균")
    with col4:
        st.metric("3년차 예상 ROI", "500%", "누적 효과")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 차트들
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.markdown("### 📈 회차별 만족도 추이")
        
        fig_satisfaction = go.Figure()
        fig_satisfaction.add_trace(go.Scatter(
            x=session_data['회차'],
            y=session_data['만족도'],
            mode='lines+markers',
            line=dict(color='#a855f7', width=4),
            marker=dict(color='#a855f7', size=10, line=dict(color='white', width=2)),
            fill='tonexty',
            fillcolor='rgba(168, 85, 247, 0.2)',
            name='만족도'
        ))
        
        fig_satisfaction.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            yaxis_range=[0, 5],
            showlegend=False,
            margin=dict(l=0, r=0, t=0, b=0)
        )
        
        fig_satisfaction.update_xaxes(gridcolor='rgba(255,255,255,0.1)')
        fig_satisfaction.update_yaxes(gridcolor='rgba(255,255,255,0.1)')
        
        st.plotly_chart(fig_satisfaction, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.markdown("### 📊 회차별 추천률 변화")
        
        colors = ['#a855f7', '#ec4899', '#06b6d4', '#10b981']
        
        fig_recommendation = go.Figure()
        fig_recommendation.add_trace(go.Bar(
            x=session_data['회차'],
            y=session_data['추천률'],
            marker_color=colors,
            text=session_data['추천률'].astype(str) + '%',
            textposition='outside'
        ))
        
        fig_recommendation.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            yaxis_range=[0, 105],
            showlegend=False,
            margin=dict(l=0, r=0, t=0, b=0)
        )
        
        fig_recommendation.update_xaxes(gridcolor='rgba(255,255,255,0.1)')
        fig_recommendation.update_yaxes(gridcolor='rgba(255,255,255,0.1)')
        
        st.plotly_chart(fig_recommendation, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # 주요 성과 요약
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown("### 🎯 주요 성과 요약")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="insight-card">
            <div class="insight-title">🎯 교육 효과성</div>
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
            <div class="insight-title">📊 참가자 특성</div>
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
            <div class="insight-title">🔄 기술 트렌드 제공</div>
            <ul>
                <li>광통신 → 유리기판 → AI메모리 → NAND</li>
                <li>신기술에서 응용기술로 진화</li>
                <li>시장분석과 기술설명 균형 유지</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown("## 👥 참가자 구성 변화")
    
    # 회차별 참가자 구성 변화
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown("### 📈 회차별 참가자 구성 변화")
    
    # 세션별 구성 표시
    col1, col2, col3, col4 = st.columns(4)
    
    sessions_info = [
        ("1회차 (4.18)", "Optical Interconnection", [45, 35, 20], ["R&D", "사업전략", "제조/기술"]),
        ("2회차 (6.25)", "Glass Substrate", [25, 50, 25], ["R&D", "사업전략", "제조/기술"]),
        ("3회차 (7.30)", "AI Chip 메모리 시스템", [24, 52, 24], ["R&D", "사업전략", "제조/기술"]),
        ("4회차 (9.2-3)", "AI X 차세대 NAND", [29, 24, 18], ["R&D", "사업전략", "제조/기술"])
    ]
    
    colors_dept = ['#a855f7', '#06b6d4', '#10b981']
    
    for i, (col, (title, topic, values, labels)) in enumerate(zip([col1, col2, col3, col4], sessions_info)):
        with col:
            st.markdown(f"""
            <div style="background: rgba(255, 255, 255, 0.06); padding: 1rem; border-radius: 16px; margin: 0.5rem 0;">
                <div style="color: #a855f7; font-weight: 600; margin-bottom: 0.5rem;">{title}</div>
                <div style="color: #9ca3af; font-size: 0.8rem; margin-bottom: 1rem; font-style: italic;">{topic}</div>
            """, unsafe_allow_html=True)
            
            for j, (label, value) in enumerate(zip(labels, values)):
                st.markdown(f"""
                <div style="margin: 0.5rem 0; display: flex; align-items: center;">
                    <div style="width: 60px; font-size: 0.8rem; color: #e5e7eb;">{label}</div>
                    <div style="flex: 1; height: 8px; background: rgba(255,255,255,0.1); border-radius: 10px; margin: 0 8px; overflow: hidden;">
                        <div style="height: 100%; width: {value}%; background: {colors_dept[j]}; border-radius: 10px;"></div>
                    </div>
                    <div style="font-size: 0.8rem; color: #d1d5db; min-width: 30px;">{value}%</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.markdown("### 📊 직군별 참여 추이")
        
        fig_dept = go.Figure()
        
        colors_line = ['#a855f7', '#06b6d4', '#10b981']
        departments = ['R&D', '사업전략', '제조기술']
        
        for i, dept in enumerate(departments):
            fig_dept.add_trace(go.Scatter(
                x=session_data['회차'],
                y=session_data[dept],
                mode='lines+markers',
                name=dept,
                line=dict(color=colors_line[i], width=3),
                marker=dict(size=8)
            ))
        
        fig_dept.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            yaxis_range=[0, 60],
            yaxis_title='참여 비율 (%)',
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            margin=dict(l=0, r=0, t=0, b=0)
        )
        
        fig_dept.update_xaxes(gridcolor='rgba(255,255,255,0.1)')
        fig_dept.update_yaxes(gridcolor='rgba(255,255,255,0.1)')
        
        st.plotly_chart(fig_dept, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.markdown("### 🎯 경력별 참여 분포")
        
        experience_data = ['10년 이상', '5-10년', '5년 미만']
        experience_values = [71.2, 18.5, 10.3]
        colors_exp = ['#a855f7', '#ec4899', '#06b6d4']
        
        fig_exp = go.Figure(data=[go.Pie(
            labels=experience_data,
            values=experience_values,
            hole=.3,
            marker_colors=colors_exp,
            textinfo='label+percent',
            textfont_size=12
        )])
        
        fig_exp.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            showlegend=False,
            margin=dict(l=0, r=0, t=0, b=0)
        )
        
        st.plotly_chart(fig_exp, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown("## 💬 피드백 분석")
    
    # 감정 분석 대시보드
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown("### 😊 감정 분석 대시보드")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="kpi-card sentiment-positive">
            <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
                <span style="font-size: 1.6rem; margin-right: 12px;">😊</span>
                <span style="font-size: 1.2rem; font-weight: 600;">긍정적 피드백</span>
            </div>
            <div style="font-size: 2.4rem; font-weight: 700; color: #10b981; margin-bottom: 12px;">87건 (74%)</div>
            <div style="font-size: 0.9rem; color: #d1d5db; opacity: 0.9;">
                "매우 만족", "유익한 시간", "도움이 되었습니다", "훌륭한 강의"
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="kpi-card sentiment-neutral">
            <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
                <span style="font-size: 1.6rem; margin-right: 12px;">😐</span>
                <span style="font-size: 1.2rem; font-weight: 600;">중립적 피드백</span>
            </div>
            <div style="font-size: 2.4rem; font-weight: 700; color: #f59e0b; margin-bottom: 12px;">21건 (18%)</div>
            <div style="font-size: 0.9rem; color: #d1d5db; opacity: 0.9;">
                "적당한 난이도", "보통", "괜찮았습니다", "무난했습니다"
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="kpi-card sentiment-negative">
            <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
                <span style="font-size: 1.6rem; margin-right: 12px;">😔</span>
                <span style="font-size: 1.2rem; font-weight: 600;">개선 요청</span>
            </div>
            <div style="font-size: 2.4rem; font-weight: 700; color: #ef4444; margin-bottom: 12px;">10건 (8%)</div>
            <div style="font-size: 0.9rem; color: #d1d5db; opacity: 0.9;">
                "시간 부족", "어려웠다", "접근성 문제", "화면 표시 요청"
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 키워드 분석
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown("### 🔍 주요 피드백 키워드 분석")
    
    keywords_data = {
        '전체': ['양자컴퓨팅', 'AI', '데이터센터', '차세대 메모리', '반도체', '기술 트렌드', 'NAND', '유리기판', '발열 해결'],
        '1회차': ['광통신', '차세대', '메모리', '포토닉스', 'CXL', 'PiM', '발열', '냉각'],
        '2회차': ['유리기판', '하이브리드본딩', '시스템반도체', '액침냉각', '양자컴퓨팅', '데이터센터'],
        '3회차': ['AI', '메모리', 'NPU', '차세대반도체', 'Custom', '소부장', 'Foundation'],
        '4회차': ['NAND', 'AI', '미래기술', '신소재', '미국반도체', '중국산업', '시장전망']
    }
    
    selected_session = st.selectbox("회차 선택", ['전체', '1회차', '2회차', '3회차', '4회차'])
    
    if selected_session in keywords_data:
        keywords = keywords_data[selected_session]
        st.markdown(f"**{selected_session} 주요 키워드**: " + " • ".join([f"**{kw}**" for kw in keywords]))
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.markdown("### 📊 회차별 감정 분석")
        
        sentiment_data = {
            '회차': session_data['회차'],
            '긍정': [85, 92, 78, 65],
            '중립': [12, 6, 18, 25],
            '개선요청': [3, 2, 4, 10]
        }
        
        sentiment_df = pd.DataFrame(sentiment_data)
        
        fig_sentiment = go.Figure()
        
        colors_sentiment = ['#10b981', '#f59e0b', '#ef4444']
        sentiments = ['긍정', '중립', '개선요청']
        
        for i, sentiment in enumerate(sentiments):
            fig_sentiment.add_trace(go.Bar(
                name=sentiment,
                x=sentiment_df['회차'],
                y=sentiment_df[sentiment],
                marker_color=colors_sentiment[i]
            ))
        
        fig_sentiment.update_layout(
            barmode='stack',
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            margin=dict(l=0, r=0, t=0, b=0)
        )
        
        fig_sentiment.update_xaxes(gridcolor='rgba(255,255,255,0.1)')
        fig_sentiment.update_yaxes(gridcolor='rgba(255,255,255,0.1)')
        
        st.plotly_chart(fig_sentiment, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.markdown("### 🎯 주요 요청 사항 분포")
        
        request_labels = ['양자컴퓨팅', 'AI/데이터센터', '차세대 메모리', '발열 해결', '기타']
        request_values = [35, 25, 20, 15, 5]
        colors_request = ['#a855f7', '#ec4899', '#06b6d4', '#10b981', '#f59e0b']
        
        fig_request = go.Figure(data=[go.Pie(
            labels=request_labels,
            values=request_values,
            hole=.3,
            marker_colors=colors_request,
            textinfo='label+percent',
            textfont_size=12
        )])
        
        fig_request.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            showlegend=False,
            margin=dict(l=0, r=0, t=0, b=0)
        )
        
        st.plotly_chart(fig_request, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

with tab4:
    st.markdown("## 💡 전략적 인사이트")
    
    # 교육 개요
    st.markdown("""
    <div class="hrd-section">
        <div class="hrd-title">📚 Next Chip Talk 교육 개요</div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="insight-card">
            <div class="insight-title">🎯 교육 목적</div>
            <p>급변하는 반도체 패러다임에 대응하기 위하여 근미래에 상용화될 가능성이 높은 반도체 기술을 조망하고, 
            최신 연구 동향과 기술적 난제에 대한 이해를 높여 기술 인사이트 향상을 목표로 함.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="insight-card">
            <div class="insight-title">📚 학습 방식</div>
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
            <div class="insight-title">👥 수강 대상</div>
            <p>반도체 관련 멤버사의 기술/개발 및 전략/마케팅 구성원, 반도체 신기술 및 신사업에 대한 
            기술 동향 지식이 필요한 구성원 (기본적인 반도체 공정 기술에 대한 이해 필요)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="insight-card">
            <div class="insight-title">🎬 학습 구성</div>
            <ul>
                <li>모더레이터의 주제 키노트</li>
                <li>전문가 강연 (학계 + 산업계)</li>
                <li>대담과 질의 응답</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # HRD 기반 교육 전략
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown("### 🚀 HRD 기반 교육 전략")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="insight-card">
            <div class="insight-title">📈 참가자 확보 전략</div>
            <ul>
                <li>타겟 직군별 맞춤 마케팅 (R&D 40%, 사업전략 35%)</li>
                <li>시즌별 참여도 분석 반영 (가을철 참여도 하락 대응)</li>
                <li>조직의 Needs와 고객의 Wants를 반영하기 위한 정기적 고객 조사 실시</li>
                <li>다양한 기업문화와 학습 선호도를 고려한 참여 확산 전략</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="insight-card">
            <div class="insight-title">⚙️ 운영 혁신</div>
            <ul>
                <li>실시간 Q&A 화면 표시 시스템 도입</li>
                <li>지역별 접근성 개선 (청주, 이천 고려)</li>
                <li>강의자료 사전/사후 제공 체계</li>
                <li>질의응답 시간 30% 확대 (현재 + 추가 30분)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="insight-card">
            <div class="insight-title">🔄 지속가능성 확보</div>
            <ul>
                <li>기술 전문가 네트워킹 플랫폼 구축</li>
                <li>분기별 기술 동향 레포트 제공</li>
                <li>mySUNI 커뮤니티 기반 후속 스터디 도입</li>
                <li>글로벌 반도체 교육 허브로 발전</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="insight-card">
            <div class="insight-title">🎯 기술 인사이트 강화</div>
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
            <div class="insight-title">💰 ROI 평가 체계</div>
            <ul>
                <li>Kirkpatrick-Phillips 5단계 모델 기반 체계적 평가</li>
                <li>직접비용(강사료, 운영비) 대비 간접효과(업무생산성, 혁신창출) 측정</li>
                <li>참가자 교육 전후 성과 변화 추적 시스템 구축</li>
                <li>장기 누적효과 극대화를 위한 3년 단위 평가 계획</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Kirkpatrick 평가 모델
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown("### 📊 Kirkpatrick-Phillips 5단계 평가 및 목표")
    
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
        line_color='#a855f7',
        fillcolor='rgba(168, 85, 247, 0.3)'
    ))
    
    fig_kirkpatrick.add_trace(go.Scatterpolar(
        r=kirkpatrick_data['2025목표'],
        theta=kirkpatrick_data['평가단계'],
        fill='toself',
        name='2025 목표',
        line_color='#ec4899',
        line_dash='dash',
        fillcolor='rgba(236, 72, 153, 0.2)'
    ))
    
    fig_kirkpatrick.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                gridcolor='rgba(255,255,255,0.3)',
                linecolor='rgba(255,255,255,0.3)'
            ),
            angularaxis=dict(
                gridcolor='rgba(255,255,255,0.3)',
                linecolor='rgba(255,255,255,0.3)'
            )
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.1,
            xanchor="center",
            x=0.5
        ),
        margin=dict(l=0, r=0, t=0, b=0)
    )
    
    st.plotly_chart(fig_kirkpatrick, use_container_width=True)
    
    # HRD 평가 모델 설명
    st.markdown("""
    <div class="insight-card">
        <div class="insight-title">🎯 HRD 평가 모델 기반 교육 효과성 분석</div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">
            <div>
                <h5 style="color: #ffffff; margin-bottom: 10px; font-size: 0.95rem;">Level 1-2: 반응 및 학습</h5>
                <p style="color: #d1d5db; font-size: 0.9rem; line-height: 1.5;">
                    참가자 만족도 4.5/5점, 추천률 95.1%로 교육에 대한 즉각적 반응이 매우 긍정적. 
                    기술 이해도 향상과 새로운 지식 습득이 효과적으로 이루어짐.
                </p>
            </div>
            <div>
                <h5 style="color: #ffffff; margin-bottom: 10px; font-size: 0.95rem;">Level 3: 행동 변화 (인사이트)</h5>
                <p style="color: #d1d5db; font-size: 0.9rem; line-height: 1.5;">
                    참가자들의 기술 트렌드 감각 향상과 업무 접근 방식 개선이 관찰됨. 
                    후속 연구 및 프로젝트 기획에 교육 내용이 반영되는 사례 증가.
                </p>
            </div>
            <div>
                <h5 style="color: #ffffff; margin-bottom: 10px; font-size: 0.95rem;">Level 4-5: 결과 및 ROI</h5>
                <p style="color: #d1d5db; font-size: 0.9rem; line-height: 1.5;">
                    기술 인사이트 향상을 통한 혁신 프로젝트 발굴과 의사결정 품질 개선. 
                    교육 투자 대비 조직 성과 창출 효과가 지속적으로 증가하는 추세.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# 푸터
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #9ca3af; font-size: 0.9rem; padding: 1rem;">
    📊 Next Chip Talk 교육 성과 분석 대시보드 | 
    🕒 마지막 업데이트: {datetime.now().strftime('%Y-%m-%d %H:%M')} | 
    💡 HRD 이론 기반 분석
</div>
""", unsafe_allow_html=True)
