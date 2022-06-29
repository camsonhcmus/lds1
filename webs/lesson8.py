import streamlit as st
from PIL import Image
import random
import itertools

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

	st.markdown('<center><p class="big-font"><font color="darkblue">Bài 9: List</center></p>', unsafe_allow_html=True)

	st.write("## Hãy tạo menu cho nhà hàng")

	st.image(Image.open('./picture/cheffthink.jpg'), width=500)

	appetizer = st.multiselect("Menu khai vị", options=["Gỏi ngó sen tôm thịt", "Gỏi bò mè bóp thấu", "Càng cua bách hoa",  "Gỏi miến trộn tôm thịt"])
	main_course = st.multiselect("Menu món chính", options=["Cá tai tượng chiên xù", "Gà bó xôi", "Mực xào sa tế",  "Cá lóc hấp bầu", "Lẩu bò", "Cơm chiên dương châu"])
	dessert = st.multiselect("Menu tráng miệng", options=["Các loại trái cây", "Rau câu", "Chè đậu xanh"])

	menu_b = st.radio("Cách thể hiện menu", options=["Chia nhỏ 3 menu", "Tạo thành 1 menu"])

	full_menu=list(itertools.chain(appetizer, main_course, dessert))

	#menu_delete = st.multiselect("Hãy chọn món để xóa", options=full_menu)

	def convert(dish):
		if dish == "Gỏi ngó sen tôm thịt":
			return Image.open('./picture/sen_tom.png')
		elif dish == "Gỏi bò mè bóp thấu":
			return Image.open('./picture/goi_bo.jpg')
		elif dish == "Càng cua bách hoa":
			return Image.open('./picture/cang_cua.png')
		elif dish == "Gỏi miến trộn tôm thịt":
			return Image.open('./picture/goi_mien.jpg')
		elif dish == "Cá tai tượng chiên xù":
			return Image.open('./picture/ca_tai.jpg')
		elif dish == "Gà bó xôi":
			return Image.open('./picture/ga_xoi.jpg')
		elif dish == "Mực xào sa tế":
			return Image.open('./picture/sa_te_muc.jpg')
		elif dish == "Cá lóc hấp bầu":
			return Image.open('./picture/ca_loc_bau.jpg')
		elif dish == "Lẩu bò":
			return Image.open('./picture/lau_bo.jpg')
		elif dish == "Cơm chiên dương châu":
			return Image.open('./picture/com_chien.jpg')
		elif dish == "Các loại trái cây":
			return Image.open('./picture/trai_cay.jpg')
		elif dish == "Rau câu":
			return Image.open('./picture/rau_cau.jpg')
		elif dish == "Chè đậu xanh":
			return Image.open('./picture/dau_xanh.jpg')

	appetizer_set = set(appetizer)
	main_course_set = set(main_course)
	dessert_set = set(dessert)

# 	for i in menu_delete:
# 		if i in appetizer_set:
# 			item1 = appetizer.remove(i)
# 		if i in main_course_set:
# 			item2 = main_course.remove(i)
# 		if i in dessert_set:
# 			item3 = dessert.remove(i)

	if menu_b == "Chia 3 menu nhỏ":
		col1, col2, col3 = st.columns(3)
		with col1:
			st.write("##### menu khai vị")
			for a in appetizer:
				st.image(convert(a), width=200)
				st.write(a)
		with col2:
			st.write("##### menu món chính")
			for m in main_course:
				st.image(convert(m), width=200)
				st.write(m)
		with col3:
			st.write("##### menu tráng miệng")
			for d in dessert:
				st.image(convert(d), width=200)
				st.write(d)
	else:
		st.write("#### Menu món ăn")
		st.write(" ")
		st.write(" ")
		st.write("##### menu khai vị")
		for a in appetizer:
			st.image(convert(a), width=200)
			st.write(a)
			print(a)
			print(type(a))
		st.write(" ")
		st.write(" ")
		st.write("##### menu món chính")
		for m in main_course:
			st.image(convert(m), width=200)
			st.write(m)
			print(m)
		st.write(" ")
		st.write(" ")
		st.write("##### menu tráng miệng")
		for d in dessert:
			st.image(convert(d), width=200)
			st.write(d)
			print(d)



