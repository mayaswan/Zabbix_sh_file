#!/usr/bin/python3
import requests
import json
import urllib.parse
import sys
msgzbx = sys.argv
LINE_ACCESS_TOKEN="YBe6CGrkmgyzzIvrM3iHAMEVxrbDyr0HUL0oVZfjrTS"
url = "https://notify-api.line.me/api/notify"
message = msgzbx[2]+msgzbx[3]
msg = urllib.parse.urlencode({"message":message})
LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
session = requests.Session()
a=session.post(url, headers=LINE_HEADERS, data=msg)
print(a.text)

