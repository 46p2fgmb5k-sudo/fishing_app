import streamlit as st
import datetime

st.set_page_config(page_title="선상낚시 빈자리 조회", page_icon="🎣")

st.title("🎣 선상낚시 실시간 빈자리 조회")
st.caption("선상24, 더피싱 통합 빈자리 확인 시스템")

st.sidebar.header("🔍 검색 조건")
selected_date = st.sidebar.date_input("날짜 선택", datetime.date.today())
platform = st.sidebar.selectbox("플랫폼", ["전체", "선상24", "더피싱"])

st.subheader(f"📅 {selected_date} 빈자리 목록")
st.info("💡 등록하신 선박 및 플랫폼의 실시간 빈자리가 여기에 표시됩니다.")

with st.container():
    c1, c2, c3 = st.columns([2, 2, 1])
    c1.write("🚢 **[선상24] 피싱킹호**\n(오천항 / 주꾸미)")
    c2.write("🔥 **3명 예약 가능**\n선비: 100,000원")
    c3.link_button("예약하기", "https://sunsang24.com")
