import json
import requests
from spider.base import Base
from spider import access_token

class Price(Base):

    def __get_quote_id(self, token, product_id, ppvIds):

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

        print(type(product_id), type(ppvIds))

        # 请求体
        body = {
            "productId": product_id,
            "ppvIds": ppvIds
        }

        try:
            result = requests.post(url, headers=headers, data=json.dumps(body))
            result = json.loads(result.text)

            code = result['code']
            data = result['data']
            resultMessage = result['resultMessage']
            if code == 200:

                # 获取机型
                list_link_option = self.db.get_link_options_pid(1, product_id, 1)

                str_options = ""
                for s_id in ppvIds:
                    for dict_option in list_link_option:
                        answer_id = dict_option['answer_id']
                        answer_name = dict_option['answer_name']
                        if s_id == answer_id:
                            str_options += answer_name+" "
                            pass
                        pass
                    pass

                price = data['price']
                print('询价成功[√] >> price: %s' % price, str_options)
            else:
                print('询价失败[X] >>  code: %s, message: %s' % (code, resultMessage))
            pass
        except BaseException as e:
            print('询价异常 >> e : ', e)
            pass
        pass

    def get_all_price(self):

        product_id = 25827
        ppvIds = [2014,3987,2072,2453,6437,2026,2067,2100,2114,2118,2124,2045,2104,2106,2108,2129,2134,2808,3168,5300,6947,6950,6982]

        # 初始化token
        cls_token = access_token.AccessToken()
        dict_access_token = cls_token._get_token()

        token = dict_access_token['token']


        for i in range(100):
            self.__get_quote_id(token, product_id, ppvIds)

        pass

