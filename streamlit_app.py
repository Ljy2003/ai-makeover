import streamlit as st
import pandas as pd
import numpy as np
import os
import json
import utils

@st.cache_data
def load_history():
    return pd.read_csv('./data/history_record.csv')

# st.set_page_config(layout="wide")
st.title('AI Makeover')

user_name = user_gender = user_height = user_years = None

if st.button('用户信息',use_container_width=True):
    utils.user_info()

if st.button('历史记录',use_container_width=True):
    utils.load_history()

st.header('Output')
st.markdown('请输入您的穿搭需求，并上传您的自拍照')




img_path = st.file_uploader('# 请上传您的自拍照',type=['jpg','png','jpeg'])

st.chat_input('输入您的穿搭需求')
