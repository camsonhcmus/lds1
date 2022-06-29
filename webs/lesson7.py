import streamlit as st
from PIL import Image
import random
import time
from datetime import datetime
import calendar

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

	st.markdown('<center><p class="big-font"><font color="darkblue">Bài 6: Datetime</center></p>', unsafe_allow_html=True)

	st.write("## Hãy chọn ngày sinh nhật")

	st.image(Image.open('./picture/cake.jpg'), width=400)

	st.write("## Ngày: ")

	day = st.slider(" ", 1, 31, 1)

	st.write("## Tháng: ")

	month = st.selectbox(" ", options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

	tim = datetime.now().timetuple()
	a1 = str("%s/%s/%s"%(tim[1], tim[2], tim[0]))
	b1 = str("%s/%s/%s"%(month, day, tim[0]))
	date_format = "%m/%d/%Y"
	a = datetime.strptime(a1, date_format)
	b = datetime.strptime(b1, date_format)
	delta = b - a

	if st.button("Xác nhận"):
		if delta.days > 0:
			st.write("#### Còn %s ngày nữa là tới sinh nhật bạn"%(delta.days))
		elif delta.days == 0:
			st.write("#### Chúc mừng sinh nhật bạn")			
		elif delta.days < 0:
			st.write("#### Sinh nhật bạn đã qua %s ngày"%(delta.days * -1))
