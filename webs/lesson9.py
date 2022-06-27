import streamlit as st
from PIL import Image
import random
import pandas as pd

@st.cache
def return_list(lst, lst2):
	lst.append(lst2)
	return lst

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

	st.markdown('<center><p class="big-font"><font color="darkblue">Bài 9: Tuple</center></p>', unsafe_allow_html=True)

	st.write("## Hãy giúp bạn đưa vật có kỉ niệm vào hộp thời gian")



	st.image(Image.open('./picture/timecapsule.jpg'), width=500)

	def convert(stuff):
		if stuff == "Dây chuyền":
			return Image.open('./picture/neckl.jpg')
		elif stuff == "Nhẫn":
			return Image.open('./picture/ring.jpg')
		elif stuff == "Sách vở":
			return Image.open('./picture/book.jpg')
		elif stuff == "Hình ảnh":
			return Image.open('./picture/picture.jpg')
		elif stuff == "Áo quần":
			return Image.open('./picture/cloth.jpg')
		elif stuff == "Búp bê":
			return Image.open('./picture/doll.jpg') 
		elif stuff == "Kỷ yếu":
			return Image.open('./picture/kyyeu.jpg')

	def try_pass(stf):		
			try:
				st.image(convert(stf), width = 100)
			except:
				return " "

	lst = ["Dây chuyền", "Nhẫn", "Sách vở",  "Hình ảnh", "Áo quần", "Búp bê", "Kỷ yếu"]
	st1= []
	
	# if 'stuff1' not in st.session_state:
	# 	st.session_state['stuff1'] = st1
	st.write("### Hãy để đồ vào hộp thời gian")

	stuff = st.multiselect("chọn món đồ", options= lst)

	# if stuff:
	# 	st.session_state.stuff1 = st1.append(stuff)
		
		
	agree = st.checkbox('Hãy check vào ô nếu bạn muốn đóng hộp')

	if agree:
		# st1.append(stuff)
		# st.write(return_list(st1, stuff))
		df1 = pd.read_csv('output.csv')
		col_one_list = df1['Name'].tolist()
		#st.write(col_one_list)
		col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

		with col1:
			try:
				st.image(convert(col_one_list[0]), width = 100)
			except:
				pass
		with col2:
			try:
				st.image(convert(col_one_list[1]), width = 100)
			except:
				pass
		with col3:
			try:
				st.image(convert(col_one_list[2]), width = 100)
			except:
				pass
		with col4:
			try:
				st.image(convert(col_one_list[3]), width = 100)
			except:
				pass
		with col5:
			try:
				st.image(convert(col_one_list[4]), width = 100)
			except:
				pass
		with col6:
			try:
				st.image(convert(col_one_list[5]), width = 100)
			except:
				pass
		with col7:
			try:
				st.image(convert(col_one_list[6]), width = 100)
			except:
				pass

	else:
		data = {'Name': stuff}
		df = pd.DataFrame(data)
		df.to_csv('output.csv', index = False)
		#st.write(stuff)
		col8, col9, col10, col11, col12, col13, col14 = st.columns(7)

		with col8:
			try:
				st.image(convert(stuff[0]), width = 100)
			except:
				pass
		with col9:
			try:
				st.image(convert(stuff[1]), width = 100)
			except:
				pass
		with col10:
			try:
				st.image(convert(stuff[2]), width = 100)
			except:
				pass
		with col11:
			try:
				st.image(convert(stuff[3]), width = 100)
			except:
				pass
		with col12:
			try:
				st.image(convert(stuff[4]), width = 100)
			except:
				pass
		with col13:
			try:
				st.image(convert(stuff[5]), width = 100)
			except:
				pass
		with col14:
			try:
				st.image(convert(stuff[6]), width = 100)
			except:
				pass

	
	# st.write("### Bước 2. Tiến hành đóng hộp")

	# clo = st.radio("Bạn có muốn chỉnh sửa đồ trong hộp không ?", options=["có", "không"])

	# if clo == "không":

	# 	col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

	# 	with col1:
	# 		try:
	# 			st.image(convert(stuff[0]), width = 100)
	# 		except:
	# 			pass
	# 	with col2:
	# 		try:
	# 			st.image(convert(stuff[1]), width = 100)
	# 		except:
	# 			pass
	# 	with col3:
	# 		try:
	# 			st.image(convert(stuff[2]), width = 100)
	# 		except:
	# 			pass
	# 	with col4:
	# 		try:
	# 			st.image(convert(stuff[3]), width = 100)
	# 		except:
	# 			pass
	# 	with col5:
	# 		try:
	# 			st.image(convert(stuff[4]), width = 100)
	# 		except:
	# 			pass
	# 	with col6:
	# 		try:
	# 			st.image(convert(stuff[5]), width = 100)
	# 		except:
	# 			pass
	# 	with col7:
	# 		try:
	# 			st.image(convert(stuff[6]), width = 100)
	# 		except:
	# 			pass


	# else:
	# 	col8, col9, col10, col11, col12, col13, col14 = st.columns(7)

	# 	with col8:
	# 		try:
	# 			st.image(convert(stuff[0]), width = 100)
	# 		except:
	# 			pass
	# 	with col9:
	# 		try:
	# 			st.image(convert(stuff[1]), width = 100)
	# 		except:
	# 			pass
	# 	with col10:
	# 		try:
	# 			st.image(convert(stuff[2]), width = 100)
	# 		except:
	# 			pass
	# 	with col11:
	# 		try:
	# 			st.image(convert(stuff[3]), width = 100)
	# 		except:
	# 			pass
	# 	with col12:
	# 		try:
	# 			st.image(convert(stuff[4]), width = 100)
	# 		except:
	# 			pass
	# 	with col13:
	# 		try:
	# 			st.image(convert(stuff[5]), width = 100)
	# 		except:
	# 			pass
	# 	with col14:
	# 		try:
	# 			st.image(convert(stuff[6]), width = 100)
	# 		except:
	# 			pass

	# 	stuff1 = st.multiselect("chọn món đồ", options= stuff)



	# 	if st.button("Xác nhận xóa"):
	# 		st.write("Bạn không thể xóa món đồ trong hộp bạn hãy quay lại bước 1 nha")
