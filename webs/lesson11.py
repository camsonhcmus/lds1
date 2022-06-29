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

	st.markdown('<center><p class="big-font"><font color="darkblue">Bài 8: Dictionary</center></p>', unsafe_allow_html=True)

	#st.markdown('''<img src='./picture/soccer.png' height="180px" width="500px" />''', unsafe_allow_html=True)
	st.markdown(" ")
	st.image(Image.open('./picture/soccer.jpg'), width=1650)
	st.markdown(" ")
	col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

	with col1:
		e = st.image(Image.open('./picture/england.jpg'), width=250)


	with col2:
		g = st.image(Image.open('./picture/german.jpeg'), width=180)

	with col3:
		sk = st.image(Image.open('./picture/s_korea.png'), width=200)


	with col4:
		j = st.image(Image.open('./picture/Japan.png'), width=250)

	with col5:
		f = st.image(Image.open('./picture/france.jpg'), width=200)


	with col6:
		s = st.image(Image.open('./picture/spain.png'), width=200)

	with col7:
		v = st.image(Image.open('./picture/vietnam-flag.jpg'), width=150)


	with col8:
		i = st.image(Image.open('./picture/italia.jpg'), width=200)		

	st.markdown("## Cùng tạo các trận đấu ngẫu nhiên")

	def convert(nation):
		if nation == "Anh":
			return Image.open('./picture/england.jpg')
		elif nation == "Tây Ban Nha":
			return Image.open('./picture/spain.png')
		elif nation == "Pháp":
			return Image.open('./picture/france.jpg')
		elif nation == "Đức":
			return Image.open('./picture/german.jpeg')
		elif nation == "Ý":
			return Image.open('./picture/italia.jpg')
		elif nation == "Nam Hàn":
			return Image.open('./picture/s_korea.png')
		elif nation == "Nhật Bản":
			return Image.open('./picture/Japan.png')
		elif nation == "Việt Nam":
			return Image.open('./picture/vietnam-flag.jpg')

	if st.button("Tạo trận đấu: "):

		team = ["Anh", "Đức", "Nam Hàn", "Nhật Bản", "Pháp", "Tây Ban Nha", "Việt Nam", "Ý"]
		pairs = {}

		for p in range(len(team) // 2):
			pairs[p+1] = [team.pop(random.randrange(len(team))),team.pop(random.randrange(len(team)))] 
			#st.markdown("Trận đấu thứ %s - %s vs %s" % (p+1, pairs[p+1][0], pairs[p+1][1]))
			col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12 = st.columns(12)

			with col1:
				st.write("Trận đấu thứ %s"% (p+1))
				# st.markdown('<div data-testid="caption" class="css-1b0udgb etr89bj0" style="width: 500px;"><span style="font-size: 20px"><center><strong> con bò </center></span></div>', unsafe_allow_html=True)
			with col2:
				st.image(convert(pairs[p+1][0]), width=50)

			with col3:
				st.write(pairs[p+1][0])
			with col4:
				st.image(Image.open('./picture/v-s.jpg'), width=50)
			with col5:
				st.write(pairs[p+1][1])			
			with col6:
				st.image(convert(pairs[p+1][1]), width=50)
			with col7:
				pass
			with col8:
				pass
			with col9:
				pass
			with col10:
				pass
			with col11:
				pass
			with col12:
				pass
