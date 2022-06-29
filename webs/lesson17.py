import streamlit as st
from PIL import Image
import random
import pandas as pd

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

	st.markdown('<center><p class="big-font"><font color="darkblue">Bài 14: List (mở rộng)</center></p>', unsafe_allow_html=True)

	st.markdown("## Chào mừng bạn đến cuộc chơi đoán từ tiếng anh")

	st.image(Image.open('./picture/wof.jpg'), width=500)

	st.write("""### Hãy đọc kỹ câu gợi ý:

		- Đây là 1 lục địa
		
	- Có tổng cộng 10 kí tự

	- Quanh năm cả châu lục đều phủ lớp băng

	- Là nơi có những trạm nghiên cứu khoa học các nước

	- Là nơi sinh sống của chim cánh cụt
		""")
	st.write("### Hãy xấp xếp thành từ trả lời:")
	letter1 = st.multiselect(" ", ("A", "i", "a", "t", "a", "c", "n", "r", "c", "t"))

	if st.button("Hiện đáp án: "):
		if len(letter1) == 10:
			letter1 = [''.join(letter1)]
			if letter1[0] == "Antarctica":
				st.write("### Chính Xác :tada:")
				st.image(Image.open('./picture/antarctica.jpg'), width=500)
				st.write("### Chính là Nam cực (Antarctica)")
			else:
				st.write("### Sai rồi hãy thử thêm nữa nha bạn :cry:")

		else:
			st.error("#### Chọn đủ số từ bạn nhé :smile:")
