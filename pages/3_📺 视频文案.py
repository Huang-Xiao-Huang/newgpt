import  streamlit as st
from langchain_openai import ChatOpenAI


#视频生成文档

#导入相关的包
import sys
sys.path.append('../namemodule')
from namemodule import videomodule

import time
import  base64

str_ = ''
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ''
elif st.session_state["OPENAI_API_KEY"] != '':
    chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"],
                                         openai_api_base="https://api.aigc369.com/v1")

st.title(" 🎬 Too酷 :red[视频脚本文案] ")
st.subheader("👌 好玩 | 有趣 👌  ")
st.write("请你提供一个脚本的主题，设置做视频的时长，就可以生成视频脚本了")

st.divider() #下划线

subject = st.text_input("💡 请输入视频的主题")
video_length = st.number_input("⏱️ 请输入视频的时长（单位：分钟）", min_value=0.1, step=0.1)
creativity = st.slider("✨ 请输入视频脚本的创造力", min_value=0.0,
                       max_value=1.0, value=0.2, step=0.1)


submit = st.button("📖  生成脚本")

if submit and not chat:
    st.info("请输入你的OpenAI API密钥")
    st.stop()
if submit and not subject:
    st.info("请输入视频的主题")
    st.stop()
if submit and not video_length >= 0.1:
    st.info("视频长度需要大于或等于0.1")
    st.stop()

if submit:
    with st.spinner("AI正在思考中，请稍等..."):
        search_result, title, script = videomodule.generate_script(subject, video_length, creativity, st.session_state["OPENAI_API_KEY"])
    st.success("视频脚本已生成！")
    st.subheader("🔥 标题：")
    st.write(title)
    st.subheader("📝 视频脚本：")
    st.write(script)

    str_ = script
    with st.expander("维基百科搜索结果 👀"):
        st.info(search_result)


#下载数据
text_contents = str_
file_name =  "视频生成文案" + str(int(time.time())) + ".txt"
b64 = base64.b64encode(text_contents.encode()).decode()
download_link = f'<a href="data:file/txt;base64,{b64}" download="{file_name}" ' \
                f' style="border: 1px solid gray; padding: 10px 15px;' \
                f' border-radius: 5px; text-decoration: none; color: #333;' \
                f'background-color:rgb(0, 204, 238);">{"👇 下载文案"}</a>'
st.markdown(download_link, unsafe_allow_html=True)