import sys
import json
import requests

def get_fql_price(token, product_id, ppvIds):

    # 获取路由
    domain = 'https://neon.aihuishou.com'
    open_api = 'fenqile/fenqile-api'

    # 请求链接
    url = '{}/{}/{}'.format(domain, open_api, 'inquiry')

    # 设置请求头
    headers = {
        "Host": "neon.aihuishou.com",
        "App-Slug": "fenqile",
        "Accept-Encoding": "br, gzip, deflate",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "sid": "b9945f23-af67-4e03-aa93-36dae56b9301",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;fenqile_ios_5.1.1;couldShowHeader_1;wv_i_v2",
        "Referer": "{}/fenqile/product/detail/{}".format(domain, product_id),
        "Accept-Language": "zh-cn",
        "Content-Type": "application/json;charset=UTF-8",
        "Content-Length": "56",
        "Origin": "https://neon.aihuishou.com",
        "Authorization": "bearer " + token
    }

    # 请求体
    body = {
        "productId": product_id,
        "ppvIds": ppvIds
    }

    price = 0

    try:
        result = requests.post(url, headers=headers, data=json.dumps(body))
        result = json.loads(result.text)

        code = result['code']
        data = result['data']
        if code == 200:
            price = data['price']

        return price
    except :
        return price
    pass


if __name__ == '__main__':

    # token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsib3BlbmFwaSJdLCJzY29wZSI6WyJmZW5xaWxlIl0sImV4cCI6MTU2NjQ4ODk2NSwiYXV0aG9yaXRpZXMiOlsiRlFMX00iXSwianRpIjoiZjE4ZWE5NDctZjQyZS00NDk3LWFlYTQtNWVjYzIzNzgzYWJmIiwiY2xpZW50X2lkIjoiZmVucWlsZSJ9.oeOfodcGepLz4xH-HIwCLp1PZ4-MBUPtyCvelaDuF2M"
    # product_Id = 25827
    # ppvIds = [2014,3987,2072,2453,6437,2026,2067,2100,2114,2118,2124,2045,2104,2106,2108,2129,2134,2808,3168,5300,6947,6950,6982]

    token = sys.argv[1]
    product_Id = sys.argv[2]
    ppvIds = sys.argv[3]

    price = get_fql_price(token, product_Id, ppvIds)
    print(price)












































