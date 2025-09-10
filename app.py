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
    
    .insight-card {
        background: rgba(168, 85, 247,
