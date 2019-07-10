#coding:utf8

#导入xlrd
import xlrd

#整个EXCEL工作簿缓存
workbook = None
#当前工作sheet
sheet = None
#逐行读取时的行数
rr = 0
#当前sheet的行数
f = 0

#打开EXCEL
def open_excel(srcfile):
    global workbook,sheet,r,rr

    #设置读取excel使用utf8编码
    xlrd.Book.encoding = 'utf8'
    #读取excel内容到缓存workbook
    workbook = xlrd.open_workbook(filename=srcfile)
    #选取第一个sheet页面
    sheet = workbook.sheet_by_index(0)
    #设置r为当前sheet的行数
    r = sheet.nrows
    rr = 0
    return

#逐行读取
def readline():
    global sheet,r,rr
    row = None

    #如果当前行还没到最后一行，则读取一行
    if (rr < r):

        row = sheet.row_values(rr)
        rr = rr+1


        return row


#调试
if __name__ == '__main__':
    open_excel(r'.\测试接口\http.xls')
    #循环读取excel里面所有行内容并打印出来
    for i in range(0,r):
        print(readline()[3])

