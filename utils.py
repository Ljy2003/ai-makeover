import json
import pandas as pd
import streamlit as st
import numpy as np

def read_user_info():
    with open('./data/user_info.json','r') as f:
        return json.load(f)
    
def dump_user_info(name,sex,age,height):
    info = {"name": name, "sex": sex, "age": age, "height": height}
    with open('./data/user_info.json','w',encoding='utf-8') as f:
        return json.dump(info,f)
    
@st.cache_data
def load_history():
    return pd.read_csv('./data/history_record.csv')

history = load_history()

@st.experimental_dialog('历史记录')
def load_history():
    for i in history.index:
        choose = st.button(history.iloc[i]['name'],key=i, use_container_width=True)
        if choose:
            choose = np.zeros(len(history.index))
            choose[i] = 1
            history['choose'] = choose
    
    history.to_csv('./data/history_record.csv',index=False)

@st.experimental_dialog('请输入您的信息，方便我们生成对应的建议')
def user_info():
    user_name = st.text_input('姓名')
    user_sex = st.selectbox('性别', ['男', '女'])
    user_age = st.number_input('年龄', min_value=10, step=1)
    user_height = st.number_input('身高',value=170, step=1)
    dump_user_info(user_name,user_sex,user_age,user_height)
