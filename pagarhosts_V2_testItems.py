#!/usr/bin/sh
import reqeusts
import json 
resp=reqeusts.post('http://192.168.120.104/zabbix/api_jsonrpc.php')
HEADER='Content-Type:application/json'

USER = "Admin"
PASS = "zabbix"

r = resp

r = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": 'USER',
        "password": 'PASS'
    },
    "id": 1
}

