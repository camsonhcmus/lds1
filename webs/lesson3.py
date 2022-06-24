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

	st.markdown('<center><p class="big-font"><font color="darkblue">Bài 3: Cấu trúc điều kiện</center></p>', unsafe_allow_html=True)

	st.markdown("## Hãy đoán con số ngẫu nhiên may mắn từ 1 đến 5 trong vòng 3 lượt")

	st.image(Image.open('./picture/lucky.png'), width=500)

	pre_num = st.text_input("Hãy nhập con số dự đoán: ")

	if st.button("Dự đoán: "):
		try:
			pre_num = int(pre_num)

		except:
			st.error("Hãy nhập số bạn nhé :smile:")

		number_test = random.randint(1,6)

		if pre_num == number_test:
			st.write("Chính xác :tada:")
			st.balloons()
			
		elif pre_num <= number_test:
			st.write("Sai :cry: con số bạn nhỏ hơn con số may mắn")
			
		elif pre_num >= number_test:
			st.write("Sai :cry: con số bạn lớn hơn con số may mắn")

