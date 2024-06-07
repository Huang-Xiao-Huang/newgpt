import streamlit as st
from langchain_openai import ChatOpenAI
import pandas as pd

#导入相关的包
import sys
sys.path.append('../namemodule')
from namemodule.vimdeomodule import musicsgen

# 设置Streamlit应用的标题
st.set_page_config(page_title="音乐生成",layout="wide")

st.title("Too酷 :red[音乐生成工具]")
st.subheader(":red[🎶] 音乐生成工具")

#有记忆对话的机器人版本
chat = None
#如果openai没有在会话中(会话的作用是存储一些历史信息),则设置为空
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ''
    st.warning("请在首页输入OPENAI_API_KEY")
elif st.session_state["OPENAI_API_KEY"] != '':
    chat = ChatOpenAI(model="gpt-3.5-turbo",openai_api_base="https://api.aigc369.com/v1",
                                          openai_api_key = "sk-8DdVVv5xOLRoSdLN5d1274Dc70514a40Be4684F7C152F04c")




title = st.text_input("音乐标题")
prompt = st.text_input("请输入音乐提示词")
button = st.button("生成音乐")
if button:
    with st.spinner("音频生成中"):
        music, video,geci = musicsgen(prompt, title)
    with st.expander("歌词"):
        st.write(geci)
    st.write("声音")
    st.audio(music)
    st.write("视频")
    st.video(video)


