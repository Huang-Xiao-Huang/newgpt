from langchain_openai import  ChatOpenAI
import streamlit as st
from namemodule import zaiyaomodule

#文本总结
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ''
    chat = None
elif st.session_state["OPENAI_API_KEY"] != '':
    chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"],
                                         openai_api_base="https://api.aigc369.com/v1")

st.set_page_config(page_title="文本摘要",layout="wide")

st.title("Too酷 :red[文本摘要]")
st.subheader("🤫 文本摘要")

# chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"],
#                                          openai_api_base="https://api.aigc369.com/v1")

#上传文件


uploaded_file = st.file_uploader( ":red[🗂]上传文件",type=["PDF","DOCX","TXT"],help="支持文件类型",
                                  label_visibility = "visible")

shengc = st.button(" ✏ 生成总结")
if chat:
    if uploaded_file is not None:
        file_contents  = uploaded_file.getvalue().decode("utf-8")
        # 将文件内容显示在界面上
        with st.expander(" 🗂 显示文件内容:"):
            st.write(file_contents)
        if shengc:
            try:
                with st.spinner("AI努力创作中，请稍等..."):
                    st.divider()
                    data = zaiyaomodule.Sumary(file_contents, st.session_state["OPENAI_API_KEY"])
                    st.write(f'''{data} :balloon:''')
            except:
                st.warning("获取失败")
    else:
        st.warning("请重新上传文件...")
else:
    st.warning("请在首页输入api-key")








