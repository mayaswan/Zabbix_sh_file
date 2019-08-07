#!/usr/bin/python3
# vim: set fileencoding=utf8
#
# authenticate with zabbix api server, and retrieve monitored hosts
# specification : https://www.zabbix.com/documentation/1.8/api
#
# $ python zabbix_api.py
import requests
from pprint import pprint
import json
import time 

ZABIX_ROOT = 'http://192.168.120.104/zabbix'
url = ZABIX_ROOT + '/api_jsonrpc.php'
while True:
########################################
# user.login
########################################
        payload = {
            "jsonrpc" : "2.0",
            "method" : "user.login",
            "params": {
              'user': "Admin",
              'password':"zabbix",
            },
            "auth" : None,
            "id" : 0,
        }
        headers = {
            'content-type': 'application/json',
        }
        res  = requests.post(url, data=json.dumps(payload), headers=headers)
        res = res.json()
        #print 'user.login response'
        pprint(res)

        ########################################
        # host.get
        ########################################
        payload = {
            "jsonrpc" : "2.0",
            "method" : "host.get",
            "params": {
              'output': [
                  'hostid',
                  'name'],
            },
            "auth" : res['result'],
            "id" : 1,
        }
        res2 = requests.post(url, data=json.dumps(payload), headers=headers)
        res2 = res2.json()
        #print 'host.get response'
        pprint(res2)
        ########################################
        # item.get
        ########################################
        payload = {
            "jsonrpc": "2.0",
            "method": "item.get",
            "params": {
                "output": "extend",
                "hostids": "10299",
                "search": {
                    "key_1": ""
                },
                "sortfield": "name"
            },
            "auth": res['result'],
            "id": 2
        }
        res3 = requests.post(url, data=json.dumps(payload), headers=headers)
        res3 = res3.json()
        #print 'host.get response'
        pprint(res3)
        webhook = "https://skservice.tech/unittest/log/log.php"
        res3 = requests.post(webhook, data=json.dumps(res3), headers=headers)
        time.sleep(5)
