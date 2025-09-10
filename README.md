# Next Chip Talk 교육 성과 분석 대시보드

2025 미래반도체 Next & Grey 영역 교육 성과를 분석하는 Streamlit 대시보드입니다.

## 실행 방법
```bash
streamlit run app.py
### 2단계: Streamlit Community Cloud 배포
1. [share.streamlit.io](https://share.streamlit.io) 접속
2. GitHub 계정으로 로그인
3. "New app" 클릭
4. 저장소 선택: `your-username/next-chip-talk-dashboard`
5. Main file path: `app.py`
6. "Deploy!" 클릭

배포되면 공개 URL이 생성되어 어디서든 접속할 수 있습니다.

---

## 방법 2: GitHub Codespaces

GitHub 저장소에서 바로 실행하려면:

1. GitHub 저장소 페이지에서 "Code" > "Codespaces" > "Create codespace" 클릭
2. 터미널에서:
```bash
pip install -r requirements.txt
streamlit run app.py --server.port 8000
