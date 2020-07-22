import requests
import random
import re
import queue
import threading
import csv
import json
from pprint import  pprint

# user_agent列表
user_agent_list = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36'
]

# referer列表
referer_list = [
    'http://fund.eastmoney.com/110022.html',
    'http://fund.eastmoney.com/110023.html',
    'http://fund.eastmoney.com/110024.html',
    'http://fund.eastmoney.com/110025.html'
]

def get_fund_code():
    # 获取一个随机user_agent和Referer
    header = {'User-Agent': random.choice(user_agent_list),
              'Referer': random.choice(referer_list)
    }

    # 访问网页接口
    req = requests.get('http://fund.eastmoney.com/js/fundcode_search.js', timeout=5, headers=header)

    #获取所有基金代码
    fund_code = req.content.decode()
    # pprint(fund_code)
    fund_code = fund_code.replace("﻿var r = [","").replace("];","")
    # # 正则批量提取
    fund_code = re.findall(r"[\[](.*?)[\]]", fund_code)
    # fund_code = re.findall(r"000001(.*?)HH", fund_code)
    # 对每行数据进行处理，并存储到fund_code_list列表中
    fund_code_list = []
    for sub_data in fund_code:
        data = sub_data.replace("\"","").replace("'","")
        data_list = data.split(",")
        fund_code_list.append(data_list)
    print(fund_code_list)
    return fund_code_list
get_fund_code()

# def get_proxy():
#     data_json = requests.get("http://proxy.1again.cc:35050/api/v1/proxy/?type=2").text
#     print(data_json)
#     # data = json.loads(data_json)
#     # print(data)
#     # return data['data']['proxy']
# get_proxy()