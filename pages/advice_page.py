import streamlit as st
import pandas as pd

#修改页面背景
# m = st.markdown("""
# <style>
# .stApp {
#     background-color: #FFFFFF;
# }
# </style>
# """, unsafe_allow_html=True)


# 修改按钮格式
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #CC0000;
    color:#ffffff;
}
div.stButton > button:hover {
background-color: #FF6666;
color:#ffffff;
    }
</style>""", unsafe_allow_html=True)

if st.button('返回'):
    st.switch_page('pages/chat_page.py')

st.markdown("<h1 style='text-align: center; color: #CCCCCC;'>Chat</h1>", unsafe_allow_html=True)

ans = '收到'
st.divider()

question = st.chat_input('请输入您的需求')



if 'chat' not in st.session_state:
    st.session_state['chat'] = {'question':[],'answer':[]}
elif question is None:
    for q,a in zip(st.session_state['chat']['question'],st.session_state['chat']['answer']):
        message_user = st.chat_message('我')
        message_assistant = st.chat_message("assistant")
        message_user.write(q)
        message_assistant.write(a)

if question is not None:
    st.session_state['chat']['question'].append(question)
    st.session_state['chat']['answer'].append(ans)
    for q,a in zip(st.session_state['chat']['question'],st.session_state['chat']['answer']):
        message_user = st.chat_message('我')
        message_assistant = st.chat_message("assistant")
        message_user.write(q)
        message_assistant.write(a)