#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header


mail_adr = {
    '主管':'jiawei.ruan@zhihan.ltd',
    'test':'306333246@qq.com',
    '宋纪超':'jichaosong@outlook.com'
}
# 第三方 SMTP 服务
mail_host = "smtp.exmail.qq.com"  # 设置服务器
mail_user = "jichao.song@zhihan.ltd"  # 用户名
mail_pass = "Sjch1994@"  # 口令

sender = 'jichao.song@zhihan.ltd'
receivers = [mail_adr['test']]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 读取html文件内容
f = open(r'.\testresult.html','rb')
mail_body = f.read()
f.close()

# mail_msg = """
# <table border="1">
#   <tr>
#     <th>模块</th>
#     <th>分组</th>
#     <th>用例名称</th>
#     <th>关键字</th>
#     <th>接口地址</th>
#     <th>参数</th>
#     <th>执行状态</th>
#   </tr>
#   <tr>
#     <td>用户模块</td>
#     <td>	   </td>
#     <td>登录</td>
#     <td>post</td>
#     <td>http://test.api.ececloud.cn/organize/person/login</td>
#     <td>username=15972184400&password=919D8575268AAABA35313D12023EC883</td>
#     <td style="color:#009933">Pass</td>
#     # <td style="word-wrap:break-word;word-break:break-all;" width="100px">Pass</td>
#   </tr>
# </table>
# """

message = MIMEText(mail_body, 'html', 'GBK')
message['From'] = Header("宋纪超", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = '测试结果'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")

except smtplib.SMTPException:
    print("Error: 无法发送邮件")
