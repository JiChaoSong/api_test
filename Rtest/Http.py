#coding:utf-8

import requests
import json
from Rtest import reader,writer
#建立一个会话
session = requests.session()

#保存请求的结果
response = ''

#保存解析后的json字典
json_res = {}

#信息头
header = {'Content-Type': 'application/x-www-form-urlencoded', 'apptype': '100', 'clienttype': '100', 'root': '241',
          'accesstoken': '4e2c1ef2-40f2-469f-80b8-2ecb737c334aPQGydH-1560240509348'}


#调用post请求的关键字
def post(url,param):
    global session,response

    # #如果参数不为空，就处理为字典
    #
    params = {}
    if len(param) > 1:
        p = param.split('&')
        print(p)
        for pp in p :
            ppp = pp.split('=')
            params[ppp[0]] = ppp[1]


    #调用post发送请求
    res = session.post(url, data=params, verify=False, timeout=10,headers=header)
    response = res.content.decode('utf8')
    code = res.json()['code']
    #print(res.json()['code'])
    if 20000 != code:
         print('接口失败')
         writer.write(reader.rr - 1, 6, 'Fail')
         writer.write(reader.rr - 1, 7, response)
    else:
         print('接口成功')
         writer.write(reader.rr-1,6,'Pass')
         writer.write(reader.rr-1,7,response)
    print(response)
    # print(session.headers)


    #把结果解析为字典
#     json_paser()
#
# #json字符串解析
# def json_paser():
#     global json_res
#     #把json字符串解析为字典
#     json_res  =  json.loads(response)
#     print(json_res['data']['accesstoken'])



# #添加键值对到请求头里面
# def add_header(hkey,jkey):
#     # 全局信息头
#     hd = {'Content-Type': 'application/x-www-form-urlencoded', 'apptype': '100', 'clienttype': '100', 'root': '241'}
#     global json_res,session
#     #print(session.headers)
#     # 把token加入到header里边去
#     hd['accesstoken'] = json_res['data']['accesstoken']
#     session.headers = hd
#     writer.write(reader.rr - 1, 6, 'Pass')
#     writer.write(reader.rr - 1, 7, hd)
#     print(session.headers)


#添加断言
def asser_equals(key,value):
    global json_res
    try:
        if json_res[key] == value:
            print('Pass',json_res[key])
            writer.write(reader.rr - 1, 6, 'Pass')
            writer.write(reader.rr - 1, 7, json_res[key])
        else:
            print('Fail',json_res[key])
            writer.write(reader.rr - 1, 6, 'Fail')
            writer.write(reader.rr - 1, 7, json_res[key])
    except:
        code = json.loads(response)
        print(code['code'])

        if 20000 != code['code']:
            writer.write(reader.rr - 1, 6, 'Fail')
            writer.write(reader.rr - 1, 7, code['code'])
        else:
            writer.write(reader.rr - 1, 6, 'Pass')
            writer.write(reader.rr - 1, 7, code['code'])

