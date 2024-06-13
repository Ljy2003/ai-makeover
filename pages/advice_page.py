import streamlit as st
import pandas as pd

ans = '收到'

question = st.chat_input('请输入您的需求')
if st.button('返回',type='primary',use_container_width=True):
    st.switch_page('pages/chat_page.py')


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