
# encoding:utf-8

import requests
import base64

'''
通用物体和场景识别
'''

# 识别工具
def shiTu(image_list, keyword):
    da_list = []
    for r_image in image_list:
        url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=2sG6h2Kq8oNRIefF8S0nZQKq&client_secret=wSRkG5TO6IK2WDVZxfDjaxhTRyxDoesL"

        payload = ""
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        access_token = response.json()["access_token"]
        print(access_token)

        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"
        # # 二进制方式打开图片文件
        f = open(r_image , 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        access_token = access_token
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            print(response.json()["result"][0]["keyword"])
            data_r = response.json()["result"][0]["keyword"]
            if keyword in data_r:
                    dd = r_image.split("\\")[-1]
                    da_list.append(dd)
            else:
                pass
                # print(da_list)
    return da_list

