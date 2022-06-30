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

	st.markdown('<center><p class="big-font"><font color="darkblue">Bài 5: String</center></p>', unsafe_allow_html=True)

	st.image(Image.open('./picture/talk.jpg'), width=500)


	st.write('## Hãy tìm từ tiếng anh xuất hiện trong câu sau:')

	sen = st.write("Hôm qua, tôi chơi game cả ngày.")

	word = "hôm qua, tôi chơi video game cả ngày"

	# ran = st.slider("Nội dung nằm ở khoảng:", 0, len(word), (0, len(word)))

	st.markdown(
	""" <style>
			div[role="radiogroup"] >  :first-child{
				display: none !important;
			}
		</style>
		""",
	unsafe_allow_html=True
	)

	def convert(num):
		if num == 1:
			return "hôm"

		elif num == 2:
			return "qua"

		elif num == 3:
			return "tôi"


		elif num == 4:
			return "chơi"

		elif num == 6:
			return "cả"

		elif num == 7:
			return "ngày"

	posi = st.radio("Vị trí của từ tiếng anh:", options=["None", 1, 2, 3, 4, 5, 6, 7], horizontal=True)

	if posi == 5:
		st.write("Chúc mừng bạn đã có sự lựa chọn chính xác")

	elif posi == "None":
		pass

	else:
		st.write('Sai, từ " %s " không phải là từ tiếng anh' % (convert(posi)))

