import requests
import json

'''接口地址：https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel= 
请求方式：get '''

#第一种参数保存在url地址里面
url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=18120798657"
r = requests.get(url=url)
print(r.text)
print(r.status_code)
print(r.cookies)
print(r.url)

#第二种方法，参数保存在params,是用字典格式进行保存

url1 = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm"
params = {
    "tel":"18120798657"
}

r1 = requests.get(url=url1,params=params)
print(r1.text)
print(r1.status_code)
































