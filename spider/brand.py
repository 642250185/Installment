import json
import requests
from spider.base import Base

class Brands(Base):

    def get_brands(self):

        # 获取路由
        domain = self.cfg.get_cfg_value("ROUTE", "domain")
        open_api = self.cfg.get_cfg_value("ROUTE", "open_api_url")
        brand_url = self.cfg.get_cfg_value("ROUTE", "brand_url")

        # 请求链接
        url = '{}/{}/{}'.format(domain, open_api, brand_url)

        # 设置请求头
        headers = {
            "Host": self.cfg.get_cfg_value("HEADERS", "Host"),
            "App-Slug": self.cfg.get_cfg_value("HEADERS", "App-Slug"),
            "Accept-Encoding": self.cfg.get_cfg_value("HEADERS", "Accept-Encoding"),
            "Connection": self.cfg.get_cfg_value("HEADERS", "Connection"),
            "Accept": self.cfg.get_cfg_value("HEADERS", "Accept"),
            "sid": self.cfg.get_cfg_value("HEADERS", "sid"),
            "User-Agent": self.cfg.get_cfg_value("HEADERS", "User-Agent"),
            "Accept-Language": self.cfg.get_cfg_value("HEADERS", "Accept-Language"),
            "Referer": self.cfg.get_cfg_value("HEADERS", "Referer"),
            "Cookie": self.cfg.get_cfg_value("HEADERS", "Cookie"),
            "Authorization": self.cfg.get_cfg_value("HEADERS", "Authorization"),
        }

        try:

            result = requests.get(url, headers=headers)
            result = json.loads(result.text)

            code = result['code']
            data = result['data']
            resultMessage = result['resultMessage']
            if code == 200:
                for dict_item in data:

                    brand_id = dict_item['id']
                    brand_name = dict_item['name']

                    dict_brand = {
                        "channel" : 1,
                        "category_id" : 1,
                        "brand_id" : brand_id,
                        "brand_name" : brand_name
                    }

                    # 检测
                    list_brands = self.db.get_brandsbyid(1, 1, brand_id)
                    if len(list_brands) > 0:
                        print('%s, %s, 已经存在' % (brand_id, brand_name))
                        continue

                    # 入库
                    self.db.add_brands(dict_brand)
                    print('save brands done.')
                    pass
                pass
            else:
                print('请求失败: %s, %s ' % (code, resultMessage))
                pass
            pass
        except BaseException as e:
            print('请求失败>> e : ', e)
            pass
        pass

