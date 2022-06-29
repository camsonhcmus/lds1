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

	st.markdown('<center><p class="big-font"><font color="darkblue">Bài 15: List (mở rộng)</center></p>', unsafe_allow_html=True)

	st.markdown("## Hãy xắp xếp hình theo hình mẫu")
	st.image(Image.open('./picture/van.jpg'), width=800)
	
	st.write("### Hình cần xắp xếp: ")
	col1, col2, col3, col4 = st.columns(4)

	# left = 5
	# top = height / 4
	# right = 164
	# bottom = 3 * height / 4

	# im1 = im.crop((left, top, right, bottom))

	imwidth = 1920
	imheight = 1604

	onethid_imw = imwidth/3   # = 640
	onethid_height = imheight/3  # = 534.6

	with col1:


		pic6 = st.image(Image.open('./picture/van.jpg').crop((onethid_imw*2, onethid_height, onethid_imw*3, onethid_height*2)), width=350)
		#st.write("## a")
		st.markdown('<h2 id ="a"><center><strong> a </center></a>', unsafe_allow_html=True)

		pic5 = st.image(Image.open('./picture/van.jpg').crop((onethid_imw, onethid_height, onethid_imw*2, onethid_height*2)), width=350)
		st.markdown('<h2 id ="a"><center><strong> d </center></a>', unsafe_allow_html=True)
		pic3 = st.image(Image.open('./picture/van.jpg').crop((onethid_imw*2, 0, onethid_imw*3, onethid_height)), width=350)	
		st.markdown('<h2 id ="a"><center><strong> g </center></a>', unsafe_allow_html=True)
		#st.markdown('<p><center><strong> d </center></span></p>', unsafe_allow_html=True)
		#st.markdown('<div data-testid="caption" class="css-1b0udgb etr89bj0" style="width: 500px;"><span style="font-size: 20px"><center><strong> g </center></span></div>', unsafe_allow_html=True)

	with col2:

		pic9 = st.image(Image.open('./picture/van.jpg').crop((onethid_imw*2, onethid_height*2, onethid_imw*3, onethid_height*3)), width=350)
		st.markdown('<h2 id ="a"><center><strong> b </center></a>', unsafe_allow_html=True)

		pic7 = st.image(Image.open('./picture/van.jpg').crop((0, onethid_height*2, onethid_imw, onethid_height*3)), width=350)
		st.markdown('<h2 id ="a"><center><strong> e </center></a>', unsafe_allow_html=True)

		pic1 = st.image(Image.open('./picture/van.jpg').crop((0, 0, onethid_imw, onethid_height)), width=350)
		st.markdown('<h2 id ="a"><center><strong> h </center></a>', unsafe_allow_html=True)

	with col3:

		pic4 = st.image(Image.open('./picture/van.jpg').crop((0, onethid_height, onethid_imw, onethid_height*2)), width=350)
		st.markdown('<h2 id ="a"><center><strong> c </center></a>', unsafe_allow_html=True)

		pic8 = st.image(Image.open('./picture/van.jpg').crop((onethid_imw, onethid_height*2, onethid_imw*2, onethid_height*3)), width=350)
		st.markdown('<h2 id ="a"><center><strong> f </center></a>', unsafe_allow_html=True)

		pic2 = st.image(Image.open('./picture/van.jpg').crop((onethid_imw, 0, onethid_imw*2, onethid_height)), width=350)
		st.markdown('<h2 id ="a"><center><strong> i </center></a>', unsafe_allow_html=True)

	with col4:				
		pass


	st.write("## Hãy xắp xếp hình trên vào thứ tự trong khung để hoàn thiện")
	st.image(Image.open('./picture/frame.PNG'), width=400)
	selection = st.multiselect(" ", options=["a", "b", "c", "d", "e", "f", "g", "h", "i"])

	if st.button("Xem kết quả: "):

		if selection == ["h", "i", "g", "c", "d", "a", "e", "f", "b"]:
			st.write("#### Chính xác chúc mừng bạn :tada:")

			col5, col6, col7, col8, col9, col10 = st.columns(6)



			with col5:


				pic1 = st.image(Image.open('./picture/van.jpg').crop((0, 0, onethid_imw, onethid_height)), width=200)  

				pic4 = st.image(Image.open('./picture/van.jpg').crop((0, onethid_height, onethid_imw, onethid_height*2)), width=200)
			
				pic7 = st.image(Image.open('./picture/van.jpg').crop((0, onethid_height*2, onethid_imw, onethid_height*3)), width=200)


			with col6:

				pic2 = st.image(Image.open('./picture/van.jpg').crop((onethid_imw, 0, onethid_imw*2, onethid_height)), width=200)

				pic5 = st.image(Image.open('./picture/van.jpg').crop((onethid_imw, onethid_height, onethid_imw*2, onethid_height*2)), width=200)
				pic8 = st.image(Image.open('./picture/van.jpg').crop((onethid_imw, onethid_height*2, onethid_imw*2, onethid_height*3)), width=200)


			with col7:
				pic3 = st.image(Image.open('./picture/van.jpg').crop((onethid_imw*2, 0, onethid_imw*3, onethid_height)), width=200)

				pic6 = st.image(Image.open('./picture/van.jpg').crop((onethid_imw*2, onethid_height, onethid_imw*3, onethid_height*2)), width=200)

				pic9 = st.image(Image.open('./picture/van.jpg').crop((onethid_imw*2, onethid_height*2, onethid_imw*3, onethid_height*3)), width=200)

			with col8:
				pass
			with col9:
				pass

			with col10:
				pass
			st.write("----")
			st.write("#### Bức ảnh hoàn thiện ")
			st.image(Image.open('./picture/van.jpg'), width=800)
			st.write("""##### Thông tin tranh vẽ
				Tên: Fields near the Alpilles
	Tác giả: Vincent van Gogh’s
	Năm: 1889
	Địa điểm: Pháp""")

		else:
			st.write("#### Bạn sai rồi hãy xắp xếp lại nhé :cry:")




	
