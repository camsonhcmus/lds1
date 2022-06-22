import streamlit as st
from PIL import Image

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

	st.markdown('<center><p class="big-font"><font color="darkblue">Bài 5: Number</center></p>', unsafe_allow_html=True)

	st.markdown("## Hãy hoàn thành bài toán: a + b + c = 100")

	st.image(Image.open('./picture/phepcong.jpg'), width=500)

	a = st.text_input('Hãy nhập số cho "a": ')
	b = st.text_input('Hãy nhập số cho "b": ')
	c = st.text_input('Hãy nhập số cho "c": ')


	
	if st.button("Hiện kết quả"):
		try:
			a = float(a)
			b = float(b)
			c = float(c)
		except:
			st.error("Hãy nhập số bạn nhé :smile:")

		result = a + b + c

		if result == 100:
			st.write("Chúc mừng bạn:tada:")
		else:
			st.write("Bạn sai rồi , hãy làm lại nhé:cry:")