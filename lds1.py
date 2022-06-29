
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
from webs import overview ,lesson1 , lesson2, lesson3, lesson4, lesson5, lesson6, lesson7, lesson8, lesson9, lesson10, lesson11, lesson12, lesson13, lesson14, lesson15, lesson16, lesson17, lesson18

import base64


# Change Page Icon and Page Title
img = Image.open('./picture/khtn.jpg')
st.set_page_config(page_title='LDS1', page_icon = img, layout="wide", initial_sidebar_state="collapsed")
 

# Hide Setting Menu and Footer
hide_menu_style = """
		<style>
		#MainMenu {visibility: hidden; }
		footer {visibility: hidden; }
		<style>
		"""

st.markdown(hide_menu_style, unsafe_allow_html = True)

#st.markdown('<div><style>h1{color: red;}</style></div>', unsafe_allow_html=True)




# html_string = '''
# 	<style>
# 	css-18e3th9{
#     position: absolute;
#     background: rgb(253, 254, 254);
#     color: rgb(49, 51, 63);
#     inset: 0px;
#     overflow: hidden;
#     background-image: url('https://www.dutchwatersector.com/sites/default/files/dws-f4w-soccer-match-netherlands-ghana-770px-1.jpg');
# 	}
# 	</style>
	
#  	'''
# components.html(html_string) 




# html_string = '''
# 	<body onload="init()">
# 	<script language="javascript">
# 	function init() {
# 	var someimage = 'changableBackgroudImage';
# 	document.body.style.background = '#3371ff';
#	<div class="stApp steamlit-wide css-hgtx2x eczokvf1"></div>
# 	}
# 	</script>
	# <style>
	# .css-hgtx2x {
	# background-image: url('https://www.dutchwatersector.com/sites/default/files/dws-f4w-soccer-match-netherlands-ghana-770px-1.jpg');
	# }
	# </style>

# 	'''css-1wrcr25 
# components.html(html_string) 
# 'url(img/bg.jpg) no-repeat center center'

# st.markdown('''
# 	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css" integrity="sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn" crossorigin="anonymous">
# 	<div class="alert alert-primary" role="alert">A simple primary alert—check it out!</div>
# ''', unsafe_allow_html=True)
#
#main_bg = "bg.jpg"
#main_bg_ext = "jpg"

#side_bg = "bg.jpg"
#side_bg_ext = "jpg"

#st.markdown(
#    f"""
#    <style>
#    .reportview-container {{
#        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
#    }}
#   .sidebar .sidebar-content {{
#        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
#    }}
#    </style>
#    """,
#    unsafe_allow_html=True
#)



with st.sidebar:
    selected = option_menu("LDS 1", ['Tổng Quan', 'Bài 1', 'Bài 2', 'Bài 3', 'Bài 4', 'Bài 5', 'Bài 6', 'Bài 7', 'Bài 8', 'Bài 9', 'Bài 10', 'Bài 11', 'Bài 12', 'Bài 13', 'Bài 14', 'Bài 15'], 
        icons=['book', 'book', 'book', 'book', 'book', 'book', 'book', 'book', 'book', 'book', 'book', 'book', 'book', 'book', 'book', 'book'], menu_icon="code-slash", default_index=0)

if selected == "Tổng Quan":
	overview.app()

if selected == "Bài 1":
   	lesson1.app()

if selected == "Bài 2":
   	lesson2.app()

if selected == "Bài 3":
   	lesson3.app()

if selected == "Bài 4":
   	lesson4.app()

if selected == "Bài 5":
   	lesson6.app()

if selected == "Bài 6":
   	lesson7.app()

# if selected == "Bài 7":
#    	lesson8.app()

# if selected == "Bài 8":
#    	lesson9.app()

if selected == "Bài 7":
   	lesson10.app()

if selected == "Bài 8":
   	lesson11.app()   

if selected == "Bài 9":
   	lesson12.app()  

if selected == "Bài 10":
   	lesson13.app()

if selected == "Bài 11":
   	lesson14.app()   

if selected == "Bài 12":
   	lesson15.app()  

if selected == "Bài 13":
   	lesson16.app()  

if selected == "Bài 14":
   	lesson17.app() 

if selected == "Bài 15":
   	lesson18.app() 

# if selected == "Bài 18":
#    	lesson18.app() 
