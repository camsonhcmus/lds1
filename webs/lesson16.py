import streamlit as st
from PIL import Image
import random
import pandas as pd

def app():
	image = Image.open('./picture/khtn.PNG')
	st.image(image, width=500)

	st.markdown("------")

	st.markdown("""
	<style>
	.big-font {
    	font-size:80px !important;
	}
	</style>
	""", unsafe_allow_html=True)

	st.markdown('<center><p class="big-font"><font color="darkblue">Bài 13: Dictionary (mở rộng)</center></p>', unsafe_allow_html=True)

	st.write("### Hãy giúp mình xắp xếp lịch học hè (1 ngày 5 môn ):")

	st.image(Image.open('./picture/schedule.jpg'), width=500)

	
	mon = st.multiselect("Thứ hai", ("Toán", "Văn", "Sử", "Địa", "Sinh", "Anh", "Vật Lý", "Hóa", "Toán", "Văn", "Sử", "Địa", "Sinh", "Anh", "Vật Lý", "Hóa"))
	tue = st.multiselect("Thứ ba", ("Toán", "Văn", "Sử", "Địa", "Sinh", "Anh", "Vật Lý", "Hóa", "Toán", "Văn", "Sử", "Địa", "Sinh", "Anh", "Vật Lý", "Hóa"))
	wed = st.multiselect("Thứ tư", ("Toán", "Văn", "Sử", "Địa", "Sinh", "Anh", "Vật Lý", "Hóa", "Toán", "Văn", "Sử", "Địa", "Sinh", "Anh", "Vật Lý", "Hóa"))
	thu = st.multiselect("Thứ năm", ("Toán", "Văn", "Sử", "Địa", "Sinh", "Anh", "Vật Lý", "Hóa", "Toán", "Văn", "Sử", "Địa", "Sinh", "Anh", "Vật Lý", "Hóa"))
	fri = st.multiselect("Thứ sáu", ("Toán", "Văn", "Sử", "Địa", "Sinh", "Anh", "Vật Lý", "Hóa", "Toán", "Văn", "Sử", "Địa", "Sinh", "Anh", "Vật Lý", "Hóa"))

	
	
	if st.button("Hiện thời khóa biểu: "):
		# try:
		if len(mon) == 5 and len(tue) == 5 and len(wed) == 5 and len(thu) == 5 and len(fri) == 5:
			sch = {'Thứ hai': mon, 'Thứ ba': tue, 'Thứ tư': wed, 'Thứ năm': thu, 'Thứ sáu': fri}
			df = pd.DataFrame(data=sch, index=["Tiết 1", "Tiết 2", "Tiết 3", "Tiết 4", "Tiết 5"])
			st.dataframe(data=df)
		else:
			st.error("#### Chọn đủ 5 môn bạn nhé :smile:")
		# except:
		# 	st.error("#### Chọn đủ 5 môn bạn nhé :smile:")
		#else:
		#	st.write("#### Chọn đủ 5 môn bạn nhé :smile:")

		
