import streamlit as st
from menu import menu
import PIL
from PIL import Image
from io import BytesIO

st.session_state['loc'] = 'chat'
st.markdown('### 请输入您的穿搭需求，并上传您的自拍照，我们将会为您提供智能穿搭推荐')

col1,col2 = st.columns(2)
with col1:
    st.button('生成穿搭建议',use_container_width=True)
with col2:
    st.button('查看推荐潮流单品',use_container_width=True)


file = st.file_uploader('**请上传您的自拍照**',type=['png','jpg','jpeg'])
if file is not None:
    st.image(file,caption='自拍',use_column_width=True)
    bytes_data = file.getvalue()
    bytes_stream = BytesIO(bytes_data)
    img = Image.open(bytes_stream)
    img.save('./data/images/selfie//selfie.png')

st.chat_input('请输入您的穿搭需求')
menu()
