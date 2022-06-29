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

	st.markdown('<center><p class="big-font"><font color="darkblue">Bài 3: Cấu trúc điều kiện</center></p>', unsafe_allow_html=True)

	st.markdown("## Hãy đoán con số ngẫu nhiên may mắn từ 1 đến 5 trong vòng 3 lượt")

	st.image(Image.open('./picture/lucky.png'), width=500)

	st.write("""### Luật chơi sẽ như sau:

		- Bạn có 3 lượt chơi

	- Trong vòng 3 lượt, bạn đoán trúng thì bạn sẽ chiến thắng 

	- Nếu như 3 lượt đoán không trúng thì nhấn bắm nút "Chơi lại"

		""")

	pre_num = st.text_input("Hãy nhập con số dự đoán: ")

	if "turn1" not in st.session_state:
		st.session_state["turn1"] = 0
	if "point1" not in st.session_state:
		st.session_state["point1"] = 0

	# st.markdown(
	# """ <button kind="primary" class="css-8k1y1z edgvbvh9">Dự đoán: </button>
	# 	""",
	# unsafe_allow_html=True
	# )



	number_test = random.randint(1,5 )

	if st.session_state.turn1 < 3 and st.session_state.point1 == 0:

		if st.button("Dự đoán: "):
			st.session_state.turn1 += 1
			st.write("##### Bạn đang chơi lượt thứ %s" %(st.session_state.turn1))

			try:
				pre_num = int(pre_num)

			except:
				st.error("Hãy nhập số bạn nhé")


			

			# if st.session_state.turn1 < 4 and pre_num != number_test:
					
			# 	if pre_num <= number_test:
			# 		st.write("Sai :cry: con số bạn nhỏ hơn con số may mắn")
					
			# 	elif pre_num >= number_test:
			# 		st.write("Sai :cry: con số bạn lớn hơn con số may mắn")

			# elif st.session_state.turn1 < 4 and pre_num == number_test:

			# 	st.write("Chính xác :tada:")
			# 	st.balloons()
			# 	st.write('Bạn đã thắng rồi hãy bắm nút "Chơi lại" nếu như bạn muốn chơi lại')

			# elif pre_num == number_test:
			# 	st.write('Bạn đã thắng rồi hãy bắm nút "Chơi lại" nếu như bạn muốn chơi lại')

			# elif st.session_state.turn1 >= 4 and pre_num != number_test: 
			# 	st.write('Bạn đã hết lượt hãy bắm nút "Chơi lại" nếu như bạn muốn thử vận may nữa')

			# elif st.session_state.turn1 >= 4 and pre_num == number_test: 
			# 	st.write('Bạn đã hết lượt hãy bắm nút "Chơi lại" nếu như bạn muốn thử vận may nữa')


			if pre_num == number_test:
				st.write("Chính xác :tada:")
				st.balloons()
				st.session_state.point1 += 1

			elif pre_num <= number_test:
				st.write("Sai :cry: con số bạn nhỏ hơn con số may mắn")
					
			elif pre_num >= number_test:
				st.write("Sai :cry: con số bạn lớn hơn con số may mắn")
			st.write("##### Số lần bạn đoán trúng là: %s lần" %(st.session_state.point1))

	elif st.session_state.turn1 < 3 and st.session_state.point1 >= 1:
		st.write("##### Bạn đã thắng cuộc")
	elif st.session_state.turn1 > 3 and st.session_state.point1 >= 1:

		st.write("##### Bạn đã thắng cuộc")

	elif st.session_state.turn1 > 3 and st.session_state.point1 == 0:

		st.write("##### Bạn đã thua cuộc")
	elif st.session_state.point1 >= 1:
		st.write("##### Bạn đã thắng")
		st.write("##### Nếu như bạn muốn chơi nữa thì hãy bấm nút chơi lại")

	elif st.session_state.point1 == 0:
		st.write("##### Bạn đã thua")





	st.markdown("----")
	#st.write('Hãy bấm nút "Chơi lại" nếu bạn muốn chơi lại hoặc refresh lượt chơi')
	if st.button('Chơi lại'):

		for key in st.session_state.keys():
			del st.session_state[key]

			st.session_state.turn1 = 0
			st.session_state.point1 = 0
