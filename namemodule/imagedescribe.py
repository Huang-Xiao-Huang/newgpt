from openai import OpenAI
import requests

def im_describe(img_url,api_key):
    url = "https://api.acedata.cloud/midjourney/describe"

    headers = {
        "accept": "application/json",
        "authorization": "Bearer e6d22c7afb4441f3b17a0a4ae5919079",
        "content-type": "application/json"
    }

    payload = {
        "image_url": img_url
    }

    response = requests.post(url, json=payload, headers=headers)
    # print(response.text)
    descibr_word = response.json()['descriptions'][0]
    # return response.json()['descriptions'][0]
    # 将英文翻译成中文
    client = OpenAI(api_key  = api_key,
                                 base_url="https://api.aigc369.com/v1")
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": f"请将下列句子翻译成中文{descibr_word}"}
      ]
    )
    return response.choices[0].message.content