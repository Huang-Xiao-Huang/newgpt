import streamlit as st
from langchain_openai import ChatOpenAI
import sys
sys.path.append('../namemodule')
from namemodule.xiaohongshumodule import generate_xiaohongshu
import time
import  base64



if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ''
elif st.session_state["OPENAI_API_KEY"] != '':
    chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"],
                                         openai_api_base="https://api.aigc369.com/v1")

str_ = ''
st.title("🖊 Too酷 :red[小红书文案]")
st.subheader('😀 小红书精彩:red[文案],输入就有，快来试试')

st.divider() #分割线


theme = st.text_input("💡 主题")
num_title  = st.number_input("🔢 生成小红书的标题个数 (最小是1，最大是5)",  placeholder=None,
                             min_value=1, max_value=5, value = "min",step=1)

submit  = st.button("开始创作")
st.divider() #分割线

if submit and not st.session_state["OPENAI_API_KEY"]:
    st.info("请输入你的OpenAI API密钥")
    st.stop()
if submit and not theme:
    st.info("请输入生成内容的主题")
    st.stop()
if submit:
    with st.spinner("AI正在努力创作中，请稍等..."):
        result = generate_xiaohongshu(theme, st.session_state["OPENAI_API_KEY"],num_title)
        # st.divider()

    str_ = "标题:" + "\n" + "\n".join([result.titles[i] for i in range(num_title)]) + "\n"  # 标题拼接
    str_ += "正文:" + "\n" + result.content  # 文本
    left_column, right_column = st.columns(2)
    # 左边部分
    with left_column:
        for i in range(num_title):
            st.markdown(f"##### 小红书标题{i + 1}")
            st.write(result.titles[i])

    # 右边部分
    with right_column:
        st.markdown("##### 小红书正文")
        st.write(result.content)

    #保存文件
    # text_contents = str_
    # file_name =  "小红书创意文案" + str(int(time.time())) + ".txt"
    # saved = st.download_button('👇 下载文案', text_contents,file_name)
    # if saved:
    #     st.info("已完成下载..")
    #     st.stop()
text_contents = str_
file_name =  "小红书创意文案"+ str(int(time.time())) + ".txt"
b64 = base64.b64encode(text_contents.encode()).decode()
download_link = f'<a href="data:file/txt;base64,{b64}" download="{file_name}" ' \
                f' style="border: 1px solid gray; padding: 10px 15px;' \
                f' border-radius: 5px; text-decoration: none; color: #333;' \
                f'background-color:rgb(0, 204, 238);">{"👇 点击下载文案"}</a>'
st.markdown(download_link, unsafe_allow_html=True)








