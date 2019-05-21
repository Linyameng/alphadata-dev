# -*- coding: utf-8 -*-
"""
Created on 2018/10/10

@author: xing yan
"""

import requests
import time
from requests.exceptions import  RequestException


import requests
import time


class BaseHttpClient:

    loginPwd = 'qq1111'
    phoneidentify = '111111'
    txPwd = '121212'
    code = '111111'

    def __init__(self, host):
        self.host = host
        self.s = requests.Session()

    def with_request(self):
        pass

    def __call__(self, id_no, cust_name, mobile,  bank_acct):

        try:

            codes = []

            r = self.get_login_url()
            codes.append(r.status_code == requests.codes.ok)
            if 'topMenu' not in r.text:
                return r.text, "获取登录首页失败！"

            time.sleep(0.5)
            r = self.get_phone_code(id_no, mobile)
            codes.append(r.status_code == requests.codes.ok)
            if 'success' not in r.text:
                return r.text, "获取手机验证码失败！"

            time.sleep(0.5)
            r = self.post_trade_register(id_no, cust_name, mobile)
            codes.append(r.status_code == requests.codes.ok)
            if 'login.htm' not in r.text:
                return r.text, '提交开户信息失败！'

            time.sleep(0.5)
            r = self.register_bind_card_binding(bank_acct)
            codes.append(r.status_code == requests.codes.ok)
            if 'shortMsgApply' not in r.text:
                return r.text, '申请绑卡失败！'

            time.sleep(0.5)
            r = self.apply_account_bind_card_code(mobile)
            codes.append(r.status_code == requests.codes.ok)
            if 'sendSuccessful' not in r.text:
                return r.text, '申请绑定银行卡手机验证码失败！'

            time.sleep(0.5)
            r = self.valida_account_bind_card_code(mobile)
            codes.append(r.status_code == requests.codes.ok)
            if 'success' not in r.text:
                return r.text, '提交绑定银行卡手机验证码失败！'

            if False in codes:
                return False, '开户绑卡失败，{}'.format(r)
            else:
                return True, '开户绑卡成功'

        except RequestException as q:
            return False, q

        finally:
            self.s.close()

    def get_login_url(self):
        """获取登录首页."""
        return self.s.get('http://{host}:15080/trade/login/login.htm'.format(host=self.host))

    def get_phone_code(self, id_no, mobile):
        """获取手机验证码"""
        params = {
            'method': 'sendCheckPhoneUniqueMsg',
            'idNo': id_no,
            'mobile': mobile,
            'captcha': '1111',
            '_': int(time.time())
        }
        return self.s.get('http://{host}:15080/trade/common/doajaxaction.htm'.format(host=self.host), params=params)

    def post_trade_register(self, id_no, cust_name, mobile):
        """提交开户信息."""
        data = {
            'address': 'addr',
            'certNo': id_no,
            'custName': cust_name,
            'loginPwd': self.loginPwd,
            'mobile': mobile,
            'phoneidentify': self.phoneidentify,
            'reLoginPwd': self.loginPwd,
            'reTxPwd': self.txPwd,
            'txPwd': self.txPwd,
            'collectProtocolMethod': 4,
            'xieyi': 'on'
        }

        return self.s.post('http://{host}:15080/trade/register/register.htm'.format(host=self.host), data=data)

    def register_bind_card_binding(self, bank_acct):
        """绑定银行卡"""
        params = {
            'method': 'binding',
            'ajax': 'true'
        }

        data = {
            'bankAcct': bank_acct,
            'bankCode': '305',
            'cityCode': '215000',
            'cnapsNo': '305305026009',
            'provCode': '21',
            'selectVerfyType': '04'
        }
        return self.s.post('http://{host}:15080/trade/register/bindcard.htm'.format(host=self.host), params=params,
                           data=data)

    def apply_account_bind_card_code(self, mobile):
        """绑定银行卡-申请短信验证码"""
        params = {
            'method': 'shortMsgApply',
            'ajax': 'true'
        }

        data = {
            'phoneNo': mobile
        }
        return self.s.post('http://{host}:15080/trade/account/bindcard.htm'.format(host=self.host), params=params,
                           data=data)

    def valida_account_bind_card_code(self, mobile):
        """绑定银行卡-提交手机短信验证码"""
        params = {
            'method': 'shortMsgValidation',
            'ajax': 'true'
        }

        data = {
            'code': self.code,
            'phoneNo': mobile
        }
        return self.s.post('http://{host}:15080/trade/account/bindcard.htm'.format(host=self.host), params=params,
                           data=data)


# fabr = utils.Fabricate()
#
#
#
# idNo, custName, mobile,  bankAcct = fabr.cust_id(), fabr.cust_name(), fabr.phone_number(), fabr.bank_number()
#
# print(idNo, custName, mobile,  bankAcct)
#
# client = BaseHttpClient(host='192.168.221.123')
# client(idNo, custName, mobile,  bankAcct)

