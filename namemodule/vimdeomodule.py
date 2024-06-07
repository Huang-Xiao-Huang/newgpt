import requests

def musicsgen(title,prompt):
    url = "https://api.acedata.cloud/suno/audios"

    headers = {
        "accept": "application/json",
        "authorization": "Bearer 4331b9f906cd48aca015e8417bb88ebe",
        "content-type": "application/json"
    }

    payload = {
        "prompt": prompt,
        "model": "chirp-v2-xxl-alpha",
        "lyric": "",
        "title": title,
        'custom':False
    }
    response = requests.post(url, json=payload, headers=headers)
    result_music = response.json()["data"][0]["audio_url"]
    result_video  = response.json()["data"][0]["video_url"]
    geci = response.json()["data"][0]["lyric"]
    print(result_music,result_video,geci)
    return  result_music,result_video,geci
# musicsgen('happy','happy a boy')
