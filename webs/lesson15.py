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

	st.markdown('<center><p class="big-font"><font color="darkblue">Bài 12: Random</center></p>', unsafe_allow_html=True)

	st.write("## Hãy tham gia trò oẳn tù tì với mình nào")

	st.image(Image.open('./picture/rpsc.jpg'), width=500)

	st.markdown(
	""" <style>
			div[role="radiogroup"] >  :first-child{
				display: none !important;
			}
		</style>
		""",
	unsafe_allow_html=True
	)

	player = st.radio("Bạn ra gì?", options=["0", "Búa", "Kéo", "Giấy"])

	def point2pic(player):
		if player == 3:
			return "Búa"
		elif player == 2:
			return "Kéo"
		elif player == 1:
			return "Giấy"
		elif player == 0:
			return "Búa"

	def convert(player):
		if player == 3 or player == "Búa":
			return Image.open('./picture/rock.png')
		elif player == 2 or player == "Kéo":
			return Image.open('./picture/scissors.png')
		elif player == 1 or player == "Giấy":
			return Image.open('./picture/paper.png')
		elif player == -1:
			return Image.open('./picture/picture.jpg')
		else:
			pass

	#if st.button('oẳn tù tì'):
	number = random.randint(1, 3)
	player2 = point2pic(number)
	if player == "Búa"or player == "Kéo"or player == "Giấy":
		col1, col2, col3 = st.columns(3)

		with col1:
			try:
				st.image(convert(player), width=200)
				st.write("### Bạn")
			except:
				pass
		with col2:
			st.image(Image.open('./picture/v-s.jpg'), width=200)
		with col3:
			st.image(convert(player2), width=200)
			st.write("### Đối thủ")
		st.write("----")
		st.write("## Kết quả: ")
		st.write(" ")
		st.write(" ")

	if player == "Búa" and player2 == "Búa":
		st.write("Huề rồi bạn")

	if player == "Búa" and player2 == "Kéo":
		st.write("Bạn thắng rồi")

	if player == "Búa" and player2 == "Giấy":
		st.write("Bạn thua rồi")

	if player == "Kéo" and player2 == "Búa":
		st.write("Bạn thua rồi ")

	if player == "Kéo" and player2 == "Kéo":
		st.write("Huề rồi bạn")

	if player == "Kéo" and player2 == "Giấy":
		st.write("Bạn thắng rồi")

	if player == "Giấy" and player2 == "Kéo":
		st.write("Bạn thua rồi")

	if player == "Giấy" and player2 == "Búa":
		st.write("Bạn thắng rồi")

	if player == "Giấy" and player2 == "Giấy":
		st.write("Huề rồi bạn")


