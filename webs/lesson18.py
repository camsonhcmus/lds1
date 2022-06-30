import streamlit as st
from PIL import Image
import random
import pandas as pd
import streamlit.components.v1 as components

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

	st.markdown("## Hãy sắp xếp hình theo hình mẫu")
	st.image(Image.open('./picture/van.jpg'), width=800)
	
	st.write("### Hình cần sắp xếp: ")
	col1, col2, col3, col4 = st.columns(4)

	st.markdown('''''', unsafe_allow_html=True)



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

	lsta =["a", "b", "c", "d", "e", "f", "g", "h", "i"]

	st.write("## Hãy sắp xếp hình trên vào thứ tự trong khung để hoàn thiện")
	st.image(Image.open('./picture/frame.PNG'), width=400)

	

	selection = st.multiselect(" ", options=["a", "b", "c", "d", "e", "f", "g", "h", "i"])
	

	# col17, col18, col19, col20, col21, col22 = st.columns(6)
	# with col17:
	# 	st.write("##### Vị trí thứ nhất: ")
	# 	po1 = st.multiselect(" ", options=["a", "b", "c", "d", "e", "f", "g", "h", "i"])
	# 	if len(po1) == 1:
	# 		st.write("bạn đã chọn %s, hãy chọn 1 hình khác ở vị trí khác" %(po1))
	# 	elif len(po1) > 1:
	# 		st.write("chỉ chọn 1 hình thôi bạn")
	# 	else:
	# 		st.write("chọn 1 hình đi bạn")
		
	# 	st.write("##### Vị trí thứ bốn: ")
	# 	po4 = st.multiselect(" ", options=["a", "b", "c", "d", "e", "f", "g", "h", "i"])
	# 	if len(po4) == 1:
	# 		st.write("bạn đã chọn %s, hãy chọn 1 hình khác ở vị trí khác" %(po4))
	# 	elif len(po4) > 1:
	# 		st.write("chỉ chọn 1 hình thôi bạn")
	# 	else:
	# 		st.write("chọn 1 hình đi bạn")

	# 	st.write("##### Vị trí thứ bảy: ")
	# 	po7 = st.multiselect(" ", options=["a", "b", "c", "d", "e", "f", "g", "h", "i"])
	# 	if len(po7) == 1:
	# 		st.write("bạn đã chọn %s, hãy chọn 1 hình khác ở vị trí khác" %(po7))
	# 	elif len(po7) > 1:
	# 		st.write("chỉ chọn 1 hình thôi bạn")
	# 	else:
	# 		st.write("chọn 1 hình đi bạn")

	# with col18:
	# 	st.write("##### Vị trí thứ hai: ")
	# 	po2 = st.multiselect(" ", options=["a", "b", "c", "d", "e", "f", "g", "h", "i"])
	# 	if len(po2) == 1:
	# 		st.write("bạn đã chọn %s, hãy chọn 1 hình khác ở vị trí khác" %(po2))
	# 	elif len(po2) > 1:
	# 		st.write("chỉ chọn 1 hình thôi bạn")
	# 	else:
	# 		st.write("chọn 1 hình đi bạn")
		
	# 	st.write("##### Vị trí thứ năm: ")
	# 	po5 = st.multiselect(" ", options=["a", "b", "c", "d", "e", "f", "g", "h", "i"])
	# 	if len(po5) == 1:
	# 		st.write("bạn đã chọn %s, hãy chọn 1 hình khác ở vị trí khác" %(po5))
	# 	elif len(po5) > 1:
	# 		st.write("chỉ chọn 1 hình thôi bạn")
	# 	else:
	# 		st.write("chọn 1 hình đi bạn")

	# 	st.write("##### Vị trí thứ tám: ")

	# 	po8 = st.multiselect(" ", options=["a", "b", "c", "d", "e", "f", "g", "h", "i"])
	# 	if len(po8) == 1:
	# 		st.write("bạn đã chọn %s, hãy chọn 1 hình khác ở vị trí khác" %(po8))
	# 	elif len(po8) > 1:
	# 		st.write("chỉ chọn 1 hình thôi bạn")
	# 	else:
	# 		st.write("chọn 1 hình đi bạn")

	# with col17:
	# 	st.write("##### Vị trí thứ ba: ")
	# 	po3 = st.multiselect(" ", options=["a", "b", "c", "d", "e", "f", "g", "h", "i"])
	# 	if len(po3) == 1:
	# 		st.write("bạn đã chọn %s, hãy chọn 1 hình khác ở vị trí khác" %(po3))
	# 	elif len(po3) > 1:
	# 		st.write("chỉ chọn 1 hình thôi bạn")
	# 	else:
	# 		st.write("chọn 1 hình đi bạn")
		
	# 	st.write("##### Vị trí thứ sáu: ")
	# 	po6 = st.multiselect(" ", options=["a", "b", "c", "d", "e", "f", "g", "h", "i"])
	# 	if len(po6) == 1:
	# 		st.write("bạn đã chọn %s, hãy chọn 1 hình khác ở vị trí khác" %(po6))
	# 	elif len(po6) > 1:
	# 		st.write("chỉ chọn 1 hình thôi bạn")
	# 	else:
	# 		st.write("chọn 1 hình đi bạn")

	# 	st.write("##### Vị trí thứ chín: ")

	# 	po9 = st.multiselect(" ", options=["a", "b", "c", "d", "e", "f", "g", "h", "i"])
	# 	if len(po9) == 1:
	# 		st.write("bạn đã chọn %s, hãy chọn 1 hình khác ở vị trí khác" %(po9))
	# 	elif len(po9) > 1:
	# 		st.write("chỉ chọn 1 hình thôi bạn")
	# 	else:
	# 		st.write("chọn 1 hình đi bạn")

	# with col17:
	# 	pass
	# with col17:
	# 	pass
			#background-color: #2196F3;

	a = components.html(
	"""
		<style>
		.grid-container {
		display: grid;
		grid-template-columns: 350px 350px 350px;
		grid-template-rows: 300px 300px 300px;
		column-gap:0px;
		padding: 10px;

			}

		.grid-item {
			background-color: rgba(255, 255, 255, 1);
			border: 0px solid rgba(0, 0, 0, 0);
			padding: 10px;
			font-size: 10px;
			text-align: center;
			}
			</style>

			<div class="grid-container">


	""",height=0,
	)

	def convert(letter):
		if letter == "a":
			return Image.open('./picture/van.jpg').crop((onethid_imw*2, onethid_height, onethid_imw*3, onethid_height*2))

		if letter == "d":
			return Image.open('./picture/van.jpg').crop((onethid_imw, onethid_height, onethid_imw*2, onethid_height*2))

		if letter == "g":
			return Image.open('./picture/van.jpg').crop((onethid_imw*2, 0, onethid_imw*3, onethid_height))

		if letter == "b":
			return Image.open('./picture/van.jpg').crop((onethid_imw*2, onethid_height*2, onethid_imw*3, onethid_height*3))

		if letter == "e":
			return Image.open('./picture/van.jpg').crop((0, onethid_height*2, onethid_imw, onethid_height*3))

		if letter == "h":
			return Image.open('./picture/van.jpg').crop((0, 0, onethid_imw, onethid_height))
	
		if letter == "c":
			return Image.open('./picture/van.jpg').crop((0, onethid_height, onethid_imw, onethid_height*2))

		
		if letter == "f":
			return Image.open('./picture/van.jpg').crop((onethid_imw, onethid_height*2, onethid_imw*2, onethid_height*3))

		
		if letter == "i":
			return Image.open('./picture/van.jpg').crop((onethid_imw, 0, onethid_imw*2, onethid_height))

	def convert_link(letter):

		
		if letter == "a":
			return "http://lds1.herokuapp.com/media/37068b419a9ce8eb9757b200346a5d62df4ed2b6a57b9f2cf601da48.jpeg"

		if letter == "d":
			return "http://lds1.herokuapp.com/media/4822feab6575154f88e77c728a8ed04af3cb9cba1e71e915ccf50be6.jpeg"

		if letter == "g":
			return "http://lds1.herokuapp.com/media/c7270549e24c7d5efb3f78dde00afe2b9b416f4bc48d22d135a92cf9.jpeg"

		if letter == "b":
			return "http://lds1.herokuapp.com/media/0c8c84e1de46757a427e77439f1a3e945e9dc74629a082d2e150cc48.jpeg"

		if letter == "e":
			return "http://lds1.herokuapp.com/media/e06ea8ff20461e27a8c01ec295749c0cfdceb395cde2cfbe58826b2b.jpeg"

		if letter == "h":
			return "http://lds1.herokuapp.com/media/23dccc106aac9e0629f421b9b8965eb1ae0ce145dd6fd2b177112f85.jpeg"
				
		if letter == "c":
			return "http://lds1.herokuapp.com/media/3df669d60a16a571bed787c03092d2bbf02b590c7e30242b79539934.jpeg"

					
		if letter == "f":
			return "http://lds1.herokuapp.com/media/60e44e072372a701f1dd3b70847b5e7e1003ee03bb92f6376b31ab34.jpeg"

					
		if letter == "i":
			return "http://lds1.herokuapp.com/media/0b6db80630c154f5b3ef242087afc0cd65e8edc7bbe74dd424b07212.jpeg"

	if st.button("Xem kết quả: "):
		try:

			if selection == ["h", "i", "g", "c", "d", "a", "e", "f", "b"]:
				st.write("#### Chính xác chúc mừng bạn :tada:")


				st.markdown('<div class="grid-item"><img src="'+convert_link(selection[0])+'"><img src="'+convert_link(selection[1])+'"><img src="'+convert_link(selection[2])+'"></div>', unsafe_allow_html=True)
				st.markdown('<div class="grid-item"><img src="'+convert_link(selection[3])+'"><img src="'+convert_link(selection[4])+'"><img src="'+convert_link(selection[5])+'"></div>', unsafe_allow_html=True)
				st.markdown('<div class="grid-item"><img src="'+convert_link(selection[6])+'"><img src="'+convert_link(selection[7])+'"><img src="'+convert_link(selection[8])+'"></div>', unsafe_allow_html=True)

				st.write("----")
				st.write("""##### Thông tin tranh vẽ
		Tên: Fields near the Alpilles
		Tác giả: Vincent van Gogh’s
		Năm: 1889
		Địa điểm: Pháp""")

			else:
				st.write("#### Bạn sai rồi hãy xắp xếp lại nhé :cry:")

				st.markdown('<div class="grid-item"><img src="'+convert_link(selection[0])+'"><img src="'+convert_link(selection[1])+'"><img src="'+convert_link(selection[2])+'"></div>', unsafe_allow_html=True)
				st.markdown('<div class="grid-item"><img src="'+convert_link(selection[3])+'"><img src="'+convert_link(selection[4])+'"><img src="'+convert_link(selection[5])+'"></div>', unsafe_allow_html=True)
				st.markdown('<div class="grid-item"><img src="'+convert_link(selection[6])+'"><img src="'+convert_link(selection[7])+'"><img src="'+convert_link(selection[8])+'"></div>', unsafe_allow_html=True)

				# st.markdown('<div class="grid-item"><img src="http://192.168.11.103:8081/media/0c8c84e1de46757a427e77439f1a3e945e9dc74629a082d2e150cc48.jpeg"></div>', unsafe_allow_html=True)

		except:
			pass




	
