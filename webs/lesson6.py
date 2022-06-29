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

	st.write('## Hãy nhập một câu và lấy ra nội dung')

	st.image(Image.open('./picture/talk.jpg'), width=500)
	

	word = st.text_input("Hãy nhập câu rồi nhấn enter: ", value=" ")
	ran = st.slider("Khoảng nội dung mà bạn muốn lấy ra:", 0, len(word), (0, len(word)))
	#ran = st.slider("Nội dung nằm ở khoảng:", 0, len(word), (0, len(word)))


	if st.button("Hiện nội dung: "):


		word1 = word[ran[0]:ran[1]]

		st.write(word1)	
