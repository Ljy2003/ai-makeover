import streamlit as st


st.image('fig/main_page.png')

m = st.markdown("""
<style>
.stApp {
    background: #FFF1EB;
}
</style>
""", unsafe_allow_html=True)

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #CC0000;
    color:#ffffff;
    height: 70px;
    font-size: 20px !important;
}
div.stButton > button:hover {
background-color: #FF6666;
color:#ffffff;
                }
</style>""", unsafe_allow_html=True)

#设置column
st.write('''<style>
[data-testid="column"] {
    min-width: calc(5% - 1rem) !important;
}
</style>''', unsafe_allow_html=True)

st.write("""
<style>
div.stImage > button:first-child{
    width: 200px;
    height: 200px;
}
</style>
""", unsafe_allow_html=True)
col1,col2,col3 = st.columns([1,8,1])
with col2:
    if st.button('# 上传',use_container_width=True):
        st.switch_page('pages/chat_page.py')

st.divider()