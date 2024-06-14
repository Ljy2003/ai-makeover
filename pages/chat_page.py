import streamlit as st
import PIL
from PIL import Image
import numpy as np
from io import BytesIO

#设置column
st.write('''<style>
[data-testid="column"] {
    width: calc(33.3333% - 1rem) !important;
    flex: 1 1 calc(33.3333% - 1rem) !important;
    min-width: calc(33% - 1rem) !important;
}
</style>''', unsafe_allow_html=True)

# 修改按钮格式
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #CC0000;
    color:#ffffff;
    font-size: 20px !important;
}
div.stButton > button:hover {
background-color: #FF6666;
color:#ffffff;
    }
</style>""", unsafe_allow_html=True)


m = st.markdown("""
<style>
.stApp {
    background: #FFF1EB;
}
</style>
""", unsafe_allow_html=True)


if st.button('$\leftarrow$'):
    st.switch_page('streamlit_app.py')

st.image('./fig/chat_title.png')


col1,col2 = st.columns(2)
with col1:
    if ('file' not in st.session_state.keys()) or st.session_state['file'] is None:
        st.image(np.ones((350,320,3)))
    else:
        file = st.session_state['file']
        st.image(file,caption='自拍',use_column_width=True)
        bytes_data = file.getvalue()
        bytes_stream = BytesIO(bytes_data)
        img = Image.open(bytes_stream)
        img.save('./data/images/selfie//selfie.png')
    col1_1,col1_2 = st.columns(2)
    if col1_1.button('输入需求',use_container_width=True):
        st.switch_page('pages/advice_page.py')
    if col1_2.button('一键改造',use_container_width=True):
        message = st.chat_message("assistant")
        message.write('aaaaaaaaa')
    st.session_state['file'] = st.file_uploader('**请上传您的自拍照**',type=['png','jpg','jpeg'])
    
with col2:
    st.image(np.ones((500,300,3)))
