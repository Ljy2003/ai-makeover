import streamlit as st
from menu import menu

st.session_state['loc'] = 'preview'
st.markdown('### 预览穿搭上身效果')

menu()