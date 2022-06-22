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

	st.markdown('<center><p class="big-font"><font color="darkblue">Bài 12: Function</center></p>', unsafe_allow_html=True)

	st.markdown("## Chào mừng bạn đến cuộc chơi xí ngầu")

	st.image(Image.open('./picture/pairdice.jpg'), width=500)

	st.write("""### Luật chơi sẽ như sau:

		- Nếu bạn lắc được xí ngầu với 2 con số giống nhau sẽ được cộng lại 2 con số

	- Nếu bạn lắc được xí ngầu khác nhau thì số xí ngầu 1 sẽ trừ số của xí ngầu 2

	- Bạn sẽ thua nếu bị số âm (ví dụ: xí ngầu 1 là 2 và xí ngầu 2 là 4 thì 2 - 4 = -2 suy ra bạn sẽ thua do kết quả âm)

	- Bạn sẽ thắng nếu lắc được 2 con số 6
		""")




	def rolldice(min, max):
		number = random.randint(min,max)
		
		return number

		



	if st.button('lắc'):
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

			st.markdown("### Xí ngầu 1")


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

			st.markdown("### Xí ngầu 2")
