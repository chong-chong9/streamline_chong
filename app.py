import streamlit as st
import pandas as pd
import numpy as np

# 데이터 준비 (예제 데이터프레임)
data = pd.DataFrame({
    "Region": ["Seoul", "Busan", "Incheon", "Daegu", "Gwangju"],
    "Latitude": [37.5665, 35.1796, 37.4563, 35.8714, 35.1601],
    "Longitude": [126.9780, 129.0756, 126.7052, 128.6014, 126.8514],
    "Students": [1000, 700, 400, 600, 500],
    "Gender": ["Male", "Female", "Female", "Male", "Male"]
})

st.title("교육 데이터 분석 및 지도 시각화")

# Sidebar
st.sidebar.header("필터 옵션")
selected_region = st.sidebar.multiselect("지역 선택", data["Region"].unique(), default=data["Region"].unique())
selected_gender = st.sidebar.multiselect("성별 선택", data["Gender"].unique(), default=data["Gender"].unique())

# 데이터 필터링
filtered_data = data[
    (data["Region"].isin(selected_region)) & 
    (data["Gender"].isin(selected_gender))
]

# 지도용 열 이름 소문자로 변환
filtered_data = filtered_data.rename(columns={"Latitude": "latitude", "Longitude": "longitude"})

# 그래프 섹션
st.subheader("학생 수 데이터 시각화")
st.bar_chart(filtered_data.set_index("Region")["Students"])

# 지도 섹션
st.subheader("지도에서 위치 표시")

try:
    st.map(filtered_data[["latitude", "longitude"]])
except KeyError as e:
    st.error("지도 데이터를 표시할 수 없습니다. 열 이름이 올바른지 확인하세요.")

# 배포 안내
st.write("이 페이지는 Streamlit으로 제작되었으며, Streamlit Cloud를 통해 배포되었습니다.")