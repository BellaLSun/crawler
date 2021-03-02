# -*- coding:utf-8 -*-
import requests
import math
import pandas as pd
import time

def get_json(url,num):
    '''''从网页获取JSON,使用POST请求,加上头部信息'''
    my_headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'Host':'www.lagou.com',
            'Referer':'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput=',
            'X-Anit-Forge-Code':'0',
            'X-Anit-Forge-Token': 'None',
            'X-Requested-With':'XMLHttpRequest',
            'Referer': 'https://www.lagou.com/jobs/list_Java/p-city_2?&cl=false&fromSearch=true&labelWords=&suginput=',
            'Cookie': 'user_trace_token=20201203110457-06470aa1-cdc1-49be-9c05-2e35f57875b7; LGUID=20201203110458-3a8c98ff-037f-403b-a4a2-cd19e9927343; LG_LOGIN_USER_ID=6d723ec0cfc5d1124c0b4c55dfd0f04efa4e40832e9f3a0015e883bd937f8553; LG_HAS_LOGIN=1; smidV2=2020121500351227d61d35e98ad11e4eebef51f6432e1000341bfcb9f2d98b0; EDUJSESSIONID=ABAAAECABCAAACDA8BED9E19C526F94BA0246D2AE5EEE8A; sensorsdata2015session=%7B%7D; JSESSIONID=ABAAABAABAGABFA2F9C17F818C2E7EE72AEAE292CBD2414; _ga=GA1.2.138990169.1613665772; _putrc=FB7DCA59AE03410C123F89F2B170EADC; login=true; WEBTJ-ID=20210219%E4%B8%8A%E5%8D%8812:30:32003032-177b5fa8db30-0a7d3103695e62-33657309-1764000-177b5fa8db41bd; unick=%E8%A3%B4%E7%A5%BA; RECOMMEND_TIP=true; index_location_city=%E5%8C%97%E4%BA%AC; PRE_UTM=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; _gid=GA1.2.2139944469.1614498790; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1613665772,1614498790; LGSID=20210228155310-244b36ea-cb4d-4eac-84c7-98f8b45ab35c; PRE_HOST=www.google.com; PRE_SITE=https%3A%2F%2Fwww.google.com%2F; TG-TRACK-CODE=index_navigation; __lg_stoken__=410b1ea4337e35a5bd55834826529eca3ffd49cc5bf004a4717fd66c0e2d3046d348562b9b4ea1d5a224daa82d70ae610e1febd6929bee56cab180d088ead5a8c95cdea5292b; X_HTTP_TOKEN=759285b84e9553df3388944161be9f5fca6f0b86c4; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2220602265%22%2C%22first_id%22%3A%22176268f5c91703-08861971bf370c-18346153-1764000-176268f5c92960%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24os%22%3A%22MacOS%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2288.0.4324.182%22%7D%2C%22%24device_id%22%3A%22176268f5c91703-08861971bf370c-18346153-1764000-176268f5c92960%22%7D; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1614498834; LGRID=20210228155354-7469f3c4-03fc-4707-a091-95ffa3a6c50f; SEARCH_ID=4e3a4937122e4051a8c01bc2e11181c3'
            }

    my_data = {
            'first': 'true',
            'pn':num,
            'kd':'数据分析'}

    res = requests.post(url, headers = my_headers, data = my_data)
    res.raise_for_status()
    res.encoding = 'utf-8'
    # 得到包含职位信息的字典
    page = res.json()
    return page


def get_page_num(count):
    '''''计算要抓取的页数'''
    # 每页15个职位,向上取整
    res = math.ceil(count/15)
    # 拉勾网最多显示30页结果
    if res > 30:
        return 30
    else:
        return res

def get_page_info(jobs_list):
    '''''对一个网页的职位信息进行解析,返回列表'''
    page_info_list = []
    for i in jobs_list:
        job_info = []
        job_info.append(i['companyFullName'])
        job_info.append(i['companyShortName'])
        job_info.append(i['companySize'])
        job_info.append(i['financeStage'])
        job_info.append(i['district'])
        job_info.append(i['positionName'])
        job_info.append(i['workYear'])
        job_info.append(i['education'])
        job_info.append(i['salary'])
        job_info.append(i['positionAdvantage'])
        page_info_list.append(job_info)
    return page_info_list

def main():
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false'
    # 先设定页数为1,获取总的职位数
    page_1 = get_json(url,1)
    print(page_1)
    total_count = page_1['content']['positionResult']['totalCount']
    num = get_page_num(total_count)
    total_info = []
    time.sleep(20)
    print('职位总数:{},页数:{}'.format(total_count,num))

    for n in range(1,num+1):
        # 对每个网页读取JSON, 获取每页数据
        page = get_json(url,n)
        jobs_list = page['content']['positionResult']['result']
        page_info = get_page_info(jobs_list)
        total_info += page_info
        print('已经抓取第{}页, 职位总数:{}'.format(n, len(total_info)))
        # 每次抓取完成后,暂停一会,防止被服务器拉黑
        time.sleep(30)
    #将总数据转化为data frame再输出
    df = pd.DataFrame(data = total_info,columns = ['公司全名','公司简称','公司规模','融资阶段','区域','职位名称','工作经验','学历要求','工资','职位福利'])
    df.to_csv('lagou_jobs.csv',index = False)
    print('已保存为csv文件.')

if __name__== "__main__":
    main()