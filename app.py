import streamlit as st
import datetime

# 페이지 설정
st.set_page_config(page_title="선상낚시 빈자리 조회", page_icon="🎣")

st.title("🎣 선상낚시 실시간 빈자리 조회")
st.caption("선상24, 더피싱 통합 빈자리 확인 시스템")

# 사이드바 검색 조건
st.sidebar.header("🔍 검색 조건")
selected_date = st.sidebar.date_input("날짜 선택", datetime.date.today())
platform = st.sidebar.selectbox("플랫폼", ["전체", "선상24", "더피싱"])

st.subheader(f"📅 {selected_date} 빈자리 목록")
st.info("💡 등록하신 선박 및 플랫폼의 실시간 빈자리가 여기에 표시됩니다.")

# 전체 선박 샘플 데이터 (필요에 따라 선박을 추가할 수 있습니다)
ship_data = [
    {
        "platform": "선상24",
        "name": "피싱킹호",
        "port": "오천항",
        "fish": "주꾸미",
        "seats": 3,
        "price": "100,000원",
        "link": "https://sunsang24.com"
    },
    {
        "platform": "선상24",
        "name": "바다호",
        "port": "대천항",
        "fish": "갑오징어",
        "seats": 5,
        "price": "110,000원",
        "link": "https://sunsang24.com"
    },
    {
        "platform": "더피싱",
        "name": "돌핀호",
        "port": "무창포항",
        "fish": "문어",
        "seats": 2,
        "price": "120,000원",
        "link": "https://thefishing.kr"
    },
    {
        "platform": "더피싱",
        "name": "스타피싱호",
        "port": "영흥도",
        "fish": "우럭",
        "seats": 4,
        "price": "90,000원",
        "link": "https://thefishing.kr"
    }
]

# 선택한 플랫폼에 따라 데이터 필터링
if platform != "전체":
    filtered_ships = [s for s in ship_data if s["platform"] == platform]
else:
    filtered_ships = ship_data

# 필터링된 결과 화면에 출력
if filtered_ships:
    for ship in filtered_ships:
        with st.container():
            c1, c2, c3 = st.columns([2, 2, 1])
            c1.write(f"🚢 **[{ship['platform']}] {ship['name']}**\n({ship['port']} / {ship['fish']})")
            c2.write(f"🔥 **{ship['seats']}명 예약 가능**\n선비: {ship['price']}")
            c3.link_button("예약하기", ship['link'])
        st.divider()
else:
    st.warning("해당 플랫폼 조건에 일치하는 선박이 없습니다.")

