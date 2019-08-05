#!/bin/sh
URL='http://192.168.120.104/zabbix/api_jsonrpc.php'
HEADER='Content-Type:application/json'

USER='"Admin"'
PASS='"zabbix"'

autenticacao()
{
  JSON='
  {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": '$USER',
        "password": '$PASS'
      },
      "id": 0,
      "auth":nall
    }
    '
    curl -s -X POST -H "$HEADER" -d "$JSON" "$URL"  | cut -d '"' -f8
  }
  TOKEN=$(autenticacao)
  
 pagarhosts()
 {
    JSON='
  
  {
    "jsonrpc": "2.0",
    "method": "item.create",
    "params": {
        "name": "Free disk space on $1",
        "key_": "vfs.fs.size[/home/joe/,free]",
        "hostid": "30074",
        "type": 0,
        "value_type": 3,
        "interfaceid": "30084",
        "applications": [
            "609",
            "610"
        ],
        "delay": 30
    },
    "auth": "038e1d7b1735c6a5436ee9eae095879e",
    "id": 1
}
  
  '
  curl -s -X POST -H "$HEADER" -d "$JSON" "$URL" | python -mjson.tool
  
  }
  pagarhosts
