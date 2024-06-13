import streamlit as st

st.image('fig/main_page.png')
if st.button('# 上传',type='primary',use_container_width=True):
    st.switch_page('pages/chat_page.py')