import streamlit as st
from PIL import Image

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

	st.markdown('<center><p class="big-font"><font color="darkblue">Bài 2: Toán tử</center></p>', unsafe_allow_html=True)

	#@dataclasses.dataclass 
	#class GameState:
	#	number_to_guess: int
	#	game_number: int = 0
	#	game_over: bool = False

	#@st.cache(allow_output_mutation=True)
	#def persistent_game_state() -> GameState:
	#	return GameState(random.randint(1, 1000))

	#state = persistent_game_state()

	#if st.button("new game"):
	#	state.number_to_guess = random.randint(1, 1000)
	#	state.game_number += 1
	#	state.game_over = False

	st.markdown("## Với các con số từ 1 đến 50, hãy tìm con số chia hết cho số được nhập")

	st.image(Image.open('./picture/phepchia.jpg'), width=500)

	inpd = st.text_input("Hãy nhập con số chia: ")

	if st.button("Thực hiện phép chia"):
		try:
			st.write("Những số chia hết là:")
			for i in range (1, 51):
				inpd = int(inpd)
				resultd = i / inpd
				mol = i % inpd

				if mol == 0:

					st.write("%s" %(i))
				else:
					pass
		except:
			st.error("Hãy nhập số bạn nhé :smile:")
