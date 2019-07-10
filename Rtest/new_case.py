#encoding = utf-8
from Rtest import Http
from Rtest import reader,writer



#准备读取excel
reader.open_excel(r'.\测试接口\http.xls')
#准备写入excelb 
writer.copy_open(r'.\测试接口\http.xls',r'.\测试接口\http2.xls')

#执行用例的方法
def run(line):
    #调用post关键字发送post请求
    if line[3]=="post":
        Http.post(line[4],line[5])
        return
    # 调用断言
    if line[3] == "assertequals":
        Http.asser_equals(line[4],line[5])
        return
    # # 调用addheader信息头
    # if line[3] == "addheader":
    #     Http.add_header(line[4], line[5])
    #     return




#使用for循环逐行读取
reader.readline()
for i in range(1,reader.r):
    line = reader.readline()
    print(line)
    if len(line[0]) > 2 or len(line[1]) > 2:
        #如果是分组信息，我们就不去执行
        pass
    else:
        #执行接口用例
        run(line)

#保存结果
writer.save_close()