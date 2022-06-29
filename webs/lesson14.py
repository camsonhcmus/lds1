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

	st.markdown('<center><p class="big-font"><font color="darkblue">Bài 11: Xử lý ngoại lệ</center></p>', unsafe_allow_html=True)

	st.write("### Hãy hoàn thành câu hỏi của mỗi bức hình:")

	#st.markdown('<center><span style="font-size: 40px"><strong><span class="css-10trblm e16nr0p30">Chúng ta đều bắt đầu học tiểu học ở lớp ...</span></span></center>', unsafe_allow_html=True)
		
	st.markdown(
	""" <style>
			div[role="radiogroup"] >  :first-child{
				display: none !important;
			}
		</style>
		""",
	unsafe_allow_html=True
	)

	col1, col2, col3 = st.columns(3)

	with col1:
		st.image(Image.open('./picture/cow.jpg'), width=400)
		#st.markdown('<div data-testid="caption" class="css-1b0udgb etr89bj0" style="width: 500px;"><span style="font-size: 20px"><center><strong> con bò </center></span></div>', unsafe_allow_html=True)
		cow = st.checkbox("Hiện câu hỏi liên quan tới con bò")
		if cow:
			cowques = st.radio("Con bò đứng trên ...", options=["", "Ngôi nhà", "Phòng Học", "Đồng cỏ", "Cái cây"])

			if cowques == "Đồng cỏ":
				
				st.write("#### Chúc mừng :tada:")

			elif cowques == "":
				pass

			else:
				st.error("Hãy chọn lại phương án phù hợp bạn nhé :smile:")
		else:
			pass

	with col2:
		st.image(Image.open('./picture/boat.jpg'), width=400)
		#st.markdown('<div data-testid="caption" class="css-1b0udgb etr89bj0" style="width: 500px;"><span style="font-size: 20px"><center><strong> thuyền </center></span></div>', unsafe_allow_html=True)
		boats = st.checkbox("Hiện câu hỏi liên quan tới chiếc thuyền")
		if boats:
			cowques = st.radio("Chiếc thuyền đi trên ...", options=["", "Sàn nhà", "Lớp Học", "Đồng cỏ", "Biển"])

			if cowques == "Biển":
				
				st.write("#### Chúc mừng :tada:")
			elif cowques == "":
				pass
			else:
				st.error("Hãy chọn lại phương án phù hợp bạn nhé :smile:")
		else:
			pass

	with col3:
		st.image(Image.open('./picture/chair.jpg'), width=350)
		#st.markdown('<div data-testid="caption" class="css-1b0udgb etr89bj0" style="width: 400px;"><span style="font-size: 20px"><center><strong> ghế dựa </center></span></div>', unsafe_allow_html=True)
		chair = st.checkbox("Hiện câu hỏi liên quan tới cái ghế")

		if chair:
			cowques = st.radio("Chiếc ghế trên có bao nhiêu tay vịn ?", options=["", "bốn", "Lớp Học", "2", "Tất cả các ý kiến trên"])
			if cowques != "":
				try:
					int(cowques)
					st.write("#### Chúc mừng :tada:")
				except:
					st.error("Hãy chọn lại phương án phù hợp bạn nhé :smile:")
			else:
				pass
		else:
			pass

	col4, col5, col6 = st.columns(3)

	with col4:
		st.image(Image.open('./picture/tree.jpg'), width=400)
		#st.markdown('<div data-testid="caption" class="css-1b0udgb etr89bj0" style="width: 500px;"><span style="font-size: 20px"><center><strong> cây </center></span></div>', unsafe_allow_html=True)
		trees = st.checkbox("Hiện câu hỏi liên quan tới cái cây")

		if trees:
			onetrees = st.radio("Cái cây màu gì ?", options=["", "Đỏ", "Xanh lá", "Tím", "Vàng"])

			if onetrees == "Xanh lá":
				
				st.write("#### Chúc mừng :tada:")
			elif cowques == "":
				pass
			else:
				st.error("Hãy chọn lại phương án phù hợp bạn nhé :smile:")
		else:
			pass

	with col5:
		st.image(Image.open('./picture/number1.jpg'), width=400)
		#st.markdown('<div data-testid="caption" class="css-1b0udgb etr89bj0" style="width: 500px;"><span style="font-size: 20px"><center><strong> số 1 </center></span></div>', unsafe_allow_html=True)
		s1 =st.checkbox("Hiện câu hỏi liên quan tới số 1")
		if s1:
			orig = st.radio("Chúng ta đều bắt đầu học tiểu học ở lớp ...", options=["", "con bò", "cây", "1", "học sinh"])
			if orig != "":
				try:
					int(orig)
					st.write("#### Chúc mừng :tada:")
				except:
					st.error("Hãy chọn lại phương án phù hợp bạn nhé :smile:")
			else:
				pass
		else:
			pass

	with col6:
		st.image(Image.open('./picture/student.jpg'), width=600)
		#st.markdown('<div data-testid="caption" class="css-1b0udgb etr89bj0" style="width: 700px;"><span style="font-size: 20px"><center><strong> học sinh </center></span></div>', unsafe_allow_html=True)
		stu =st.checkbox("Hiện câu hỏi liên quan tới học sinh")

		if stu:
			onestu = st.radio("Điều gì quan trọng với học sinh ?", options=["", "Kiến thức", "Bằng cấp", "Bạn bè", "Tất cả các ý trên"])

			if onestu == "Tất cả các ý trên":
				
				st.write("#### Chúc mừng :tada:")

			elif cowques == "":
				pass

			else:
				st.error("Hãy chọn lại phương án phù hợp bạn nhé :smile:")
		else:
			pass
