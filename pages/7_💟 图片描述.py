from langchain_openai import  ChatOpenAI
import streamlit as st
import os
from PIL import Image
import sys

sys.path.append('../namemodule')
from namemodule import imagedescribe

#图片分类
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ''
elif st.session_state["OPENAI_API_KEY"] != '':
    chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"],
                                         openai_api_base="https://api.aigc369.com/v1")
st.set_page_config(page_title="图片描述",layout="wide")
st.title("Too酷 :red[图片描述]")
st.subheader("🤫 图片描述 🤫")
chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"],
                                         openai_api_base="https://api.aigc369.com/v1")

def main():
    folder_path = st.text_input("请输入图片链接")
    if st.button("🖼 开始描述") and st.session_state["OPENAI_API_KEY"]:
        st.image(folder_path)
        with st.spinner("⌛图片描述生成中..."):
            result = imagedescribe.im_describe(folder_path,st.session_state["OPENAI_API_KEY"])
            st.text(result)
    else:
        st.warning("请在首页输入api_key")
main()




