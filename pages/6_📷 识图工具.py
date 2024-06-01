from langchain_openai import  ChatOpenAI
import sys
import streamlit as st
from PIL import Image
import tempfile
import os
import shutil

sys.path.append('../namemodule')
from namemodule.shitumodule2 import  shiTu


#图片分类
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ''
elif st.session_state["OPENAI_API_KEY"] != '':
    chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"],
                                         openai_api_base="https://api.aigc369.com/v1")
st.set_page_config(page_title="文档总结",layout="wide")
st.title("Too酷 :red[识图工具]")
st.subheader("🤫 识图工具 🤫")
chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"],
                                         openai_api_base="https://api.aigc369.com/v1")


def save_uploaded_files(uploaded_files, directory="../uploaded_images/"):
    # 清空保存目录函数
    def clear_upload_directory(directory):
        if os.path.exists(directory):
            shutil.rmtree(directory)
        os.makedirs(directory)

    paths = []
    clear_upload_directory(directory)  # 清空保存目录

    for uploaded_file in uploaded_files:
        file_path = os.path.join(directory, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        paths.append(file_path)
    return paths


def main():
    image_paths = []

    # 上传多张图片
    uploaded_files = st.file_uploader("选择图片", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
    if uploaded_files:
        image_paths = save_uploaded_files(uploaded_files)
    # for i, uploaded_file in enumerate(uploaded_files):
    #     # 将文件保存到临时目录，并获取路径
    #     with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
    #         temp_file.write(uploaded_file.getbuffer())
    #         temp_file_path = temp_file.name
    #         # image_paths.append(temp_file_path)
    #         st.session_state["save_image"].append(temp_file_path)
    #         image_paths = st.session_state["save_image"]
        search_keyword = st.text_input('✍ 文件名搜索')
        # 关键词
        search_wu = st.text_input("🤔  分类搜索")
        # if button:
            # if (search_keyword and search_wu) or image_paths:
            # 创建一个列表来保存每个上传图片的路径
        if search_keyword:
            image_paths = [f for f in image_paths if search_keyword in f]
        elif search_wu:
            print(image_paths)
                # image_paths = [image_paths + "\\" + f for f in image_paths if
                # f.endswith('.jpg') or f.endswith('.png')]
            with st.spinner("整理中..."):
                image_paths = shiTu(image_paths,search_wu)
                if not  image_paths:
                    st.info("没有找到相关图片")

            # 每行显示3张图片
        columns = st.columns(3)
        for i, uploaded_file in enumerate(image_paths):
            # 使用列布局显示图片
            with columns[i % 3]:
                # 打开并显示图片
                image = Image.open(uploaded_file)
                st.image(image, caption=f'Image {i + 1}', use_column_width=True)
        for path in image_paths:
            st.write(path)
        img_num = f'一共有{len(image_paths)}张图片'
        st.markdown(f"###### {img_num}")
    # else:
    #     st.write("请上传图片路径")
main()





