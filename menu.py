import streamlit as st

def menu():
    if 'loc' not in st.session_state.keys():
        import streamlit_app
    else:
        st.sidebar.page_link('streamlit_app.py',label='首页')
        st.sidebar.page_link('./pages/chat_page.py',label='穿搭推荐')
        st.sidebar.page_link('./pages/preview_page.py',label='穿搭预览')
