from dominate.tags import *
from kkk import *

excel_value()
h = html()
with h.add(body()):
    h1("测试结果")
    style(
        type='text/css'
    )
    with table(border="1",cellpadding="10"):

        l = tr()
        l += th(excel_value()[0][0])
        l.add(th(excel_value()[1][0]))
        l.add(th(excel_value()[2][0]))
        l.add(th(excel_value()[3][0]))
        l.add(th(excel_value()[4][0]))
        # l.add(th(excel_value()[5][0]))
        with l:
            th(excel_value()[6][0])

        for i in range(1,len(excel_value()[0])):

            ll = tr()
            ll += td(excel_value()[0][i],width="200px",rowspan="1",style="word-wrap : break-word ")
            ll.add(td(excel_value()[1][i],width="200px",rowspan="1",style="word-wrap : break-word "))
            ll.add(td(excel_value()[2][i],width="200px",rowspan="1",style="word-wrap : break-word "))
            ll.add(td(excel_value()[3][i],width="200px",rowspan="1",style="word-wrap : break-word "))
            ll.add(td(excel_value()[4][i],width="200px",rowspan="1",style="word-wrap : break-word "))
            # ll.add(td(excel_value()[5][i],width="200px",rowspan="1",style="word-wrap : break-word "))
            with ll:
                if excel_value()[6][i] == 'Pass':
                    td(excel_value()[6][i],width="200px",rowspan="1",style="word-wrap : break-word ",bgcolor="#00FF00")

                elif excel_value()[6][i] == 'Fail':
                    td(excel_value()[6][i], width="200px", rowspan="1", style="word-wrap : break-word ",
                       bgcolor="#FF0000")

                else:
                    td(excel_value()[6][i], width="200px", rowspan="1", style="word-wrap : break-word ",
                       bgcolor="#FFFFFF")

with open('testresult.html','w') as f:
    f.write(h.render())
