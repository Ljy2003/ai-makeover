import streamlit as st
import pandas as pd
import numpy as np

# @st.cache_data
# def load_history():
#     return pd.read_csv('D:\work2\Project1_data\history_record.csv')

st.set_page_config(layout="wide")
st.title('AI Makeover')

user_name = user_gender = user_height = user_years = None
# with st.popover('用户信息',use_container_width=True):
#     st.markdown('请输入您的信息，方便我们生成对应的建议')
#     user_name = st.text_input('姓名')
#     user_gender = st.selectbox('性别', ['男', '女'])
#     user_years = st.number_input('年龄', min_value=10, step=1)
#     user_height = st.number_input('身高',value=170, step=1)


# history = load_history()
# with st.popover('历史记录',use_container_width=True):
    
#     for i in history.index:
#         choose = st.button(history.iloc[i]['name'],key=i, use_container_width=True)
#         if choose:
#             choose = np.zeros(len(history.index))
#             choose[i] = 1
#             history['choose'] = choose
#     history.to_csv('D:\work2\Project1_data\history_record.csv',index=False)


# history.to_csv('D:\work2\Project1_data\history_record.csv',index=False)



st.header('Output')
# try:
#     st.text(history['name'][history['choose'] == 1].values[0])
# except:
#     st.markdown('请输入您的穿搭需求，并上传您的自拍照')




img_path = st.file_uploader('# 请上传您的自拍照',type=['jpg','png','jpeg'])

st.chat_input('输入您的穿搭需求')
