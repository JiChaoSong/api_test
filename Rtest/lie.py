#conding:utf8

from Rtest import Http
import unittest,random


class case(unittest.TestCase):
        password = {'username':'15972184400','password':'919D8575268AAABA35313D12023EC883'}

        def test_testfun(self):
            #登录接口
            Http.post('http://test.api.ececloud.cn/organize/person/login','username=15972184400&password=919D8575268AAABA35313D12023EC883')
            # 添加断言
            Http.asser_equals('code', '20000')
            #信息头
            Http.add_header('token',Http.json_paser())
            #任务列表
            Http.post('http://test.api.ececloud.cn/organize/mission/list','')
            #随便
            Http.post('http://test.api.ececloud.cn/organize/person/info','')
            #问题列表
            Http.post('http://test.api.ececloud.cn/organize/issue/list','')
            #教案列表
            Http.post('http://test.api.ececloud.cn/organize/tPActivity/list','')



        def test_bos(self):
            for name in range(1):
                namelist = ["王力宏", "谢霆锋", "刘德华", "流口水", "林俊杰", "周杰棍", "双杰伦", "李小龙", "王大拿", "谢大脚",
                            "谢广坤", "刘能", "赵四", "三毛", "洪金宝"]
                usernames = random.choice(namelist)
            #超级后台登录
            Http.post('http://pre.api.ececloud.cn/admin/admin/login','username=admin&password=E10ADC3949BA59ABBE56E057F20F883E')
            # 信息头
            Http.add_header('', Http.json_paser())
            #服务市场-添加培训
            #Http.post('http://pre.api.ececloud.cn/admin/educationModule/add',{'name': usernames,'teamId': 5,'summary': 'dfasdf','images': [],'phases': '[{"phaseId":174}]','effectivityDay': 30,'day': 1,'price': 100,'putAway': 1})
            #订单管理-详情
            Http.post('http://pre.api.ececloud.cn/admin/educationOrder/info','educationOrderId=19')
            # 添加断言
            Http.asser_equals('code', '20000')
            #培训管理列表
            Http.post('http://pre.api.ececloud.cn/admin/educationModule/list',{'page':1,'size':10,'name':'','teamId':'','fromTime':'','toTime':''})
            #培训管理下/上架
            i = random.randint(0,1)
            Http.post('http://pre.api.ececloud.cn/admin/educationModule/edit',{'educationModuleId':'163','putAway':i})


if __name__ == '__main__':
    unittest.main