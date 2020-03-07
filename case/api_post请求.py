import requests
import json


#发送post请求，2种数据请求格式
#第一种  form-data ,表单格式
#第二种 json

'''
1.注册接口:http://127.0.0.1:8000/register/
请求方式:post
请求参数:uname,pwd
2.登录接口:http://127.0.0.1:8000/student/login/
请求方式:post
请求参数:uname,pwd
'''

# url = "http://127.0.0.1:8000/register/"
# data = {
#     "uname":"zzgg",
#     "pwd":"1234"
# }
# #发送请求
# r = requests.post(url=url,data=data)
# print(r.text)


url_login = "http://127.0.0.1:8000/student/login/"
#json格式的数据，但是接口只支持data的方式提交
x = {
    "uname":"gg",
    "pwd":"1234"
}
r_login = requests.post(url=url_login,data=x)
print(r_login.text)



