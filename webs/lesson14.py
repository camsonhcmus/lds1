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

	st.markdown('<center><p class="big-font"><font color="darkblue">Bài 14: Xử lý ngoại lệ</center></p>', unsafe_allow_html=True)

	st.write("### Hãy hoàn thành câu sau với các lựa chọn bên dưới:")

	st.markdown('<center><span style="font-size: 40px"><strong><span class="css-10trblm e16nr0p30">Chúng ta đều bắt đầu học tiểu học ở lớp ...</span></span></center>', unsafe_allow_html=True)
		

	col1, col2, col3 = st.columns(3)

	with col1:
		st.image(Image.open('./picture/cow.jpg'), width=400)
		st.markdown('<div data-testid="caption" class="css-1b0udgb etr89bj0" style="width: 500px;"><span style="font-size: 20px"><center><strong> con bò </center></span></div>', unsafe_allow_html=True)

	with col2:
		st.image(Image.open('./picture/boat.jpg'), width=400)
		st.markdown('<div data-testid="caption" class="css-1b0udgb etr89bj0" style="width: 500px;"><span style="font-size: 20px"><center><strong> thuyền </center></span></div>', unsafe_allow_html=True)

	with col3:
		st.image(Image.open('./picture/chair.jpg'), width=350)
		st.markdown('<div data-testid="caption" class="css-1b0udgb etr89bj0" style="width: 400px;"><span style="font-size: 20px"><center><strong> ghế dựa </center></span></div>', unsafe_allow_html=True)

	col4, col5, col6 = st.columns(3)

	with col4:
		st.image(Image.open('./picture/tree.jpg'), width=400)
		st.markdown('<div data-testid="caption" class="css-1b0udgb etr89bj0" style="width: 500px;"><span style="font-size: 20px"><center><strong> cây </center></span></div>', unsafe_allow_html=True)

	with col5:
		st.image(Image.open('./picture/number1.jpg'), width=400)
		st.markdown('<div data-testid="caption" class="css-1b0udgb etr89bj0" style="width: 500px;"><span style="font-size: 20px"><center><strong> số 1 </center></span></div>', unsafe_allow_html=True)


	with col6:
	 	st.image(Image.open('./picture/student.jpg'), width=600)
	 	st.markdown('<div data-testid="caption" class="css-1b0udgb etr89bj0" style="width: 700px;"><span style="font-size: 20px"><center><strong> học sinh </center></span></div>', unsafe_allow_html=True)


	orig = st.radio("Hãy lựa chọn phương án phù hợp", options=["con bò", "thuyền", "ghế dựa", "cây", "1", "học sinh"])

	try:
		int(orig)
		st.write("## Chúc mừng :tada:")
	except:
		st.error("Hãy chọn lại phương án phù hợp bạn nhé :smile:")

