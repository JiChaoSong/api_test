import xlrd
sheet1_nrows = []
sheet1_ncols = []
# cols_value = globals()
def excel_value():
    cols_value = []
    # 打开文件
    workbook = xlrd.open_workbook(r'.\测试接口\http2.xls')

    # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始
    sheet1_nrows = sheet1.nrows
    sheet1_ncols.append(sheet1.ncols)
    #获取第i行内容
    for i in range(0, sheet1.ncols):

        cols = sheet1.col_values(i)

        cols_i = cols

        cols_value.append(cols_i)



    return cols_value


# print(excel_value()[6][2])
