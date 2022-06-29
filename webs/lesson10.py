import streamlit as st
from PIL import Image
import random

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

	st.markdown('<center><p class="big-font"><font color="darkblue">Bài 7: Set</center></p>', unsafe_allow_html=True)

	st.write("## Mình sẽ giúp bạn xắp xếp các màu bạn chọn theo thứ tự của cầu vòng")

	st.image(Image.open('./picture/rainbow.jpg'), width=800)

	lst1 = ["Màu đỏ", "Màu vàng","Màu cam",  "Màu xanh lá", "Màu xanh dương","Màu chàm","Màu tím"]

	color = st.multiselect("Màu sắc", options= lst1)

	def stuff2number(stuff):
		if stuff == "Màu đỏ":
			return 1
		elif stuff == "Màu cam":
			return 2
		elif stuff == "Màu vàng":
			return 3
		elif stuff == "Màu xanh lá":
			return 4
		elif stuff == "Màu xanh dương":
			return 5
		elif stuff == "Màu chàm":
			return 6
		elif stuff == "Màu tím":
			return 7

	def convert(stuff):
		if stuff == 1:
			return Image.open('./picture/red.jpg')
		elif stuff == 2:
			return Image.open('./picture/orange.jpg')
		elif stuff == 3:
			return Image.open('./picture/yellow.jpg')
		elif stuff == 4:
			return Image.open('./picture/green.jpg')
		elif stuff == 5:
			return Image.open('./picture/blue.jpg')
		elif stuff == 6:
			return Image.open('./picture/indigo.jpg') 
		elif stuff == 7:
			return Image.open('./picture/purple.png')


	con_thing = []

	for i in color:
		nu = stuff2number(i)
		con_thing.append(nu)

	sett = set(con_thing)

	col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)

	with col1:
		try:
			st.image(convert(con_thing[0]), width = 100)
		except:
			pass
	with col2:
		try:
			st.image(convert(con_thing[1]), width = 100)
		except:
			pass
	with col3:
		try:
			st.image(convert(con_thing[2]), width = 100)
		except:
			pass
	with col4:
		try:
			st.image(convert(con_thing[3]), width = 100)
		except:
			pass
	with col5:
		try:
			st.image(convert(con_thing[4]), width = 100)
		except:
			pass
	with col6:
		try:
			st.image(convert(con_thing[5]), width = 100)
		except:
			pass
	with col7:
		try:
			st.image(convert(con_thing[6]), width = 100)
		except:
			pass
	with col8:
		try:
			st.image(convert(con_thing[7]), width = 100)
		except:
			pass
	with col9:
		try:
			st.image(convert(con_thing[8]), width = 100)
		except:
			pass
	with col10:
		try:
			st.image(convert(con_thing[9]), width = 100)
		except:
			pass


	if st.button("Xắp xếp lại theo cầu vòng"):

		sett = set(con_thing)

		col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

		with col1:
			try:
				st.image(convert(list(sett)[0]), width = 100)
			except:
				pass
		with col2:
			try:
				st.image(convert(list(sett)[1]), width = 100)
			except:
				pass
		with col3:
			try:
				st.image(convert(list(sett)[2]), width = 100)
			except:
				pass
		with col4:
			try:
				st.image(convert(list(sett)[3]), width = 100)
			except:
				pass
		with col5:
			try:
				st.image(convert(list(sett)[4]), width = 100)
			except:
				pass
		with col6:
			try:
				st.image(convert(list(sett)[5]), width = 100)
			except:
				pass
		with col7:
			try:
				st.image(convert(list(sett)[6]), width = 100)
			except:
				pass
