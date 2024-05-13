import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


#导入相关的包
import sys
sys.path.append('../namemodule')

from namemodule.duihuamodule import get_chat_response
from  langchain.memory import  ConversationBufferMemory #有记忆的


#有记忆对话的机器人版本
chat = None
#如果openai没有在会话中(会话的作用是存储一些历史信息),则设置为空
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ''
elif st.session_state["OPENAI_API_KEY"] != '':
    # chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"],
    #                                      openai_api_base="https://api.aigc369.com/v1")
    chat = ChatOpenAI(model="gpt-3.5-turbo",openai_api_base="https://api.aigc369.com/v1",
                                          openai_api_key = "sk-8DdVVv5xOLRoSdLN5d1274Dc70514a40Be4684F7C152F04c")

st.session_state["OPENAI_API_KEY"] = 'sk-8DdVVv5xOLRoSdLN5d1274Dc70514a40Be4684F7C152F04c'
chat = ChatOpenAI(model="gpt-3.5-turbo",openai_api_base="https://api.aigc369.com/v1",
                                          openai_api_key = "sk-8DdVVv5xOLRoSdLN5d1274Dc70514a40Be4684F7C152F04c")


st.set_page_config(
    page_title="Wecome to Openai",
    layout= "wide",
    page_icon="👀使用机器人👀"
)
#目录
st.title("😀  Too酷 :red[智能对话] 😀 ")
st.subheader("大语言模型-智能对话")

st.markdown(
    """
    <style>
    .custom-divider {
        margin-top: 0px;
        margin-bottom: 0px;
        border-top: 1px solid red;
        color:red;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)


if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "万能对话机器人"}]
col1 = st.columns(20)
with col1[0]:
    st.page_link("./🏠 首页.py", label='', icon="⚙",help="设置")
with col1[1]:
    st.page_link("./🏠 首页.py", label='', icon="💒",help="首页")
with col1[2]:
    st.page_link("./🏠 首页.py", label='', icon="🤡",help="面具")
with col1[3]:
    st.page_link("./🏠 首页.py", label='', icon="🤖",help="机器人")


st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)







if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "万能对话机器人"}]
for message in st.session_state["messages"]:
    # if message["role"] == "ai":
    #     st.markdown("🤖 " + message["content"])  # 自定义 AI 表情
    # else:
    #     st.markdown("🧑 " + message["content"])  # 自定义人类表情

    st.chat_message(message["role"]).write(message["content"])

# st.link_button("Go to gallery", "https://streamlit.io/gallery")

prompt = st.chat_input("☞ 输入你想知道的")
# st.markdown("[🧡](https://www.example.com)", unsafe_allow_html=True)


if prompt:
    if not st.session_state["OPENAI_API_KEY"]:
        st.info("请输入你的OpenAI API Key")
        st.stop()
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)
    # st.markdown("🧑 " + prompt)

    with st.spinner("AI正在思考中，请稍等..."):
        response = get_chat_response(prompt, st.session_state["memory"],
                                     st.session_state["OPENAI_API_KEY"])
    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)
    # st.markdown("🤖 " + response)


