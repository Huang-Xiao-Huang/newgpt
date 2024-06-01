import streamlit as st
from langchain_openai import ChatOpenAI


#导入相关的包
import sys
sys.path.append('../namemodule')
from namemodule.tranlatemodule import translate_text

# 设置Streamlit应用的标题
st.set_page_config(page_title="翻译小助手",layout="wide")

st.title("Too酷 :red[语言翻译]")
st.subheader(":red[📖] 多语言翻译")

#有记忆对话的机器人版本
chat = None
#如果openai没有在会话中(会话的作用是存储一些历史信息),则设置为空
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ''
    st.warning("请在首页输入OPENAI_API_KEY")
elif st.session_state["OPENAI_API_KEY"] != '':
    chat = ChatOpenAI(model="gpt-3.5-turbo",openai_api_base="https://api.aigc369.com/v1",
                                          openai_api_key = "sk-8DdVVv5xOLRoSdLN5d1274Dc70514a40Be4684F7C152F04c")

if 'text_area_content' not in st.session_state:
    st.session_state['text_area_content'] = ''
if "input_text" not in st.session_state:
    st.session_state['input_text'] = ''


# 创建一个下拉选择框，用户可以选择源语言
source_lang = st.selectbox('选择源语言', ['自动检测', '英语', '中文', '法语', '德语', '日语'])

# 创建一个下拉选择框，用户可以选择目标语言
target_lang = st.selectbox('选择目标语言', ['英语', '中文', '法语', '德语', '日语'])
col1,col2 = st.columns(2)
with col1:
    # 创建一个文本输入区域，用户可以在其中输入要翻译的文本
    text_to_translate = st.text_area('请输入文本',height=200)
    
with col2:

    transt = st.text_area('翻译的结果', st.session_state['text_area_content'],height=200)
# 开始按钮
transbutton = st.button("开始翻译")

if transbutton:
    if text_to_translate and source_lang and target_lang and chat:
        with st.spinner("正在翻译..."):
            st.session_state['input_text'] = text_to_translate
            dats = translate_text(text_to_translate,source_lang,target_lang,chat)
            st.session_state['text_area_content'] = dats
            # st.experimental_rerun() #实现实时刷新和数据更新
            st.success("翻译成功")
        


