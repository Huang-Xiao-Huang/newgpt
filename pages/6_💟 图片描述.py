from langchain_openai import  ChatOpenAI
import streamlit as st
import os
from PIL import Image
import sys

sys.path.append('../namemodule')
from namemodule.shitumodule import  shiTu

#图片分类
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ''
elif st.session_state["OPENAI_API_KEY"] != '':
    chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"],
                                         openai_api_base="https://api.aigc369.com/v1")
st.set_page_config(page_title="文档总结",layout="wide")
st.title("Too酷 :red[图片描述]")
st.subheader("🤫 图片描述 🤫")
chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"],
                                         openai_api_base="https://api.aigc369.com/v1")


def main():
    folder_path = st.file_uploader(":red[🗂]上传图片", type=["PNG", "JPG"], help="支持文件类型图片",
                                     label_visibility="visible")
    # folder_path = rf'{folder_path}'
    print(folder_path)

    buttoned = st.button("🆗  开启描述")

    if buttoned :
        # 读取文件夹中的文件
        st.info("使用文档")

        # except:pass
    else:
        st.write('请输入文件夹路径。')

main()



# 显示图片并应用样式
# st.image("your_image.jpg", caption="Original Image", use_column_width=True)