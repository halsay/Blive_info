import time
import requests
import json

UID = 591844
RECORD_COUNT = 5

url = f"https://api.danmaku.suki.club/api/search/user/detail?uid={UID}&pagesize={RECORD_COUNT}"

payload = {}
headers = {
   'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)'
}
proxy = {
    # 'http':'http://127.0.0.1:10809',
    # 'https':'http://127.0.0.1:10809',
}

action_type = ['普通弹幕','礼物','上舰','SC','进入直播间']

response = requests.get(url, headers=headers, timeout=50, proxies=proxy)
if response.status_code == 200:
    res = json.loads(response.text)
    user_name = res['data']['data'][0]['danmakus'][0]['name']
    print(f'User Name: {user_name}')

    for d in res['data']['data']:
        liver = d['channel']['name']
        for da in d['danmakus']:
            action = da['type']
            ac = action_type[action]
            cur_time = da["sendDate"]
            # print(cur_time)
            date_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(cur_time))
            if ac == '普通弹幕' or ac == 'SC':
                message = da['message']
                print(f'直播间：{liver}, {ac}: {message}, 时间: {date_time}')
            elif ac == '进入直播间':
                print(f'进入直播间: {liver}, 直播标题: {d["live"]["title"]}, 时间: {date_time}')
            else:
                print(f'直播间：{liver}, {ac}, 时间: {date_time}')
        print('================================================')
