import json
import requests

# url = 'http://bijia.huishoubao.com/han/api/price'
#
# headers = {
#     "Content-Type" : "application/json"
# }
#
# body = {
#     "options": "7399;7396;2014;2903;2072;2100;2125;2120;2114;2067;3168;2129;2134;6982;2045;5300;2104;2108;6947;2808;6949",
#     "pid": "27639",
#     "channelId": "1",
#     "multipleStr":""
# }
#
# result = requests.post(url, headers=headers, data=json.dumps(body))
# result = json.loads(result.text)
# print('result: ', result)


# url = 'https://neon.aihuishou.com/fenqile/fenqile-api/oauth/token?grant_type=client_credentials&client_id=fenqile&client_secret=RJFJ2TLWRRb4j9Km'
#
# headers = {
#     "Host": "neon.aihuishou.com",
#     "App-Slug": "fenqile",
#     # "Cookie": "sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216c847404d61b7-034e69f72f8c448-1375277d-250125-16c847404d73c2%22%2C%22%24device_id%22%3A%2216c847404d61b7-034e69f72f8c448-1375277d-250125-16c847404d73c2%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22https%3A%2F%2Fchannel.m.fenqile.com%2Fcategory%2Findex.html%22%2C%22%24latest_referrer_host%22%3A%22channel.m.fenqile.com%22%2C%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; gr_user_id=179115ee-68af-4b8a-8e8a-1ebd37533a17; fenqile_sid=b9945f23-af67-4e03-aa93-36dae56b9301; acw_tc=76b20fea15655903728481703e6c8deaea8cab92942be12ab4ed35946a2c1c; grwng_uid=682d426e-905c-4464-b74c-dd5d36245beb",
#     "Connection": "keep-alive",
#     "Accept": "application/json, text/plain, */*",
#     "sid": "b9945f23-af67-4e03-aa93-36dae56b9301",
#     "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;fenqile_ios_5.1.1;couldShowHeader_1;wv_i_v2",
#     "Referer": "https://neon.aihuishou.com/fenqile/",
#     "Accept-Language": "zh-cn",
#     "Accept-Encoding": "br, gzip, deflate"
# }
#
# result = requests.get(url, headers=headers)
# result = json.loads(result.text)
# print(result)

url = 'http://123.207.53.181:5000/xianyu/random'

result = requests.get(url)
print('>>>>> : ', type(result.text), result)
result = json.loads(result.text)
print(result)
















