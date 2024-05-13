
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