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

	st.markdown('<center><p class="big-font"><font color="darkblue">Bài 4: Cấu trúc lặp</center></p>', unsafe_allow_html=True)

	st.markdown("## Hiển thị bảng cửu chương")

	st.image(Image.open('./picture/multable.jpg'), width=500)

	inp = st.text_input("Bạn muốn hiển thị bảng cửu chương số mấy: ")

	if st.button("Kết quả"):
		try:
			for i in range (1, 10):
				inp = int(inp)
				result = inp * i
				print(type(inp))
				print("%s x %s = %s" % (inp, i, result))

				st.write("%s x %s = %s" % (inp, i, result))

		except:
			st.error("Hãy nhập số bạn nhé :smile:")


