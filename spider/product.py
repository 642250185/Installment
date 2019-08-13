import json
import requests
from spider.base import Base

class Product(Base):

    def __get_product(self, dict_brand):

        category_id = dict_brand['category_id']
        brand_id = dict_brand['brand_id']

        # 获取路由
        domain = self.cfg.get_cfg_value("ROUTE", "domain")
        open_api = self.cfg.get_cfg_value("ROUTE", "open_api_url")
        product_url = self.cfg.get_cfg_value("ROUTE", "product_url")

        # 请求链接
        url = '{}/{}/{}'.format(domain, open_api, product_url)

        # 设置请求头
        headers = {
            "Host": self.cfg.get_cfg_value("HEADERS", "Host"),
            "App-Slug": self.cfg.get_cfg_value("HEADERS", "App-Slug"),
            "Accept-Encoding": self.cfg.get_cfg_value("HEADERS", "Accept-Encoding"),
            "Connection": self.cfg.get_cfg_value("HEADERS", "Connection"),
            "Accept": self.cfg.get_cfg_value("HEADERS", "Accept"),
            "sid": self.cfg.get_cfg_value("HEADERS", "sid"),
            "User-Agent": self.cfg.get_cfg_value("HEADERS", "User-Agent"),
            "Referer": self.cfg.get_cfg_value("HEADERS", "Referer"),
            "Accept-Language": self.cfg.get_cfg_value("HEADERS", "Accept-Language"),
            "Content-Type": self.cfg.get_cfg_value("HEADERS", "Content-Type"),
            "Content-Length": self.cfg.get_cfg_value("HEADERS", "Content-Length"),
            "Origin": self.cfg.get_cfg_value("HEADERS", "Origin"),
            "Cookie": self.cfg.get_cfg_value("HEADERS", "Cookie"),
            "Authorization": self.cfg.get_cfg_value("HEADERS", "Authorization"),
        }

        # 请求体
        body = {
            "categoryId": category_id,
            "brand": brand_id,
            "pageIndex": 0,
            "pageSize": 999
        }

        try:
            result = requests.post(url, headers=headers, data=json.dumps(body))
            result = json.loads(result.text)

            code = result['code']
            data = result['data']
            resultMessage = result['resultMessage']

            if code == 200:
                for dict_item in data:
                    product_id = dict_item['id']
                    product_name = dict_item['name']

                    dict_product = {
                        "channel" : 1,
                        "brand_id" : brand_id,
                        "product_id" : product_id,
                        "product_name" : product_name
                    }

                    # 检测是否存在
                    is_product = self.db.get_productbypid(1, product_id)
                    if len(is_product) > 0:
                        print('已存在 >> %s, %s, %s' % (brand_id, product_id, product_name))
                        continue

                    # 入库
                    self.db.add_product(dict_product)
                    print('%s, %s, %s ' % (brand_id, product_id, product_name))
                pass
            else:
                print('请求失败: %s, %s, code: %s, message: %s' % (category_id, brand_id, code, resultMessage))
                pass
            pass
        except BaseException as e:
            print('请求失败>> e: ', e)
            pass
        pass

    def all_product(self):

        # 获取所有的品牌
        list_brands = self.db.get_allbrands(1, 1)

        print('brand_Len: ', len(list_brands))

        for dict_brand in list_brands:

            self.__get_product(dict_brand)

            # break
            pass
        pass




