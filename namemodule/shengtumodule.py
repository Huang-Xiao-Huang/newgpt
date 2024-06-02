import requests
import re
#😚
def shTu(client,number,Prompt):
    image_data = []
    # 使用 DALL-E 生成图像
    for i in range(number):
        response = client.images.generate(
            model="dall-e-2",
            prompt=Prompt,
            size="512x512",
        )
        # 获取生成的图像 URL
        image_url = response.data[0].url
        image_data.append(image_url)
    return image_data
            # print("Generated image:", image_url)

def shiMID(client,number,Prompt):
    image_data = []
    url = "https://api.acedata.cloud/midjourney/imagine"
    headers = {
        "accept": "application/json",
        "authorization": "Bearer e6d22c7afb4441f3b17a0a4ae5919079",
        "content-type": "application/json"
    }
    for i in range(number):
        payload = {
            "mode": "fast",
            "translation": True,
            "prompt": Prompt
        }

        response = requests.post(url, json=payload, headers=headers).text
        derw = re.compile('"image_url":"(.*?)"', re.S)
        print(derw)
        iamge_url = re.findall(derw, response)[0]
        # print(e)
        image_data.append(iamge_url)
    return  image_data
