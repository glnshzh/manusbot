import http.client
import json

import requests

url=f"http://soundai.natapp1.cc/vits/genByTextList2Hash/"
headers={"uId":"478184350","token":"02e0f109-e392-4d30-8e0a-bc8efacb99ed",'Content-Type': 'application/json'}
data={
	"modelId": 20,
	"roleId": "0",
	"lang": "[ZH]",
	"textList": [
		"你好"
	]
}
req=requests.post(url,headers=headers,data=json.dumps(data))
hash_code=req.text
hashcode=req.json()['data'][0]['hashCode']
url_record=f"http://soundai.natapp1.cc/vits/getUrlByHashCode"
parms={"code":hashcode}
record=requests.get(headers=headers,url=url_record,params=parms)
while record.json()['data'][0]['url']==None:
	record = requests.get(headers=headers, url=url_record, params=parms)

print(record.text)



# conn=http.client.HTTPSConnection("petstore-demo.apifox.com")
# payload=''
# headers={
# 	'uId':'478184350',
# 	'token':'02e0f109-e392-4d30-8e0a-bc8efacb99ed',
# 	'User-Agent':'Apifox/1.0.0 (https://apifox.com)'
#
# }
# url="/vits/getUrlByHashCode?code="+hashcode
# print(url)
# conn.request("GET",url,payload,headers)
# res=conn.getresponse()
# data=res.read()
# print(data.decode("utf-8"))


# import http.client
# import json
#
# conn = http.client.HTTPSConnection("soundai.natapp1.cc")
# payload = json.dumps({
#    "modelId": 20,
#    "roleId": "0",
#    "lang": "[ZH]",
#    "textList": [
#       "啾咪~ 大家好啊！我是秋蒂啊~",
#       "一名在日本留学虚拟主播。",
#       "客户端自己来切片"
#    ]
# })
# headers = {
#    'uId': '478184350',
#    'token': '02e0f109-e392-4d30-8e0a-bc8efacb99ed',
#    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
#    'Content-Type': 'application/json'
# }
# conn.request("POST", "/vits/genByTextList2Hash", payload, headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))