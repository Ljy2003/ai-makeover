import streamlit as st
import PIL
from PIL import Image
from io import BytesIO

st.set_page_config(layout='wide')

st.image('./fig/chat_title.png')

with open('data/need.txt','r',encoding='utf-8') as f:
    needs = f.readline()
text = st.text_input('请输入您的穿搭需求',needs)
flag = st.button('输入需求',use_container_width=True)
if flag:
    with open('data/need.txt','w',encoding='utf-8') as f:
        f.write(text)
    st.markdown('已上传您的穿搭需求')

file = st.file_uploader('**请上传您的自拍照**',type=['png','jpg','jpeg'])
if file is not None:
    st.image(file,caption='自拍',use_column_width=True)
    bytes_data = file.getvalue()
    bytes_stream = BytesIO(bytes_data)
    img = Image.open(bytes_stream)
    img.save('./data/images/selfie//selfie.png')

if st.button('一键改造',type='primary',use_container_width=True):
    pass
if st.button('返回',use_container_width=True):
    st.switch_page('streamlit_app.py')
