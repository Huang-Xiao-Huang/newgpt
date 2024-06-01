import streamlit as st
from langchain_openai import ChatOpenAI
import pandas as pd

#导入相关的包
import sys
sys.path.append('../namemodule')
from namemodule.dataprocessmodule import dataframe_agent

# 设置Streamlit应用的标题
st.set_page_config(page_title="翻译小助手",layout="wide")

st.title("Too酷 :red[分析工具]")
st.subheader(":red[📖] 智能数据分析工具")

#有记忆对话的机器人版本
chat = None
#如果openai没有在会话中(会话的作用是存储一些历史信息),则设置为空
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ''
    st.warning("请在首页输入OPENAI_API_KEY")
elif st.session_state["OPENAI_API_KEY"] != '':
    chat = ChatOpenAI(model="gpt-3.5-turbo",openai_api_base="https://api.aigc369.com/v1",
                                          openai_api_key = "sk-8DdVVv5xOLRoSdLN5d1274Dc70514a40Be4684F7C152F04c")



def create_chart(input_data, chart_type):
    df_data = pd.DataFrame(input_data["data"], columns=input_data["columns"])
    df_data.set_index(input_data["columns"][0], inplace=True)
    if chart_type == "bar":
        st.bar_chart(df_data)
    elif chart_type == "line":
        st.line_chart(df_data)
    elif chart_type == "scatter":
        st.scatter_chart(df_data)


data = st.file_uploader("上传你的数据文件（csv格式）：", type="csv")
if data:
    st.session_state["df"] = pd.read_csv(data)
    with st.expander("原始数据"):
        st.dataframe(st.session_state["df"])

query = st.text_area("请输入你关于以上表格的问题，或数据提取请求，或可视化要求（支持散点图、折线图、条形图）：")
button = st.button("生成回答")

if button and not st.session_state["OPENAI_API_KEY"]:
    st.info("请输入你的OpenAI API密钥")
if button and "df" not in st.session_state:
    st.info("请先上传数据文件")
if button and st.session_state["OPENAI_API_KEY"] and "df" in st.session_state:
    with st.spinner("AI正在思考中，请稍等..."):
        response_dict = dataframe_agent(st.session_state["OPENAI_API_KEY"], st.session_state["df"], query)
        if "answer" in response_dict:
            st.write(response_dict["answer"])
        if "table" in response_dict:
            st.table(pd.DataFrame(response_dict["table"]["data"],
                                  columns=response_dict["table"]["columns"]))
        if "bar" in response_dict:
            create_chart(response_dict["bar"], "bar")
        if "line" in response_dict:
            create_chart(response_dict["line"], "line")
        if "scatter" in response_dict:
            create_chart(response_dict["scatter"], "scatter")

