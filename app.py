import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime
import base64

# 페이지 설정

st.set_page_config(
page_title=“Next Chip Talk 교육 성과 분석”,
page_icon=“🔬”,
layout=“wide”,
initial_sidebar_state=“collapsed”
)

# 로고 업로드 기능

logo_file = st.file_uploader(“로고 이미지 업로드 (선택사항)”, type=[‘png’, ‘jpg’, ‘jpeg’], key=“logo_uploader”)

# 커스텀 CSS 스타일 (별똥별 배경 + 모든 개선사항 포함)

st.markdown(”””

<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Noto+Sans+KR:wght@300;400;500;600;700&display=swap');
    
    /* 전체 앱 배경 - 검은색 + 별똥별 효과 */
    .stApp {
        background: linear-gradient(135deg, #000000 0%, #0a0a1a 30%, #1a1a2e 70%, #0a0a1a 100%);
        background-size: 400% 400%;
        animation: gradientShift 20s ease infinite;
        color: #ffffff;
        position: relative;
        overflow-x: hidden;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* 별똥별 효과 */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(2px 2px at 20px 30px, rgba(255, 255, 255, 0.8), transparent),
            radial-gradient(2px 2px at 40px 70px, rgba(168, 85, 247, 0.6), transparent),
            radial-gradient(1px 1px at 90px 40px, rgba(255, 255, 255, 0.4), transparent),
            radial-gradient(1px 1px at 130px 80px, rgba(236, 72, 153, 0.5), transparent),
            radial-gradient(2px 2px at 160px 30px, rgba(255, 255, 255, 0.3), transparent),
            radial-gradient(1px 1px at 200px 90px, rgba(6, 182, 212, 0.4), transparent),
            radial-gradient(1px 1px at 250px 50px, rgba(255, 255, 255, 0.6), transparent),
            radial-gradient(2px 2px at 300px 20px, rgba(168, 85, 247, 0.3), transparent),
            radial-gradient(1px 1px at 350px 60px, rgba(255, 255, 255, 0.5), transparent);
        background-repeat: repeat;
        background-size: 350px 200px;
        animation: sparkle 25s linear infinite;
        pointer-events: none;
        z-index: 0;
    }
    
    @keyframes sparkle {
        0% { transform: translate(0, 0); }
        100% { transform: translate(-350px, -200px); }
    }
    
    /* 메인 컨테이너 - 별똥별 위에 표시되도록 z-index 조정 */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1400px;
        position: relative;
        z-index: 1;
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
        position: relative;
        z-index: 2;
    }
    
    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 1.5rem;
    }
    
    .logo-fallback {
        font-family: 'Orbitron', 'Courier New', monospace !important;
        font-size: 4rem;
        font-weight: 300;
        color: #ffffff;
        letter-spacing: 0.2em;
        text-shadow: 0 10px 30px rgba(168, 85, 247, 0.3);
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }
    
    .logo-image {
        max-width: 350px;
        width: 100%;
        height: auto;
        margin-bottom: 25px;
        filter: drop-shadow(0 10px 30px rgba(168, 85, 247, 0.3));
        transition: all 0.3s ease;
    }
    
    .logo-image:hover {
        transform: translateY(-5px);
        filter: drop-shadow(0 20px 40px rgba(168, 85, 247, 0.4));
    }
    
    .main-title {
        font-family: 'Orbitron', 'Courier New', monospace !important;
        font-size: 2.4rem;
        font-weight: 600;
        color: #ffffff;
        text-shadow: 0 5px 15px rgba(255, 255, 255, 0.1);
        margin: 25px 0 15px 0;
        letter-spacing: 0.05em;
    }
    
    .sub-title {
        font-size: 1.1rem;
        color: #b8b9ff;
        font-weight: 300;
        margin-bottom: 1rem;
        line-height: 1.6;
    }
    
    .accent-line {
        width: 120px;
        height: 4px;
        background: linear-gradient(90deg, #a855f7, #ec4899, #06b6d4);
        margin: 25px auto;
        border-radius: 2px;
        box-shadow: 0 0 20px rgba(168, 85, 247, 0.5);
    }
    
    /* 인포그래픽 아이콘 스타일 */
    .icon-overview {
        display: inline-block;
        width: 16px;
        height: 16px;
        margin-right: 8px;
        background: linear-gradient(135deg, #a855f7, #ec4899);
        clip-path: polygon(0% 0%, 100% 0%, 100% 75%, 75% 100%, 0% 100%);
        vertical-align: middle;
    }
    
    .icon-composition {
        display: inline-block;
        width: 16px;
        height: 16px;
        margin-right: 8px;
        background: linear-gradient(135deg, #06b6d4, #10b981);
        clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
        vertical-align: middle;
    }
    
    .icon-feedback {
        display: inline-block;
        width: 16px;
        height: 16px;
        margin-right: 8px;
        background: linear-gradient(135deg, #ec4899, #f59e0b);
        border-radius: 50%;
        vertical-align: middle;
    }
    
    .icon-insights {
        display: inline-block;
        width: 16px;
        height: 16px;
        margin-right: 8px;
        background: linear-gradient(135deg, #f59e0b, #a855f7);
        clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
        vertical-align: middle;
    }
    
    .icon-chart-line {
        display: inline-block;
        width: 16px;
        height: 16px;
        margin-right: 8px;
        background: linear-gradient(135deg, #a855f7, #ec4899);
        clip-path: polygon(0% 100%, 0% 60%, 25% 40%, 50% 70%, 75% 20%, 100% 50%, 100% 100%);
        vertical-align: middle;
    }
    
    .icon-users {
        display: inline-block;
        width: 16px;
        height: 16px;
        margin-right: 8px;
        background: linear-gradient(135deg, #06b6d4, #10b981);
        clip-path: circle(30% at 35% 35%), circle(30% at 65% 35%), circle(50% at 50% 75%);
        vertical-align: middle;
    }
    
    .icon-target {
        display: inline-block;
        width: 16px;
        height: 16px;
        margin-right: 8px;
        background: linear-gradient(135deg, #a855f7, #ec4899);
        border-radius: 50%;
        position: relative;
        vertical-align: middle;
    }
    
    .icon-target::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 6px;
        height: 6px;
        background: #ffffff;
        border-radius: 50%;
    }
    
    .icon-lightbulb {
        display: inline-block;
        width: 16px;
        height: 16px;
        margin-right: 8px;
        background: linear-gradient(135deg, #f59e0b, #a855f7);
        clip-path: circle(40%);
        filter: drop-shadow(0 0 6px rgba(245, 158, 11, 0.6));
        vertical-align: middle;
    }
    
    .icon-money {
        display: inline-block;
        width: 16px;
        height: 16px;
        margin-right: 8px;
        background: linear-gradient(135deg, #f59e0b, #ec4899);
        clip-path: polygon(30% 0%, 70% 0%, 100% 30%, 100% 70%, 70% 100%, 30% 100%, 0% 70%, 0% 30%);
        vertical-align: middle;
    }
    
    .icon-gear {
        display: inline-block;
        width: 16px;
        height: 16px;
        margin-right: 8px;
        background: linear-gradient(135deg, #06b6d4, #ec4899);
        clip-path: polygon(50% 0%, 80% 10%, 100% 35%, 90% 70%, 65% 100%, 35% 100%, 10% 70%, 0% 35%, 20% 10%);
        vertical-align: middle;
    }
    
    .icon-growth {
        display: inline-block;
        width: 16px;
        height: 16px;
        margin-right: 8px;
        background: linear-gradient(135deg, #ec4899, #a855f7);
        clip-path: polygon(0% 100%, 20% 60%, 40% 80%, 60% 40%, 80% 60%, 100% 0%, 100% 100%);
        vertical-align: middle;
    }
    
    .icon-loop {
        display: inline-block;
        width: 16px;
        height: 16px;
        margin-right: 8px;
        background: linear-gradient(135deg, #10b981, #06b6d4);
        border-radius: 50%;
        border: 2px solid transparent;
        background-clip: padding-box;
        vertical-align: middle;
    }
    
    .icon-book {
        display: inline-block;
        width: 16px;
        height: 16px;
        margin-right: 8px;
        background: linear-gradient(135deg, #a855f7, #ec4899);
        clip-path: polygon(0% 0%, 100% 0%, 100% 80%, 80% 100%, 0% 100%);
        vertical-align: middle;
    }
    
    .icon-rocket {
        display: inline-block;
        width: 16px;
        height: 16px;
        margin-right: 8px;
        background: linear-gradient(135deg, #f59e0b, #a855f7);
        clip-path: polygon(50% 0%, 100% 100%, 80% 85%, 50% 70%, 20% 85%, 0% 100%);
        vertical-align: middle;
    }
    
    /* 탭 스타일 */
    .stTabs [data-baseweb="tab-list"] {
        background: rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 8px;
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.12);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        gap: 8px;
        position: relative;
        z-index: 2;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 12px;
        color: #d1d5db !important;
        font-weight: 500;
        font-family: 'Noto Sans KR', sans-serif;
        transition: all 0.4s ease;
        padding: 16px 20px;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #a855f7, #ec4899) !important;
        color: white !important;
        transform: translateY(-3px);
        box-shadow: 0 12px 30px rgba(168, 85, 247, 0.4);
    }
    
    .stTabs [data-baseweb="tab"]:hover:not([aria-selected="true"]) {
        background: rgba(255, 255, 255, 0.15) !important;
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(255, 255, 255, 0.1);
    }
    
    /* KPI 카드 스타일 */
    .kpi-card {
        background: rgba(255, 255, 255, 0.08);
        padding: 30px 25px;
        border-radius: 20px;
        text-align: center;
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.12);
        margin: 0.5rem 0;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
        z-index: 2;
    }
    
    .kpi-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, #a855f7, #ec4899, #06b6d4);
        transform: translateX(-100%);
        transition: transform 0.6s ease;
    }
    
    .kpi-card:hover::before {
        transform: translateX(0);
    }
    
    .kpi-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 50px rgba(168, 85, 247, 0.25);
        background: rgba(255, 255, 255, 0.12);
    }
    
    .kpi-value {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #a855f7, #ec4899, #06b6d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 12px;
    }
    
    .kpi-label {
        font-size: 1.1rem;
        color: #e5e7eb;
        margin-bottom: 8px;
        font-weight: 500;
    }
    
    .kpi-desc {
        font-size: 0.95rem;
        color: #9ca3af;
        opacity: 0.8;
    }
    
    /* 차트 컨테이너 */
    .chart-container {
        background: rgba(255, 255, 255, 0.08);
        padding: 30px;
        border-radius: 20px;
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.12);
        margin: 1rem 0;
        transition: all 0.3s ease;
        position: relative;
        z-index: 2;
    }
    
    .chart-container:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2);
    }
    
    /* 인사이트 카드 */
    .insight-card {
        background: rgba(255, 255, 255, 0.06);
        padding: 25px;
        border-radius: 12px;
        border-left: 4px solid #a855f7;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.08);
        transition: all 0.3s ease;
        position: relative;
        z-index: 2;
    }
    
    .insight-card:hover {
        background: rgba(255, 255, 255, 0.1);
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(168, 85, 247, 0.15);
    }
    
    .insight-title {
        color: #a855f7;
        font-weight: 600;
        font-size: 1.1rem;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
    }
    
    .insight-card ul {
        color: #e5e7eb;
        line-height: 1.6;
    }
    
    .insight-card li {
        margin-bottom: 8px;
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
    
    /* 교육 개요 섹션 */
    .education-overview {
        background: linear-gradient(135deg, rgba(168, 85, 247, 0.2), rgba(236, 72, 153, 0.2));
        padding: 35px;
        border-radius: 20px;
        margin: 2rem 0;
        border: 1px solid rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(20px);
        position: relative;
        z-index: 2;
    }
    
    .education-title {
        font-size: 2rem;
        font-weight: 600;
        text-align: center;
        color: #ffffff;
        margin-bottom: 1.5rem;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    .education-item {
        background: rgba(255, 255, 255, 0.12);
        padding: 25px;
        border-radius: 16px;
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    
    .education-item:hover {
        transform: translateY(-3px);
        background: rgba(255, 255, 255, 0.18);
    }
    
    .education-item h4 {
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 12px;
        color: #ffffff;
        display: flex;
        align-items: center;
    }
    
    .education-item p, .education-item ul {
        font-size: 0.95rem;
        line-height: 1.6;
        color: rgba(255, 255, 255, 0.9);
    }
    
    .education-item ul {
        padding-left: 0;
        list-style: none;
    }
    
    .education-item li {
        margin-bottom: 10px;
        padding-left: 20px;
        position: relative;
    }
    
    .education-item li::before {
        content: "▸";
        position: absolute;
        left: 0;
        color: #fbbf24;
        font-weight: bold;
    }
    
    /* 세션 구성 카드 */
    .session-composition {
        text-align: center;
        padding: 20px;
        border-radius: 16px;
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.08);
        margin: 0.5rem;
        transition: all 0.3s ease;
        position: relative;
        z-index: 2;
    }
    
    .session-composition:hover {
        background: rgba(255, 255, 255, 0.1);
        transform: translateY(-3px);
    }
    
    .session-title {
        font-weight: 600;
        margin-bottom: 8px;
        color: #a855f7;
        font-size: 0.95rem;
        line-height: 1.3;
    }
    
    .session-topic {
        font-size: 0.8rem;
        color: #9ca3af;
        margin-bottom: 15px;
        font-style: italic;
        opacity: 0.8;
    }
    
    .dept-bar {
        margin: 10px 0;
        display: flex;
        align-items: center;
    }
    
    .dept-name {
        width: 70px;
        font-size: 0.8rem;
        text-align: left;
        color: #e5e7eb;
    }
    
    .dept-progress {
        flex: 1;
        height: 8px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        margin: 0 8px;
        overflow: hidden;
    }
    
    .dept-fill {
        height: 100%;
        border-radius: 10px;
        transition: width 0.8s ease;
    }
    
    .dept-percent {
        font-size: 0.8rem;
        min-width: 35px;
        color: #d1d5db;
        font-weight: 500;
    }
    
    /* HRD 분석 섹션 */
    .hrd-analysis {
        margin-top: 30px;
        padding: 25px;
        background: rgba(255, 255, 255, 0.06);
        border-radius: 12px;
        border-left: 4px solid #a855f7;
        position: relative;
        z-index: 2;
    }
    
    .hrd-analysis h4 {
        color: #a855f7;
        margin-bottom: 15px;
        font-weight: 600;
        display: flex;
        align-items: center;
    }
    
    .hrd-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 20px;
    }
    
    .hrd-item h5 {
        color: #ffffff;
        margin-bottom: 10px;
        font-size: 0.95rem;
    }
    
    .hrd-item p {
        color: #d1d5db;
        font-size: 0.9rem;
        line-height: 1.5;
    }
    
    /* Streamlit 기본 요소들 스타일 조정 */
    .stMarkdown, .stText {
        color: #ffffff !important;
        position: relative;
        z-index: 2;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
        font-family: 'Orbitron', 'Courier New', monospace !important;
    }
    
    .stSelectbox > div > div {
        background-color: rgba(255, 255, 255, 0.1);
        color: #ffffff;
        position: relative;
        z-index: 2;
    }
    
    /* 사이드바 숨기기 */
    section[data-testid="stSidebar"] {
        display: none;
    }
    
    /* 메트릭 컨테이너 스타일 */
    [data-testid="metric-container"] {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.12);
        padding: 1rem;
        border-radius: 20px;
        backdrop-filter: blur(20px);
        position: relative;
        z-index: 2;
    }
    
    [data-testid="metric-container"] > div {
        color: #ffffff !important;
    }
    
    [data-testid="metric-container"] [data-testid="metric-value"] {
        color: #ffffff !important;
    }
    
    [data-testid="metric-container"] [data-testid="metric-label"] {
        color: #d1d5db !important;
    }
    
    /* 파일 업로더 스타일 */
    .stFileUploader > div {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 12px;
        backdrop-filter: blur(20px);
        position: relative;
        z-index: 2;
    }
    
    .stFileUploader label {
        color: #ffffff !important;
    }
</style>

“””, unsafe_allow_html=True)

# 로고 및 헤더

if logo_file is not None:
logo_bytes = logo_file.read()
logo_base64 = base64.b64encode(logo_bytes).decode()

```
st.markdown(f"""
<div class="header-container">
    <div class="logo-container">
        <img src="data:image/png;base64,{logo_base64}" alt="Logo" class="logo-image">
    </div>
    <h1 class="main-title">Next Chip Talk 교육 성과 분석</h1>
    <p class="sub-title">2025 미래반도체 Next & Grey 영역 교육 성과</p>
    <div class="accent-line"></div>
</div>
""", unsafe_allow_html=True)
```

else:
st.markdown(”””
<div class="header-container">
<div class="logo-container">
<div class="logo-fallback">nct</div>
</div>
<h1 class="main-title">Next Chip Talk 교육 성과 분석</h1>
<p class="sub-title">2025 미래반도체 Next & Grey 영역 교육 성과</p>
<div class="accent-line"></div>
</div>
“””, unsafe_allow_html=True)

# 데이터 정의

@st.cache_data
def load_data():
session_data = pd.DataFrame({
‘회차’: [‘1회차\n(4.18)’, ‘2회차\n(6.25)’, ‘3회차\n(7.30)’, ‘4회차\n(9.2-3)’],
‘주제’: [‘Optical Interconnection’, ‘Glass Substrate’, ‘AI Chip 메모리 시스템’, ‘AI X 차세대 NAND’],
‘참가자수’: [38, 38, 25, 17],
‘만족도’: [4.5, 4.6, 4.4, 4.5],
‘추천률’: [95.0, 97.4, 100.0, 88.2],
‘R&D’: [45, 25, 24, 29],
‘사업전략’: [35, 50, 52, 24],
‘제조기술’: [20, 25, 24, 18]
})
return session_data

session_data = load_data()

# 탭 생성 (인포그래픽 아이콘 포함)

tab1, tab2, tab3, tab4 = st.tabs([
“🔷 종합 개요”,
“🔶 참가자 구성 변화”,
“🔘 피드백 분석”,
“🔺 전략적 인사이트”
])

with tab1:
st.markdown(’<div style="display: flex; align-items: center; margin-bottom: 2rem;"><div class="icon-overview"></div><span style="font-size: 1.5rem; font-weight: 600; color: #ffffff;">종합 개요</span></div>’, unsafe_allow_html=True)

```
# KPI 카드들 (ROI 관련 내용 제거)
col1, col2, col3 = st.columns(3)

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

# 차트들
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div style="display: flex; align-items: center; margin-bottom: 1rem;"><div class="icon-chart-line"></div><span style="font-size: 1.2rem; font-weight: 600; color: #ffffff;">회차별 만족도 추이</span></div>', unsafe_allow_html=True)
    
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
        height=400
    )
    
    fig_satisfaction.update_xaxes(gridcolor='rgba(255,255,255,0.1)')
    fig_satisfaction.update_yaxes(gridcolor='rgba(255,255,255,0.1)')
    
    st.plotly_chart(fig_satisfaction, use_container_width=True)

with col2:
    st.markdown('<div style="display: flex; align-items: center; margin-bottom: 1rem;"><div class="icon-chart-line"></div><span style="font-size: 1.2rem; font-weight: 600; color: #ffffff;">회차별 추천률 변화</span></div>', unsafe_allow_html=True)
    
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
        height=400
    )
    
    fig_recommendation.update_xaxes(gridcolor='rgba(255,255,255,0.1)')
    fig_recommendation.update_yaxes(gridcolor='rgba(255,255,255,0.1)')
    
    st.plotly_chart(fig_recommendation, use_container_width=True)

# 주요 성과 요약
st.markdown('<div style="display: flex; align-items: center; margin: 2rem 0 1rem 0;"><div class="icon-target"></div><span style="font-size: 1.5rem; font-weight: 600; color: #ffffff;">주요 성과 요약</span></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="insight-card">
        <div class="insight-title"><div class="icon-target"></div>교육 효과성</div>
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
        <div class="insight-title"><div class="icon-users"></div>참가자 특성</div>
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
        <div class="insight-title"><div class="icon-loop"></div>기술 트렌드 제공</div>
        <ul>
            <li>광통신 → 유리기판 → AI메모리 → NAND</li>
            <li>신기술에서 응용기술로 진화</li>
            <li>시장분석과 기술설명 균형 유지</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
```

with tab2:
st.markdown(’<div style="display: flex; align-items: center; margin-bottom: 2rem;"><div class="icon-composition"></div><span style="font-size: 1.5rem; font-weight: 600; color: #ffffff;">참가자 구성 변화</span></div>’, unsafe_allow_html=True)

```
# 회차별 참가자 구성 변화
st.markdown('<div style="display: flex; align-items: center; margin: 2rem 0 1rem 0;"><div class="icon-chart-line"></div><span style="font-size: 1.3rem; font-weight: 600; color: #ffffff;">회차별 참가자 구성 변화</span></div>', unsafe_allow_html=True)

# 세션별 구성 표시
col1, col2, col3, col4 = st.columns(4)

sessions_info = [
    ("1회차 (4.18)", "Optical Interconnection", [45, 35, 20], ["R&D", "사업전략", "제조/기술"]),
    ("2회차 (6.25)", "Glass Substrate", [25, 50, 25], ["R&D", "사업전략", "제조/기술"]),
    ("3회차 (7.30)", "AI Chip 메모리 시스템", [24, 52, 24], ["R&D", "사업전략", "제조/기술"]),
    ("4회차 (9.2-3)", "AI X 차세대 NAND", [29, 24, 18], ["R&D", "사업전략", "제조/기술"])
]

colors_dept = ['linear-gradient(90deg, #a855f7, #ec4899)', 'linear-gradient(90deg, #06b6d4, #0ea5e9)', 'linear-gradient(90deg, #10b981, #059669)']

for i, (col, (title, topic, values, labels)) in enumerate(zip([col1, col2, col3, col4], sessions_info)):
    with col:
        st.markdown(f"""
        <div class="session-composition">
            <div class="session-title">{title}</div>
            <div class="session-topic">{topic}</div>
        """, unsafe_allow_html=True)
        
        for j, (label, value) in enumerate(zip(labels, values)):
            st.markdown(f"""
            <div class="dept-bar">
                <div class="dept-name">{label}</div>
                <div class="dept-progress">
                    <div class="dept-fill" style="width: {value}%; background: {colors_dept[j]};"></div>
                </div>
                <div class="dept-percent">{value}%</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div style="display: flex; align-items: center; margin: 2rem 0 1rem 0;"><div class="icon-chart-line"></div><span style="font-size: 1.2rem; font-weight: 600; color: #ffffff;">직군별 참여 추이</span></div>', unsafe_allow_html=True)
    
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
        height=400
    )
    
    fig_dept.update_xaxes(gridcolor='rgba(255,255,255,0.1)')
    fig_dept.update_yaxes(gridcolor='rgba(255,255,255,0.1)')
    
    st.plotly_chart(fig_dept, use_container_width=True)

with col2:
    st.markdown('<div style="display: flex; align-items: center; margin: 2rem 0 1rem 0;"><div class="icon-target"></div><span style="font-size: 1.2rem; font-weight: 600; color: #ffffff;">경력별 참여 분포</span></div>', unsafe_allow_html=True)
    
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
        height=400
    )
    
    st.plotly_chart(fig_exp, use_container_width=True)
```

with tab3:
st.markdown(’<div style="display: flex; align-items: center; margin-bottom: 2rem;"><div class="icon-feedback"></div><span style="font-size: 1.5rem; font-weight: 600; color: #ffffff;">피드백 분석</span></div>’, unsafe_allow_html=True)

```
# 감정 분석 대시보드
st.markdown('<div style="display: flex; align-items: center; margin: 2rem 0 1rem 0;"><div class="icon-lightbulb"></div><span style="font-size: 1.3rem; font-weight: 600; color: #ffffff;">감정 분석 대시보드</span></div>', unsafe_allow_html=True)

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

# 키워드 분석
st.markdown('<div style="display: flex; align-items: center; margin: 2rem 0 1rem 0;"><div class="icon-lightbulb"></div><span style="font-size: 1.3rem; font-weight: 600; color: #ffffff;">주요 피드백 키워드 분석</span></div>', unsafe_allow_html=True)

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

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div style="display: flex; align-items: center; margin: 2rem 0 1rem 0;"><div class="icon-chart-line"></div><span style="font-size: 1.2rem; font-weight: 600; color: #ffffff;">회차별 감정 분석</span></div>', unsafe_allow_html=True)
    
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
        height=400
    )
    
    fig_sentiment.update_xaxes(gridcolor='rgba(255,255,255,0.1)')
    fig_sentiment.update_yaxes(gridcolor='rgba(255,255,255,0.1)')
    
    st.plotly_chart(fig_sentiment, use_container_width=True)

with col2:
    st.markdown('<div style="display: flex; align-items: center; margin: 2rem 0 1rem 0;"><div class="icon-target"></div><span style="font-size: 1.2rem; font-weight: 600; color: #ffffff;">주요 요청 사항 분포</span></div>', unsafe_allow_html=True)
    
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
        height=400
    )
    
    st.plotly_chart(fig_request, use_container_width=True)

# 피드백 인사이트
st.markdown('<div style="display: flex; align-items: center; margin: 2rem 0 1rem 0;"><div class="icon-lightbulb"></div><span style="font-size: 1.3rem; font-weight: 600; color: #ffffff;">피드백 인사이트</span></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="insight-card">
        <div class="insight-title"><div class="icon-target"></div>가장 많이 요청된 주제</div>
        <ul>
            <li>양자컴퓨팅 관련 기술 (12건)</li>
            <li>AI 데이터센터 및 발열 해결 (8건)</li>
            <li>차세대 메모리 기술 (7건)</li>
            <li>반도체 미래 전망 (6건)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="insight-card">
        <div class="insight-title"><div class="icon-gear"></div>주요 개선 포인트</div>
        <ul>
            <li>질의응답 시간 확대 (5건)</li>
            <li>지역별 접근성 개선 (3건)</li>
            <li>화면 표시 개선 (3건)</li>
            <li>강의자료 사전 배포 (2건)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="insight-card">
        <div class="insight-title"><div class="icon-lightbulb"></div>만족 요인</div>
        <ul>
            <li>전문가 구성의 우수성</li>
            <li>최신 기술 트렌드 제공</li>
            <li>이해하기 쉬운 설명</li>
            <li>기술 인사이트 향상에 도움</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
```

with tab4:
st.markdown(’<div style="display: flex; align-items: center; margin-bottom: 2rem;"><div class="icon-insights"></div><span style="font-size: 1.5rem; font-weight: 600; color: #ffffff;">전략적 인사이트</span></div>’, unsafe_allow_html=True)

```
# ROI 상세 분석 (4번째 탭으로 이동)
st.markdown('<div style="display: flex; align-items: center; margin: 2rem 0 1rem 0;"><div class="icon-money"></div><span style="font-size: 1.3rem; font-weight: 600; color: #ffffff;">ROI 380% 상세 분석</span></div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("직접비용 비중", "40%", "강사료, 운영비")
with col2:
    st.metric("간접비용 비중", "60%", "참가자 시간, 기회비용")
with col3:
    st.metric("일반교육 ROI", "150%", "업계 평균")
with col4:
    st.metric("3년차 예상 ROI", "500%", "누적 효과")

# 교육 개요
st.markdown("""
<div class="education-overview">
    <div class="education-title"><div class="icon-book"></div>Next Chip Talk 교육 개요</div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="education-item">
        <h4><div class="icon-target"></div>교육 목적</h4>
        <p>급변하는 반도체 패러다임에 대응하기 위하여 근미래에 상용화될 가능성이 높은 반도체 기술을 조망하고, 
        최신 연구 동향과 기술적 난제에 대한 이해를 높여 기술 인사이트 향상을 목표로 함.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="education-item">
        <h4><div class="icon-book"></div>학습 방식</h4>
        <ul>
            <li>현장 참여 세미나</li>
            <li>온라인 생중계를 통한 실시간 웨비나</li>
            <li>추후 동영상 mySUNI 플랫폼에 녹화본 업로드</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="education-item">
        <h4><div class="icon-users"></div>수강 대상</h4>
        <p>반도체 관련 멤버사의 기술/개발 및 전략/마케팅 구성원, 반도체 신기술 및 신사업에 대한 
        기술 동향 지식이 필요한 구성원 (기본적인 반도체 공정 기술에 대한 이해 필요)</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="education-item">
        <h4><div class="icon-chart-line"></div>학습 구성</h4>
        <ul>
            <li>모더레이터의 주제 키노트</li>
            <li>전문가 강연 (학계 + 산업계)</li>
            <li>대담과 질의 응답</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# HRD 기반 교육 전략
st.markdown('<div style="display: flex; align-items: center; margin: 2rem 0 1rem 0;"><div class="icon-rocket"></div><span style="font-size: 1.3rem; font-weight: 600; color: #ffffff;">HRD 기반 교육 전략</span></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="insight-card">
        <div class="insight-title"><div class="icon-growth"></div>참가자 확보 전략</div>
        <ul>
            <li>타겟 직군별 맞춤 마케팅</li>
            <li>시즌별 참여도 분석 반영</li>
            <li>정기적 고객 조사 실시</li>
            <li>다양한 기업문화 고려</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insight-card">
        <div class="insight-title"><div class="icon-loop"></div>지속가능성 확보</div>
        <ul>
            <li>기술 전문가 네트워킹 플랫폼</li>
            <li>분기별 기술 동향 레포트</li>
            <li>mySUNI 커뮤니티 스터디</li>
            <li>글로벌 반도체 교육 허브</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="insight-card">
        <div class="insight-title"><div class="icon-target"></div>기술 인사이트 강화</div>
        <ul>
            <li>양자컴퓨팅 전문 세션 신설</li>
            <li>AI 데이터센터 심화 과정</li>
            <li>차세대 메모리 기술 시리즈</li>
            <li>기술 트렌드 감각 향상</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insight-card">
        <div class="insight-title"><div class="icon-gear"></div>운영 혁신</div>
        <ul>
            <li>실시간 Q&A 화면 표시</li>
            <li>지역별 접근성 개선</li>
            <li>강의자료 사전/사후 제공</li>
            <li>질의응답 시간 30% 확대</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="insight-card">
        <div class="insight-title"><div class="icon-money"></div>ROI 평가 체계</div>
        <ul>
            <li>Kirkpatrick-Phillips 5단계 모델</li>
            <li>직접/간접 비용 측정</li>
            <li>교육 전후 성과 추적</li>
            <li>3년 단위 평가 계획</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Kirkpatrick 평가 모델
st.markdown('<div style="display: flex; align-items: center; margin: 2rem 0 1rem 0;"><div class="icon-chart-line"></div><span style="font-size: 1.3rem; font-weight: 600; color: #ffffff;">Kirkpatrick-Phillips 5단계 평가 및 목표</span></div>', unsafe_allow_html=True)

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
    height=500
)

st.plotly_chart(fig_kirkpatrick, use_container_width=True)

# HRD 평가 모델 설명
st.markdown("""
<div class="hrd-analysis">
    <h4><div class="icon-target"></div>HRD 평가 모델 기반 교육 효과성 분석</h4>
    <div class="hrd-grid">
        <div class="hrd-item">
            <h5>Level 1-2: 반응 및 학습</h5>
            <p>참가자 만족도 4.5/5점, 추천률 95.1%로 교육에 대한 즉각적 반응이 매우 긍정적. 
            기술 이해도 향상과 새로운 지식 습득이 효과적으로 이루어짐.</p>
        </div>
        <div class="hrd-item">
            <h5>Level 3: 행동 변화 (인사이트)</h5>
            <p>참가자들의 기술 트렌드 감각 향상과 업무 접근 방식 개선이 관찰됨. 
            후속 연구 및 프로젝트 기획에 교육 내용이 반영되는 사례 증가.</p>
        </div>
        <div class="hrd-item">
            <h5>Level 4-5: 결과 및 ROI</h5>
            <p>기술 인사이트 향상을 통한 혁신 프로젝트 발굴과 의사결정 품질 개선. 
            교육 투자 대비 조직 성과 창출 효과가 지속적으로 증가하는 추세.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
```

# 푸터

st.markdown(”—”)
st.markdown(f”””

<div style="text-align: center; color: #9ca3af; font-size: 0.9rem; padding: 1rem; position: relative; z-index: 2;">
    <div class="icon-chart-line"></div> Next Chip Talk 교육 성과 분석 대시보드 | 
    <div class="icon-lightbulb"></div> 마지막 업데이트: {datetime.now().strftime('%Y-%m-%d %H:%M')} | 
    <div class="icon-target"></div> HRD 이론 기반 분석
</div>
""", unsafe_allow_html=True)
