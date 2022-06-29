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

	st.markdown('<center><p class="big-font"><font color="darkblue">Bài 10: Random</center></p>', unsafe_allow_html=True)

	st.markdown('### Hãy phối đồ dựa trên tủ áo đang có')

	st.markdown('### Đây sẽ là tủ áo')

	col1, col2, col3, col4 = st.columns(4)

	with col1:
		st.image(Image.open('./picture/c1.PNG'), width=250)

	with col2:
		st.image(Image.open('./picture/c2.PNG'), width=250)

	with col3:
		st.image(Image.open('./picture/c3.PNG'), width=250)

	with col4:
		st.image(Image.open('./picture/c5.PNG'), width=250)

	col5, col6, col7, col8 = st.columns(4)

	with col5:
		st.image(Image.open('./picture/p2.PNG'), width=200)

	with col6:
		st.image(Image.open('./picture/p3.PNG'), width=200)

	with col7:
		st.image(Image.open('./picture/p6.png'), width=200)

	with col8:
		st.image(Image.open('./picture/p5.PNG'), width=200)

	col9, col10, col11, col12 = st.columns(4)

	with col9:
		st.image(Image.open('./picture/air1.jpg'), width=250)

	with col10:
		st.image(Image.open('./picture/air2.jpg'), width=250)

	with col11:
		st.image(Image.open('./picture/air3.jpg'), width=250)

	with col12:
		st.image(Image.open('./picture/air4.jpg'), width=250)

	st.markdown(" ")
	st.markdown(" ")

	def convert(cloth):
		if cloth == 1:
			return Image.open('./picture/c1.PNG')
		elif cloth == 2:
			return Image.open('./picture/c2.PNG')
		elif cloth == 3:
			return Image.open('./picture/c3.PNG')
		elif cloth == 4:
			return Image.open('./picture/c5.PNG')
		elif cloth == 5:
			return Image.open('./picture/p2.PNG')
		elif cloth == 6:
			return Image.open('./picture/p3.PNG')
		elif cloth == 7:
			return Image.open('./picture/p6.png')
		elif cloth == 8:
			return Image.open('./picture/p5.PNG')
		elif cloth == 9:
			return Image.open('./picture/air1.jpg')
		elif cloth == 10:
			return Image.open('./picture/air2.jpg')
		elif cloth == 11:
			return Image.open('./picture/air3.jpg')
		elif cloth == 12:
			return Image.open('./picture/air4.jpg')

	if st.button("Phối đồ ngẫu nhiên"):
		a1 = random.randint(1,4)
		a2 = random.randint(5,8)
		a3 = random.randint(9,12)

		st.image(convert(a1), width=250)
		st.image(convert(a2), width=240)
		st.image(convert(a3), width=200)
