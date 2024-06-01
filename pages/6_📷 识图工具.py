from langchain_openai import  ChatOpenAI
import streamlit as st
import os
from PIL import Image
import sys

sys.path.append('../namemodule')
from namemodule.shitumodule import  shiTu



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


def main():
    # st.write("""
    # <style>
    # /* 自定义图片样式 */
    # .stImage {
    #   background-color:red;
    # }
    # </style>
    # """, unsafe_allow_html=True)
    # 选择要读取的文件夹
    folder_path = st.text_input('📷 输入文件夹路径')
    # folder_path = rf'{folder_path}'
    print(folder_path)
    # 文件名字分类
    search_keyword = st.text_input('✍ 文件名搜索')
    # 关键词
    search_wu =  st.text_input("🤔  分类搜索")

    button = st.button("🆗  确定")

    if (search_keyword and search_wu) or folder_path :
        # 读取文件夹中的文件
        # try:
        image_files = os.listdir(folder_path)
        print(image_files)
        image_files = [f for f in image_files if f.endswith('.jpg') or f.endswith('.png')]
        if len(image_files) > 0:
            # 如果存在搜索关键词，只显示包含关键词的图片。
            if search_keyword:
                image_files = [f for f in image_files if search_keyword in f]
            elif search_wu:
                image_files = [folder_path + "\\" + f for f in image_files if
                               f.endswith('.jpg') or f.endswith('.png')]
                with st.spinner("整理中..."):
                    image_files = shiTu(image_files,search_wu)
                    if not  image_files:
                        st.info("没有找到相关图片")
                    # print(image_files)


            # 将图像文件分为三列
            col1, col2, col3 = st.columns(3)
            # 显示文件夹中的图像
            for i, image_file in enumerate(image_files):
                image_path = os.path.join(folder_path, image_file)
                with open(image_path, 'rb') as f:
                    img = Image.open(f)
                    if i % 3 == 0:
                        with col1:
                            st.image(img, caption=image_file, use_column_width=True)

                            # st.write(f'<img src=f"data:image/jpeg;base64,{img}" class="custom-image">')
                    elif i % 3 == 1:
                        with col2:
                            # st.write(f'<img src=f"data:image/jpeg;base64,{img}" class="custom-image">')
                            col2.image(img, caption=image_file, use_column_width=True)
                    else:
                        with col3:
                            # st.write(f'<img src=f"data:image/jpeg;base64,{img}" class="custom-image">')
                            col3.image(img, caption=image_file, use_column_width=True)
                            # col3.write(
                            #     f'<div class="column"><img src="data:image/jpeg;base64,{img}" class="custom-image"></div>',
                            #     unsafe_allow_html=True)

            img_num = f'一共有{len(image_files)}张图片'
            st.markdown(f"###### {img_num}")

        # except:pass
    else:
        st.write('请输入文件夹路径。')

main()




# 显示图片并应用样式
# st.image("your_image.jpg", caption="Original Image", use_column_width=True)