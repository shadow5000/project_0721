import requests
import json

def get_proxy():
    data_json=requests.get("http://proxy.1again.cc:35050/api/v1/proxy/?https=1").text
    print(data_json)
    data=json.loads(data_json)
    print(data['data']['proxy'])
    # return  data['data']['proxy']
proxy=get_proxy()
print(proxy)