import numpy as np
import pandas as pd
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

	st.markdown('<center><p class="big-font"><font color="darkblue">Bài 1: Biến và các kiểu dữ liệu cơ sở</center></p>', unsafe_allow_html=True)

	st.image(Image.open('./picture/intro.jpg'), width=500)

	name = st.text_input("Họ và tên: ")
	age = st.slider("Tuổi", 10, 20, 1)
	school = st.text_input("Hãy nhập tên trường: ")
	#location = st.selectbox("Hiện em đang số ở", options=["Thành phố HCM", "Tỉnh khác"]
	location = st.selectbox("Nơi sinh sống", options=["Thành phố Thủ Đức", 
	"Quận Bình Tân" , 
	"Quận 1", 
	"Quận Bình Thạnh", 
	"Quận 3", 
	"Quận Gò Vấp", 
	"Quận 4", 
	"Quận Phú Nhuận", 
	"Quận 5", 
	"Quận Tân Bình", 
	"Quận 6", 
	"Quận Tân Phú", 
	"Quận 7", 
	"Huyện Bình Chánh", 
	"Quận 8", 
	"Huyện Cần Giờ", 
	"Quận 10", 
	"Huyện Củ Chi", 
	"Quận 11", 
	"Huyện Hóc Môn", 
	"Quận 12", 
	"Huyện Nhà Bè", 
	"Tỉnh thành khác"])
	hob = st.multiselect("Sở thích", options=["Đọc sách", "Chơi game", "Ăn uống",  "Thể thao", "Đi dạo phố", "Đi shopping", "Đi chơi với bạn", "Khác"])
	if st.button("Hoàn thành"):
		st.write("Em tên là %s, %s tuổi, đang học trường %s , sống ở %s và em có sở thích %s. Hiện em đang tham gia lớp LDS1 và rất vui được găp các bạn." % (name, age, school, location, ', '.join(map(str, hob))))




	
