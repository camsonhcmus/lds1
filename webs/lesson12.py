import streamlit as st
from PIL import Image
import random
import pandas as pd
import numpy as np

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

	st.markdown('<center><p class="big-font"><font color="darkblue">Bài 9: Function</center></p>', unsafe_allow_html=True)

	st.markdown("## Chào mừng bạn đến cuộc chơi xí ngầu")

	st.image(Image.open('./picture/pairdice.jpg'), width=500)

	st.write("""### Luật chơi sẽ như sau:

		- Trong vòng 3 lượt khi lắc con số lớn hơn đối thủ thì sẽ được 1 điểm

	- Nếu lắc con số nhỏ hơn hoặc bằng đối thủ thì sẽ được 0 điểm

	- Nếu bạn có tổng số điểm hơn đối thủ thì bạn sẽ là người chiến thắng

		""")




	def rolldice(min, max):
		number = random.randint(min,max)
		
		return number

	"session:", st.session_state	

	if "turn" not in st.session_state:
		st.session_state["turn"] = 0
	# if "countdata" not in st.session_state:
	# 	st.session_state["countdata"] = pd.DataFrame(columns=['lượt', 'điểm xí ngầu của bạn', 'Điểm xí ngầu đối thủ'])
	if "countpoint" not in st.session_state:
		st.session_state["countpoint"] = 0


	if st.button('lắc'):
		st.session_state.turn += 1

		a = st.session_state.turn
		st.write("##### Bạn đang chơi lượt thứ %s" %(st.session_state.turn))
		number = rolldice(1,6)
		number1 = rolldice(1,6)

		col1, col2 = st.columns(2)

		with col1:
			if number == 1:
				image1 = Image.open('./picture/1.PNG')
				st.image(image1, width=150)

			elif number == 2:
				image2 = Image.open('./picture/2.PNG')
				st.image(image2, width=150)

			elif number == 3:
				image3 = Image.open('./picture/3.PNG')
				st.image(image3, width=150)

			elif number == 4:
				image4 = Image.open('./picture/4.PNG')
				st.image(image4, width=150)

			elif number == 5:
				image5 = Image.open('./picture/5.PNG')
				st.image(image5, width=150)

			else:
				image6 = Image.open('./picture/6.PNG')
				st.image(image6, width=150)

			st.markdown("### Bạn")


		with col2:
			if number1 == 1:
				image1 = Image.open('./picture/1.PNG')
				st.image(image1, width=150)

			elif number1 == 2:
				image2 = Image.open('./picture/2.PNG')
				st.image(image2, width=150)

			elif number1 == 3:
				image3 = Image.open('./picture/3.PNG')
				st.image(image3, width=150)

			elif number1 == 4:
				image4 = Image.open('./picture/4.PNG')
				st.image(image4, width=150)

			elif number1 == 5:
				image5 = Image.open('./picture/5.PNG')
				st.image(image5, width=150)

			else:
				image6 = Image.open('./picture/6.PNG')
				st.image(image6, width=150)

			st.markdown("### Đối thủ")

		st.markdown(" ")
		st.markdown(" ")
		st.markdown(" ")

		if st.session_state.turn < 4:
			if number == number1:
				st.markdown("##### Huề rồi bạn")
			if number < number1:
				st.markdown("##### Bạn đã thua")

				
			if number > number1:
				st.markdown("##### Bạn đã thắng")
				if st.session_state.turn < 4:
					st.session_state.countpoint += 1

		#st.markdown("----")

		# st.session_state.countdata.loc[st.session_state.turn] = [st.session_state.turn, st.session_state.countpoint]
		

			#st.write("Bảng số điểm của bạn sau mỗi lượt")
			#st.dataframe(st.session_state.countdata)
			st.markdown(" ")
			st.write("##### Số điểm bạn đang có %s điểm" %(st.session_state.countpoint))


		else:
			st.write('##### Bạn đã hết lượt chơi hãy Hãy bấm nút "Chơi lại" nếu bạn muốn chơi')
			st.markdown(" ")
			st.write("##### Tổng số điểm bạn có là %s điểm" %(st.session_state.countpoint))

		if st.session_state.turn > 3:
			if st.session_state.countpoint >= 2:
				st.write("##### Bạn đã là người thắng cuộc")
			else:
				st.write("##### Đối thủ của bạn là người thắng cuộc")

	st.markdown("----")
	st.write('Hãy bấm nút "Chơi lại" nếu bạn muốn chơi lại hoặc refresh lượt chơi')
	if st.button('Chơi lại'):

		for key in st.session_state.keys():
			del st.session_state[key]

		st.session_state.turn = 0
		st.session_state.countdata = pd.DataFrame(columns=['lượt', 'Tổng số điểm có được sau mỗi lượt'])
		st.session_state.countpoint = 0
