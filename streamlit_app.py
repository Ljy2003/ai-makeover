import streamlit as st
from menu import menu

st.session_state['loc'] = 'main'

st.title('AI Makeover')
st.markdown('您的智能穿搭助手')
# with st.popover('点击查看详情',use_container_width=True):
#     st.markdown(
#         '''
#         AI Makeover是一款基于多模态大模型的智能穿搭工具
#         '''
#     )
# with st.popover('使用说明',use_container_width=True):
#     st.markdown(
#         '''
#         * 在侧边栏点击 **穿搭推荐** ，上传您的自拍照（全身或半身），
#         随后输入您的穿搭需求（如：我想要干净清爽/柔和舒适的穿搭）
#         * 在穿搭推荐界面中，点击 **生成穿搭建议**，得到个性化的穿搭建议
#         * 在穿搭推荐界面中，点击 **查看推荐潮流单品**，挑选合适的推荐单品
#         * 
#         '''
#     )
st.image('fig/logo.png')
menu()