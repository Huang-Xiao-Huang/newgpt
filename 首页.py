import streamlit as st

# ==============首页信息==================
chat = None
# 如果openai没有在会话中(会话的作用是存储一些历史信息),则设置为空
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ''

# 页面设置
st.set_page_config(page_title="AI 智能小工具", layout="wide", page_icon="👀")
st.title(":red[TOO] 酷智能工具")

# 显示图片
# image = open(r"D:\AI 大语言模型项目\bigdemo\index1.jpg", 'rb').read()
# st.image(image)


# =============banner============
# 定义不同的 CSS 样式
html = """
<style>
.metric-container-1 {
    background-color: lightblue;
    color: black; /* 设置字体颜色为黑色 */
    padding: 15px;
    border-radius: 10px;
    box-shadow: 2px 2px 5px grey;
}

.metric-container-2 {
    background-color: lightgreen;
    color: black; /* 设置字体颜色为白色 */
    padding: 15px;
    border-radius: 10px;
    box-shadow: 2px 2px 5px grey;
}

.metric-container-3 {
    background-color: lightcoral;
    color: black; /* 设置字体颜色为黑色 */
    padding: 15px;
    border-radius: 10px;
    box-shadow: 2px 2px 5px grey;
}

.custom-text {
    font-weight: bold;
    color: #FF5733; /* 设置自定义颜色 */
    font-size: 20px; /* 设置字体大小为20px */
}
</style>
"""

# 在页面上渲染自定义样式
st.markdown(html, unsafe_allow_html=True)

# 创建三个列
col1, col2, col3 = st.columns(3)
# 在每个列中创建 metric 组件，并为每个组件应用不同的样式
with col1:
    st.markdown(
        '<div class="metric-container-1">🌡️ Temperature<br><span class="custom-text">🧠 人工智能</span><br>🚀 高效</div>',
        unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-container-2">💨 Wind<br><span class="custom-text">📚 大模型</span><br>🔑 简单</div>',
                unsafe_allow_html=True)

with col3:
    st.markdown(
        '<div class="metric-container-3">💧 Humidity<br><span class="custom-text">💻 AICG</span><br>🛠 实用</div>',
        unsafe_allow_html=True)

# st.title(":red[TOO] 酷智能工具")
# st.subheader(":blue[快捷 | 方便 | 准确]")

# ===============侧边栏信息============================
with st.sidebar:
    st.subheader('TOO 酷')
    st.write("😀 大模型 | 生成AI")
    st.write("📫 邮箱: 11233@qq.com")
    st.write("💡 开发者: 哒哒er")

# ============分割线样式=========
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

# 设置部分
st.markdown("##### ⚙ 基本设置")

col1, col2 = st.columns([3, 1])
with col1:
    openai_api_key = st.text_input(label="请输入api_key", type="password")

    saved = st.button("💾 保存")

    # 定义自定义 CSS 样式
    html = """
    <style>
    .custom-button {
        height: 50px; /* 设置按钮高度为50px */
        line-height: 50px; /* 垂直居中文本 */
        text-align: center; /* 文本水平居中 */
        background-color: lightblue;
        color: black;
        font-size: 16px;
        font-weight: bold;
        border-radius: 5px;
        cursor: pointer;
    }
    </style>
    """

    # 在页面上渲染自定义样式
    st.markdown(html, unsafe_allow_html=True)

    # 创建一个自定义样式的按钮
    # button_html = '<button class="custom-button">Custom Button</button>'
    # saved = st.markdown(button_html, unsafe_allow_html=True)
    # if st.markdown(button_html, unsafe_allow_html=True):
    #     st.session_state["OPENAI_API_KEY"] = openai_api_key
    #     st.info("你的api已经保存")
# st.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api-keys)")


# 提交保存按钮
if saved:
    st.session_state["OPENAI_API_KEY"] = openai_api_key
    st.info("你的api已经保存")

# 分割线
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

# 设置背景颜色和居中文本
# ==================设置面具=====================
st.markdown("##### 🕶 文字功能")
col1, col2, col3, col4, col5, col6 = st.columns(6)
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

col6, col7, col8, col9, col10, col11 = st.columns(6)
with col6:
    st.page_link("./pages/9_📝 简历书写.py", label="简历书写 ", icon="6️⃣")
with col7:
    st.page_link("./pages/10_📖 语言翻译.py", label="语言翻译 ", icon="7️⃣")

st.markdown("##### 🕶 图片功能")
col11, col12, col13, col14, col15 = st.columns(5)
with col11:
    st.page_link("pages/6_📷 识图工具.py", label=" 识图工具 ", icon="6️⃣")

with col12:
    st.page_link("pages/7_💟 图片描述.py", label="图片描述", icon="8️⃣")

with col13:
    st.page_link("pages/8_🖼 以文生图.py", label="以文生图", icon="9️⃣")


st.markdown("##### 🕶 智能工具")
cola, col1b, col1c, col1d, col1e = st.columns(5)
with cola:
    st.page_link("pages/11_📈 分析工具.py", label="分析工具", icon="9️⃣")



# ============面具样式设计部分=============================
# 面具部分的按钮
button_style_image = """
    <style>
    [data-testid="stHorizontalBlock"] {
        //background-color: #ccffff;
        border-radius: 5px;
        height:200%;
        padding-left:10px;
        padding-top:10px;
        padding-bottom:10px;


    }
    </style>
"""
st.markdown(button_style_image, unsafe_allow_html=True)
# 页面跳转按钮代码
diliver_image = """
    <style>
    [data-testid="stPageLink-NavLink"] {
        background-color:#66ccff;
        height:45px;
        box-shadow: 2px 2px 5px grey;
    }
    </style>
"""
st.markdown(diliver_image, unsafe_allow_html=True)

# 分割线条
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

