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

	st.markdown('<center><p class="big-font"><font color="darkblue">Bài 7: Datetime</center></p>', unsafe_allow_html=True)

	st.write("## Hãy nhập thời gian hiện tại vào robot")

	st.image(Image.open('./picture/robot.png'), width=250)

	st.write("## Ngày: ")

	day = st.slider(" ", 1, 31, 1)

	st.write("## Tháng: ")

	month = st.selectbox(" ", options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

	st.write("## Năm: ")
	
	year = st.radio(" ", options=[2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025], horizontal=True)

	st.write(" ")

	def convert(month):
		if month == 1:
			return "Jan"
		elif month == 2:
			return "Feb"
		elif month == 3:
			return "Mar"
		elif month == 4:
			return "Apr"
		elif month == 5:
			return "May"
		elif month == 6:
			return "Jun"
		elif month == 7:
			return "July"
		elif month == 8:
			return "Aug"
		elif month == 9:
			return "Sep"
		elif month == 10:
			return "Oct"
		elif month == 11:
			return "Nov"
		else:
			return "Dec"

	def convert_day(day):
		if day == 0:
			return "Thứ hai"
		if day == 1:
			return "Thứ ba"
		if day == 2:
			return "Thứ tư"
		if day == 3:
			return "Thứ năm"
		if day == 4:
			return "Thứ sáu"
		if day == 5:
			return "Thứ bảy"
		if day == 6:
			return "Chủ nhật"
       


	if st.button("Nhập thông tin: "):

		ti = time.asctime(time.localtime(time.time()))
		spl_ti = ti.split(" ")
		currentdate = datetime.now().timetuple()
		days = calendar.weekday(currentdate[0], currentdate[1], currentdate[2])


		if day==int(spl_ti[2]) and convert(month)==spl_ti[1] and year==int(spl_ti[4]):
			st.write("Cảm ơn bạn đã nhập thông tin chính xác :smile:")
			st.write("Thời gian hiện tại là: %s, ngày %s tháng %s năm %s" % (convert_day(days), currentdate[2], currentdate[1], currentdate[0]))
		else:
			st.write("Thông tin của bạn đã sai :cry: vì:")
			st.write("Thời gian hiện tại không phải: %s, ngày %s tháng %s năm %s" % (convert_day(calendar.weekday(year, month, day)), day, month, year))
