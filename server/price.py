import json
import requests
from spider.base import Base

class Price(Base):

    def __get_quote_id(self, product_id, ppvIds):

        # 获取路由
        domain = self.cfg.get_cfg_value("ROUTE", "domain")
        open_api = self.cfg.get_cfg_value("ROUTE", "open_api_url")

        # 请求链接
        url = '{}/{}/{}'.format(domain, open_api, 'inquiry')

        # 设置请求头
        headers = {
            "Host": self.cfg.get_cfg_value("HEADERS", "Host"),
            "App-Slug": self.cfg.get_cfg_value("HEADERS", "App-Slug"),
            "Accept-Encoding": self.cfg.get_cfg_value("HEADERS", "Accept-Encoding"),
            "Connection": self.cfg.get_cfg_value("HEADERS", "Connection"),
            "Accept": self.cfg.get_cfg_value("HEADERS", "Accept"),
            "sid": self.cfg.get_cfg_value("HEADERS", "sid"),
            "User-Agent": self.cfg.get_cfg_value("HEADERS", "User-Agent"),
            "Referer": "{}/fenqile/product/detail/{}".format(domain, product_id),
            "Accept-Language": self.cfg.get_cfg_value("HEADERS", "Accept-Language"),
            "Content-Type": self.cfg.get_cfg_value("HEADERS", "Content-Type"),
            "Content-Length": self.cfg.get_cfg_value("HEADERS", "Content-Length"),
            "Origin": self.cfg.get_cfg_value("HEADERS", "Origin"),
            "Cookie": self.cfg.get_cfg_value("HEADERS", "Cookie"),
            "Authorization": self.cfg.get_cfg_value("HEADERS", "Authorization"),
        }

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
                print('list_link_option: ', list_link_option)

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

                print('str_options : ', str_options)

                price = data['price']
                print('询价成功[√] >> price: %s' % price)

                pass
            else:
                print('询价失败[X] >>  code: %s, message: %s' % (code, resultMessage))
                pass
            pass
        except BaseException as e:
            print('询价异常 >> e : ', e)
            pass
        pass

    def get_all_price(self):

        product_id = 25827
        ppvIds = [2014,3987,2072,2453,6437,2026,2067,2100,2114,2118,2124,2045,2104,2106,2108,2129,2134,2808,3168,5300,6947,6950,6982]

        self.__get_quote_id(product_id, ppvIds)


        pass



























