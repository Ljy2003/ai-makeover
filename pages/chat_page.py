import streamlit as st
from menu import menu

st.session_state['loc'] = 'chat'
st.markdown('### 请输入您的穿搭需求，并上传您的自拍照，我们将会给您提供智能穿搭推荐')

st.markdown('**请上传您的自拍照**')
st.file_uploader('',type=['png','jpg','jpeg'])
st.chat_input('请输入您的穿搭需求')
st.button('生成穿搭建议',use_container_width=True)
st.button('查看推荐潮流单品',use_container_width=True)
menu()