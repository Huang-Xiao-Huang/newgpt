import streamlit as st


#==============首页信息==================
chat = None
#如果openai没有在会话中(会话的作用是存储一些历史信息),则设置为空
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ''


# 页面设置
st.set_page_config(page_title="AI 智能小工具",layout= "wide",page_icon="👀")
st.title(":red[TOO] 酷智能工具")



# 创建三个列
col1, col2, col3 = st.columns(3)
# 在每个列中创建 metric 组件，并为每个组件应用不同的样式
with col1:
    st.markdown('<div class="metric-container-1">🌡️ Temperature<br><span class="custom-text">🧠 人工智能</span><br>🚀 高效</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-container-2">💨 Wind<br><span class="custom-text">📚 大模型</span><br>🔑 简单</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="metric-container-3">💧 Humidity<br><span class="custom-text">💻 AICG</span><br>🛠 实用</div>', unsafe_allow_html=True)


#===============侧边栏信息============================
with st.sidebar:
    st.subheader('TOO 酷')
    st.write("😀 大模型 | 生成AI")
    st.write("📫 邮箱: 11233@qq.com")
    st.write("💡 开发者: 哒哒er")



# 设置部分
st.markdown("##### ⚙ 基本设置")

col1,col2 = st.columns([3,1])
with col1:
    openai_api_key = st.text_input(label= "请输入api_key",type="password")
    saved = st.button("💾 保存")



#提交保存按钮
if saved:
    st.session_state["OPENAI_API_KEY"] = openai_api_key
    st.info("你的api已经保存")

#分割线
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

# 设置背景颜色和居中文本
#==================设置面具=====================
st.markdown("##### 🕶 挑选文字面具")
col1, col2, col3,col4,col5,col6 = st.columns(6)
with col1:
    st.page_link("pages/1_💬 智能对话.py", label=" 智能对话 ", icon="1️⃣")

with col2:
    st.page_link("pages/2_📕 小红书文案.py", label="小红书文案 ", icon="2️⃣")

with col3:
    st.page_link("pages/3_📺 视频文案.py", label=" 视频文案 ", icon="3️⃣")

with col4:
    st.page_link("pages/4_📔 文档问答.py", label=" PDF问答 ", icon="4️⃣")

with col5:
    st.page_link("pages/5_📁 文本摘要.py", label=" 文本摘要 ", icon="5️⃣")


col6,col7, col8,col9,col10 = st.columns(5)
with col6:
    st.page_link("pages/8_📝 简历书写.py", label="简历书写 ", icon="9️⃣")

st.markdown("##### 🕶 挑选图片面具")
col11, col12, col13, col14, col15 = st.columns(5)


with col11:
    st.page_link("pages/6_💟 图片描述.py"  ,label="图片描述", icon="7️⃣")

with col12:
    st.page_link("pages/7_🖼 以文生图.py"  ,label="以文生图", icon="8️⃣")



#分割线条
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

