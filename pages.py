import streamlit as st

def main_page():
    st.title('AI Makeover')
    st.markdown('您的智能穿搭助手')
    with st.popover('点击查看详情'):
        st.markdown(
            '''
            AI Makeover是一款基于多模态大模型的智能穿搭工具
            '''
        )

def chat_page():
    st.markdown('### 请输入您的穿搭需求，并上传您的自拍照，我们将会给您提供智能穿搭推荐')
    st.markdown('**请上传您的自拍照**')
    st.file_uploader('',type=['png','jpg','jpeg'])
    st.chat_input('请输入您的穿搭需求')