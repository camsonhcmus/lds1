import streamlit as st
from PIL import Image
import hydralit_components as hc
import base64
import streamlit.components.v1 as components

def app():

	#c1, c2, c3 = st.columns(3)

	#with c1:

	#	image = Image.open('./picture/khtn.jpg')
	#	st.image(image)

	#with c2:
	#	st.title("Trung Tâm tin học khoa học tự nhiên Thành Phố Hồ Chí Minh")

	image = Image.open('./picture/khtn.PNG')
	st.image(image, width=500)

	st.markdown("------")

	st.markdown("""
	<style>
	.big-font {
    	font-size:80px !important;
	}
	body {
		background: url('./picture/bg.jpg') no-repeat center center;
	}
	</style>
	""", unsafe_allow_html=True)

	st.markdown('<center><p class="big-font"><font color="darkblue"> Tổng Quan Lập Trình Python</center></p>', unsafe_allow_html=True)

	# html_string = '''
	# 	<script type="text/javascript">
	# 	document.querySelectorAll('body').forEach(function(el) {
	# 	el.addEventListener(
	# 	'click',
	# 	function() {
	# 		var someimage = 'changableBackgroudImage';
	# 		document.body.style.background = 'url(picture/soccer.jpg) no-repeat center center'
	# 		}
	# 	});
	# 	</script>

	# '''
	# components.html(html_string)

	# html_string = '''<body style="background: url('https://www.dutchwatersector.com/sites/default/files/dws-f4w-soccer-match-netherlands-ghana-770px-1.jpg') no-repeat center center;"">'''
	# components.html(html_string)


	# main_bg = "bg.jpg"
	# main_bg_ext = "jpg"

	# side_bg = "bg.jpg"
	# side_bg_ext = "jpg"

	# st.markdown(
	# 	f"""
	# 	<style>
	# 	.reportview-container {{
	# 		background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
	# 	}}
	# 	.sidebar .sidebar-content {{
	#     	background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
	# 	}}
	# 	</style>
	# 	""",
	# 	unsafe_allow_html=True
	# )

	
	st.markdown("""### Chương trình (Program) 
		• Chương trình là tập hợp các chỉ thị lệnh yêu cầu máy tính thực thi một tác vụ cụ thể. 
	• Một cách chi tiết, chương trình là một bộ các hướng dẫn cho máy tính biết phải làm gì. 
	• Nếu chúng ta thay đổi chương trình máy tính sẽ thực hiện một bộ các hành động hoặc nhiệm vụ khác. 
""")

	st.markdown("""### Ngôn ngữ lập trình (Programming Language)
		• Là một ngôn ngữ nhân tạo
	• Gồm một tập các ký hiệu và cú pháp được chuẩn hóa để mô tả những xử lý mà người và máy đều có thể hiểu được 
		""")

	st.markdown("""### Lập trình (Programming) 
		• Là quá trình xây dựng các chương trình nguồn được viết bằng một hoặc nhiều ngôn ngữ lập trình
	• Gồm một tập các ký hiệu và cú pháp được chuẩn hóa để mô tả những xử lý mà người và máy đều có thể hiểu được 
		""")

	st.markdown("""### Tại sao nên học lập trình?
		• Vì lập trình là một phần cơ bản của khoa học máy tính.
	• Có sự hiểu biết về lập trình sẽ giúp chúng ta hiểu biết về những điểm mạnh và điểm yếu của máy tính.
	• Để ta có thể làm ra những sản phẩm phục vụ các công việc 
		""")

	st.markdown("""### Python là một ngôn ngữ lập trình cấp cao, thông dịch, hướng đối tượng và đa mục đích.""")

	st.markdown("""### Triết lý thiết kế:
		• Code dễ đọc, dễ viết
	• Cú pháp ngắn gọn
	• Cấu trúc rõ ràng - Phù hợp khi xây dựng các loại ứng dụng với quy mô từ nhỏ đến lớn 
	""")

	st.markdown("""### Lịch sử phát triển của Python:
		• Python đã bắt đầu được thực hiện vào tháng 12 năm 1989 bởi Guido van Rossum tại Centrum Wiskunde & Informatica (CWI) ở Hà Lan.
	• Python xuất bản version 1.0 tháng 01/1994.
	• Python 3.3 xuất bản ngày 29/09/2017
	• Python 3.4 xuất bản ngày 18/03/2019
	• Phiên bản mới nhất, Python 3.10.0 xuất bản ngày 04/10/2021
	• Mã nguồn mở, miễn phí
	""")

	st.markdown("""### Đặc điểm của Python:
		• Code dễ đọc, dễ học
	• Bố cục trực quan, dễ hiểu
	• Lập trình hướng đối tượng, lập trình hàm, thủ tục (đa lập trình)
	• Từ khóa ít, cấu trúc đơn giản
	• Thư viện chuẩn rộng lớn, tương thích và tích hợp với Linux, Windows, và Macintosh (macOS)
	• Là ngôn ngữ thông dịch, quá trình debug dễ dàng
	• Hỗ trợ lập trình GUI, mã nguồn mở, có thể tích hợp với các ngôn ngữ lập trình khác 
	""")	


	#st.markdown("<style> body {background-image: url('./picture/khtn.jpg');}</style>", unsafe_allow_html=True)
	#c1, c2, c3 = st.columns(3)

	
	#with c2:
	#	st.title("")
	#st.balloons()

	


	#st.markdown('<img src="/picture/khtn.jpg" alt="" style="width:500px;height:600px;">', unsafe_allow_html=True)

	#import base64

	#@st.cache(allow_output_mutation=True)
	#def get_base64_of_bin_file(bin_file):
    #	with open(bin_file, 'rb') as f:
    #    	data = f.read()
    #	return base64.b64encode(data).decode()

	#def set_png_as_page_bg(png_file):
    #	bin_str = get_base64_of_bin_file(png_file)
    #	page_bg_img = '''
    #	<style>
    #	body {
    #	background-image: url("data:image/png;base64,%s");
    #	background-size: cover;
    #	}
    #	</style>
    #	''' % bin_str
    #
    #	st.markdown(page_bg_img, unsafe_allow_html=True)
    #	return

	#set_png_as_page_bg('/picture/background.png')
