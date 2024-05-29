from langchain_openai import  ChatOpenAI
import streamlit as st
import sys

import os

sys.path.append('../namemodule')
from namemodule.PDFansermodule import pdf_anwser,txt_answer,pdf_agent

from langchain.memory import ConversationBufferMemory


#文档问答
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ''
    st.warning("请在首页输入OPENAI_API_KEY")
elif st.session_state["OPENAI_API_KEY"] != '':
    chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"],
                                         openai_api_base="https://api.aigc369.com/v1")

if "memory1" not in st.session_state:
    st.session_state["memory1"] = ConversationBufferMemory(
        return_messages=True,
        memory_key="chat_history",
        output_key="answer"
    )


st.set_page_config(page_title="文档问答",layout="wide")
st.title("Too酷 :red[文档问答]")
st.subheader("🤫 文档解答 🤫")
# chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"],
#                                          openai_api_base="https://api.aigc369.com/v1")

folder_path = st.file_uploader(":red[🗂]上传txt或PDF文档", type=["PDF","TXT"], help="文档格式",
                                 label_visibility="visible")
input_questions = st.text_input("📑 请输入你的问题")

if folder_path and input_questions and st.session_state["OPENAI_API_KEY"]:
    if folder_path.name.split('.')[-1] == "pdf":
        with st.spinner("AI正在思考中，请稍等..."):
            response = pdf_agent(st.session_state["OPENAI_API_KEY"], st.session_state["memory1"],
                                folder_path, input_questions)
            st.write("### 答案")
            st.write(response["answer"])
            st.session_state["chat_history"] = response["chat_history"]

    elif folder_path.name.split('.')[-1] == "txt":
        print(folder_path)
       
        response = txt_answer(st.session_state["OPENAI_API_KEY"], st.session_state["memory1"],
                                folder_path, input_questions)
        st.write("### 答案")
        st.write(response["answer"])
        st.session_state["chat_history"] = response["chat_history"]
else:
    st.warning("请输入相关的信息")


if "chat_history" in st.session_state:
    with st.expander("历史消息"):
        for i in range(0, len(st.session_state["chat_history"]), 2):
            human_message = st.session_state["chat_history"][i]
            ai_message = st.session_state["chat_history"][i+1]
            st.write(human_message.content)
            st.write(ai_message.content)
            if i < len(st.session_state["chat_history"]) - 2:
                st.divider()


# if folder_path:
#     # print(folder_path.name.split('.')[-1])
#     if folder_path.name.split('.')[-1] == "pdf":
#         docs = pdf_answers()
#         str_ = ''
#         for i in docs:
#             str_ += i.page_content
#
#         with st.container(height=300):
#
#             st.markdown(str_)
#
#         input_questions = st.text_input("📑 请输入你的问题")
#         buttoned = st.button("🆗  回答问题")
#         if buttoned:
#             with st.spinner("回答问题中..."):
#                 de = pdf_anwser(str_, input_questions, st.session_state["OPENAI_API_KEY"])
#                 st.write(de)
#     elif folder_path.name.split('.')[-1] == "txt":
#         docs = txt_process()
#         str_ = ''
#         for i in docs:
#             str_ += i.page_content
#         # with st.expander(" 🗂 文件内容:"):
#         #     st.markdown(str_)
#
#         with st.container(height=300):
#             st.markdown(str_)
#
#         input_questions = st.text_input("📑 请输入你的问题")
#         buttoned = st.button("🆗 回答")
#
#         if buttoned:
#             with st.spinner("生成答案中..."):
#                 de = txt_answer(docs, input_questions, st.session_state["OPENAI_API_KEY"])
#                 st.write(de)
# st.divider()
#
# # 显示图片并应用样式
# # st.image("your_image.jpg", caption="Original Image", use_column_width=True)
