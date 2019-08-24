import json
import requests
from spider.base import Base
from spider import access_token

class Option(Base):

    def __analysis_options(self, product_id, list):
        list_spu_options = []

        for question in list:
            q_id = question['id']
            q_name = question['name']
            q_type = question['type']
            answers = question['values']
            for answer in answers:
                a_id = answer['id']
                a_name = answer['name']

                dict_option = {
                    "channel": self.channel,
                    "flag": q_type,
                    "product_id": product_id,
                    "querstion_id": q_id,
                    "querstion_name": q_name,
                    "answer_id": a_id,
                    "answer_name": a_name
                }

                list_spu_options.append(dict_option)

                pass
            pass

        return list_spu_options

    def __get_option(self, token, product):

        product_id = product['product_id']
        product_name = product['product_name']

        # 获取路由
        domain = self.cfg.get_cfg_value("ROUTE", "domain")
        open_api = self.cfg.get_cfg_value("ROUTE", "open_api_url")

        # 请求链接
        url = '{}/{}/products/{}/{}'.format(domain, open_api, product_id, 'product-info-with-properties')

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
            "Cookie": self.cfg.get_cfg_value("HEADERS", "Cookie"),
            "Authorization": "bearer " + token
        }

        try:

            # 判断该机型是否入options库
            options = self.db.get_optionbypid(self.channel, product_id)
            if len(options) > 0:
                print('已存在库中 >> 机型ID: %s, 机型名称: %s 跳过' % (product_id, product_name))
                return
            # 发起请求
            result = requests.get(url, headers=headers)
            result = json.loads(result.text)

            code = result['code']
            data = result['data']
            resultMessage = result['resultMessage']

            if code == 200:
                productInfo = data['productInfo']
                properties = productInfo['properties']

                # 过滤数据
                list_spu_options = self.__analysis_options(product_id, properties)

                if len(options) == len(list_spu_options):
                    print('机型ID: %s, 机型名称: %s, 选项数量无变化: [%s, %s]' % (product_id, product_name, len(options), len(list_spu_options)))
                    return

                # 当全部过滤好该机型的数据之后再执行入库操作，
                # 确保了采集该机型详情的完整性。
                for dict_spu_option in list_spu_options:

                    _querstion_id = dict_spu_option['querstion_id']
                    _querstion_name = dict_spu_option['querstion_name']
                    _answer_id = dict_spu_option['answer_id']
                    _answer_name = dict_spu_option['answer_name']

                    # 查询参数
                    dict_params_SQL = {
                        "channel" : self.channel,
                        "product_id": product_id,
                        "querstion_id": _querstion_id,
                        "answer_id": _answer_id
                    }

                    # 检测是否存在
                    is_option = self.db.get_optionbyparams(dict_params_SQL)
                    if len(is_option) > 0:
                        print('已存在 >> %s, %s, %s, %s, %s, %s ' % (product_id, product_name, _querstion_id, _querstion_name, _answer_id, _answer_name))
                        continue
                    else:
                        print('机型ID: %s, 机型名称: %s, 问题ID: %s, 问题名称: %s, 答案ID: %s, 答案名称: %s ' % (product_id, product_name, _querstion_id, _querstion_name, _answer_id, _answer_name))
                        self.db.add_option(dict_spu_option)
                    pass
                pass
            else:
                print('请求失败 %s,  %s,  code: %s, message: %s' % (product_id,  product_name, code, resultMessage))
                pass
            pass
        except BaseException as e:
            print('请求异常 >> e: ', e)
            pass
        pass

    def all_spu_options(self):

        all_products = self.db.get_allproducts(self.channel)
        print('SPU_Len: ', len(all_products))

        # 初始化token
        cls_token = access_token.AccessToken()
        dict_access_token = cls_token._get_token()

        token = dict_access_token['token']

        for product in all_products:
            self.__get_option(token, product)
            break
            pass
        pass

