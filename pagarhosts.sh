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
      "method": "host.get",
      "params": {
          "output": [
              "hostid",
              "host"
        ]
    },
    "auth": "'$TOKEN'",
    "id":1
  }
  '
  curl -s -X POST -H "$HEADER" -d "$JSON" "$URL" | python -mjson.tool
  
  }
  pagarhosts

