from openai import OpenAI
import streamlit as st

import sys
sys.path.append('../namemodule')
from namemodule import shengtumodule


def xianshitu(image_data):
    '''
    显示图片
    '''
    images_per_row = 5
    image_spacing = 5
    #显示多张图片，每行最多5张
    for i in range(0, len(image_data), images_per_row):
        row_images = image_data[i:i + images_per_row]  # 获取当前行的图片列表
        row_captions = [f"Image {i + 1}" for i in range(len(row_images))]  # 设置当前行的图片标题
        st.divider()
        for img, caption in zip(row_images, row_captions):
            st.image(img, caption=caption, width=150)  # 显示当前行的图片
            # 添加下载按钮
            download_button_str = f"Download {caption}"



st.set_page_config(page_title="以文生图",layout="wide")
st.title("Too酷 :red[以文生图]")
st.subheader(":red[🖼] 智能图片生成")
st.write("你想要的图片这里都有")
st.divider() #分割线

#如果openai没有在会话中(会话的作用是存储一些历史信息),则设置为空
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ''
    st.warning("请在首页输入OPENAI_API_KEY")
elif st.session_state["OPENAI_API_KEY"] != '':
       client = OpenAI(api_key = st.session_state["OPENAI_API_KEY"],
                                     base_url = "https://api.aigc369.com/v1")

# client = OpenAI(api_key = st.session_state["OPENAI_API_KEY"],
#                          base_url = "https://api.aigc369.com/v1")\



model_image =  st.multiselect(
    '选择模型与工具',
    ["dall-e-2", "midjourney"],
    ["dall-e-2"]
)
options = st.multiselect(
    '请你选择生成图像的风格',
    ["插画风格", "黑白摄影风格", "自然风景风格",
     "艺术风格", "明亮生动风格"],
    ["艺术风格"]
)

st.write('你选择的是🤫:', options)
# print(options)

number = st.number_input('🗒 生成的图片个数', value=1, min_value=1, max_value=4)

Prompt12 = st.text_input("🎨 请输入图片描述")
bttons = st.button("💾按钮")

Prompt = f"你现在是一名著名画家,请画一幅{Prompt12}画,要求{options[0]}风格"
print(Prompt)

if bttons  and  st.session_state["OPENAI_API_KEY"]:
    # try:
    if model_image[0] == "dall-e-2":
        with st.spinner("⌛ 图片生成中..."):
            image_data = shengtumodule.shTu(client,number,Prompt)
            xianshitu(image_data)
    elif model_image[0] == "midjourney":
        with st.spinner("⌛ 图片生成中..."):
            image_data = shengtumodule.shiMID('hello',number,Prompt)
            xianshitu(image_data)


                    # st.download_button(label=download_button_str, data=img, file_name=f"{caption}.jpg",
                    #                    mime="image/jpeg")

    # except:
    #     st.warning("无法生成图片")
    #     st.stop()


