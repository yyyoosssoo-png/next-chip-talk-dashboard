# -*- coding: utf-8 -*-
import streamlit as st
import codecs

# ----------------------------------------------------------------------
# Streamlit 페이지 설정
#
# layout="wide": 페이지를 넓은 레이아웃으로 설정하여 대시보드가 화면에 꽉 차게 표시됩니다.
# page_title: 브라우저 탭에 표시될 제목입니다.
# page_icon: 브라우저 탭에 표시될 아이콘입니다. (이모지 사용 가능)
# ----------------------------------------------------------------------
try:
    st.set_page_config(
        page_title="Next Chip Talk 교육 성과 분석 대시보드",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="collapsed" # 사이드바를 초기에 숨김
    )
except Exception as e:
    # st.set_page_config는 스크립트 실행 시 한 번만 호출해야 하므로 예외 처리
    pass

# ----------------------------------------------------------------------
# HTML 파일 불러오기
#
# 'codecs' 라이브러리를 사용하면 utf-8과 같은 다양한 인코딩을 안정적으로 처리할 수 있습니다.
# 특히 한글이 포함된 파일을 다룰 때 유용합니다.
# ----------------------------------------------------------------------
def load_html_file(file_path):
    """지정된 경로의 HTML 파일을 읽어 그 내용을 반환합니다."""
    try:
        with codecs.open(file_path, 'r', 'utf-8') as f:
            return f.read()
    except FileNotFoundError:
        st.error(f"'{file_path}' 파일을 찾을 수 없습니다. 'app.py'와 동일한 경로에 파일이 있는지 확인해주세요.")
        return None
    except Exception as e:
        st.error(f"파일을 읽는 중 오류가 발생했습니다: {e}")
        return None

# ----------------------------------------------------------------------
# 메인 애플리케이션 실행
# ----------------------------------------------------------------------
def main():
    """메인 함수: HTML을 불러와 Streamlit 화면에 렌더링합니다."""

    # 제목 추가 (선택 사항)
    st.markdown("<h1 style='text-align: center; color: #a855f7;'>Next Chip Talk 교육 성과 분석</h1>", unsafe_allow_html=True)
    st.markdown("---") # 구분선

    # HTML 파일 경로
    html_file_path = "nct-dashboard_ver6.HTML"
    
    # HTML 코드 불러오기
    html_code = load_html_file(html_file_path)

    # HTML 코드가 성공적으로 로드되었을 경우 화면에 표시
    if html_code:
        # st.components.v1.html을 사용하여 HTML 콘텐츠를 렌더링합니다.
        # height: 컴포넌트의 높이를 픽셀 단위로 지정합니다.
        # scrolling=True: 콘텐츠가 높이를 초과할 경우 스크롤바를 생성합니다.
        st.components.v1.html(html_code, height=900, scrolling=True)

# ----------------------------------------------------------------------
# 스크립트가 직접 실행될 때 main() 함수를 호출
# ----------------------------------------------------------------------
if __name__ == "__main__":
    main()
