#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: luckscript
@contact: luckscript@gmail.com
@site: http://www.msun.com
@file: mob_sms.py
@time: 17/3/16 15:12
"""

import requests

class MobSMS:
    def __init__(self, appkey):
        self.appkey = appkey
        self.server_verify_url = 'https://api.sms.mob.com/sms/verify'
        self.webapi_send_url = 'https://xxxxxxxxxxxxxxxxxx' # 接口地址联系客服
        self.webapi_check_url = 'https://xxxxxxxxxxxxxxxxxx' # 接口地址联系客服

    # 短信服务端验证接口
    def verify_sms_code(self, zone, phone, code, debug=False):
        if debug:
            return 200

        data = {'appkey': self.appkey, 'phone': phone, 'zone': zone, 'code': code}
        req = requests.post(self.server_verify_url, data=data, verify=False)
        if req.status_code == 200:
            j = req.json()
            return j.get('status', 500)

        return 500

    # Web-Api验证码发送接口
    def webapi_send_code(self, zone, phone, debug=False):
        if debug:
            return 200

        data = {'appkey': self.appkey, 'phone': phone, 'zone': zone}
        req = requests.post(self.webapi_send_url, data=data, verify=False)
        if req.status_code == 200:
            j = req.json()
            return j.get('status', 500)

        return 500

    # Web-Api验证码校验接口
    def webapi_check_code(self, zone, phone, code, debug=False):
        if debug:
            return 200

        data = {'appkey': self.appkey, 'phone': phone, 'zone': zone, 'code': code}
        req = requests.post(self.webapi_check_url, data=data, verify=False)
        if req.status_code == 200:
            j = req.json()
            return j.get('status', 500)

        return 500


if __name__ == '__main__':
    mobsms = MobSMS('xxxxxxxxxxxxxxxxxx') # 修改为您的appkey.在官网（http://www.mob.com)登录后获取,接口地址联系客服
    print mobsms.verify_sms_code(86, 13900000000, '1234')