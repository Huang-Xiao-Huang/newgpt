from openai import OpenAI
import streamlit as st


import sys
sys.path.append('../namemodule')
from namemodule import jianlimodule



st.set_page_config(page_title="简历书写",layout="wide")

st.title("Too酷 :red[简历书写]")
st.subheader(":red[ 📝] 简历书写")
st.write("快速书写简历")


st.divider() #分割线

client = None
#如果openai没有在会话中(会话的作用是存储一些历史信息),则设置为空
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ''
    st.warning("请在首页输入OPENAI_API_KEY")
elif st.session_state["OPENAI_API_KEY"] != '':
       client = OpenAI(api_key = st.session_state["OPENAI_API_KEY"],
                                     base_url = "https://api.aigc369.com/v1")




if client:
    name = st.text_input("你的名字")
    age = st.number_input("你的年龄",min_value=10,max_value=70)
    education = st.selectbox(
        '你的学历',
    ("专科", "本科", "硕士研究生",
         "博士研究生", "其他")
    )

    job = st.text_input("你面试的职位")
    years = st.number_input("工作年限",min_value=0)
    city = st.text_input("意向城市")

    # number = st.number_input('🗒 生成简历的个数', value=1, min_value=1, max_value=4)

    bttons = st.button("💾生成简历")


    if bttons:
        try:
            with st.spinner("⌛简历生成中..."):
                dic_info = {"姓名":name,"年龄":age,"学历":education,"工作年限":years
                                    ,"面试职位":job,"意向城市":city}

                da = jianlimodule.Jianli(dic_info,st.session_state["OPENAI_API_KEY"])
                st.divider() #分割线
                de = st.markdown(da)
                print(da)
                st.text_area('显示简历信息',da,height=500)

        except:
            st.warning("无法生成简历")
            st.stop()
    else:
        pass
else:
    st.warning("请在首页输入api-key")
