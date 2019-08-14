import MySQLdb
import datetime
from utils.config import *

class DBConnect(object):

    def __init__(self):

        cfg = Config()
        HOST = cfg.get_cfg_value("DATABASE", "host")
        USER = cfg.get_cfg_value("DATABASE", "username")
        PASSWD = cfg.get_cfg_value("DATABASE", "password")
        DB = cfg.get_cfg_value("DATABASE", "database")

        self.db = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, db=DB, use_unicode=True, charset="utf8")
        self.cursor = self.db.cursor()


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()


    def get_brandsbyid(self, channel,  category_id,  brand_id):
        '''
        检测该渠道该类别下的品牌是否存在
        :param channel:     渠道
        :param category_id:    类别
        :param brand_id:    品牌ID
        :return:
        '''
        SQL = "select * from t_bi_brands where channel = {} and category_id = {} and brand_id = {}".format(channel, category_id, brand_id)
        self.cursor.execute(SQL)
        tuple_brand = self.cursor.fetchone()

        list_brands = []
        if tuple_brand is None:
            return list_brands
        else:
            list_brands.append({
                "id" : tuple_brand[0],
                "channel" : tuple_brand[1],
                "category_id" : tuple_brand[2],
                "brand_id" : tuple_brand[3],
                "brand_name" : tuple_brand[4],
            })

            return list_brands

    def get_productbypid(self, channel, product_id):

        SQL = "select * from t_bi_products where channel = {} and product_id = {}".format(channel, product_id)
        self.cursor.execute(SQL)
        tuple_product = self.cursor.fetchone()

        list_products = []
        if tuple_product is None:
            return list_products
        else:
            list_products.append({
                "id" : tuple_product[0],
                "channel" : tuple_product[1],
                "brand_id" : tuple_product[2],
                "product_id" : tuple_product[3],
                "product_name" : tuple_product[4]
            })

            return list_products

    def get_optionbypid(self, channel, product_id):

        SQL = "select * from t_bi_options where channel = {} and product_id = {}".format(channel, product_id)
        self.cursor.execute(SQL)
        results = self.cursor.fetchall()
        list_options = []
        for row in results:
            dict_options = {
                "id": row[0],
                "channel": row[1],
                "product_id": row[2],
                "querstion_id": row[3],
                "querstion_name": row[4],
                "answer_id": row[5],
                "answer_name": row[6],
                "create_date": row[7],
                "update_date": row[8]
            }
            list_options.append(dict_options)
        return list_options

    def get_optionbyparams(self, dict_params):
        '''
        获取具体的问题项和答案项在该机型中是否存在
        :param dict_params:
        :return:
        '''
        channel = dict_params['channel']
        product_id = dict_params['product_id']
        querstion_id = dict_params['querstion_id']
        answer_id = dict_params['answer_id']

        SQL = "select * from t_bi_options where channel = {} and product_id = {} and querstion_id = {} and answer_id = {}".format(channel, product_id, querstion_id, answer_id)

        self.cursor.execute(SQL)
        results = self.cursor.fetchone()
        if results is None:
            return []

        return results

    def get_allbrands(self, channel, category_id):

        SQL = "select * from t_bi_brands where channel = {} and category_id = {}".format(channel, category_id)
        self.cursor.execute(SQL)
        results = self.cursor.fetchall()
        list_brands = []
        for row in results:
            dict_brands = {
                "id" : row[0],
                "channel" : row[1],
                "category_id" : row[2],
                "brand_id" : row[3],
                "brand_name" : row[4]
            }
            list_brands.append(dict_brands)

        return list_brands


    def get_allproducts(self, channel):

        SQL = "select * from t_bi_products where channel = {}".format(channel)
        self.cursor.execute(SQL)
        results = self.cursor.fetchall()
        list_products = []
        for row in results:
            dict_products = {
                "id" : row[0],
                "channel" : row[1],
                "brand_id" : row[2],
                "product_id" : row[3],
                "product_name" : row[4],
                "create_date" : row[5],
                "update_date" : row[6]
            }
            list_products.append(dict_products)

        return list_products


    def get_alloptions(self, channel):

        SQL = "select * from t_bi_options where channel = {}".format(channel)
        self.cursor.execute(SQL)
        results = self.cursor.fetchall()
        list_options = []
        for row in results:
            dict_options = {
                "id": row[0],
                "channel": row[1],
                "product_id": row[2],
                "querstion_id": row[3],
                "querstion_name": row[4],
                "answer_id": row[5],
                "answer_name": row[6],
                "create_date": row[7],
                "update_date": row[8]
            }
            list_options.append(dict_options)

        return list_options


    def get_allspu_alloption(self, category_id, channel):

        SQL = "select b.channel, b.category_id, b.brand_id, b.brand_name, p.product_id, p.product_name, o.querstion_id, o.querstion_name, o.answer_id, o.answer_name " \
              "from t_bi_options o, t_bi_products p, t_bi_brands b " \
              "where o.product_id = p.product_id " \
              "and p.brand_id = b.brand_id " \
              "and b.category_id = {} and p.channel = {} and o.channel = {}".format(category_id, channel, channel)

        self.cursor.execute(SQL)
        results = self.cursor.fetchall()
        list_options = []
        for row in results:
            dict_options = {
                "channel": row[0],
                "category_id": row[1],
                "brand_id": row[2],
                "brand_name": row[3],
                "product_id": row[4],
                "product_name": row[5],
                "querstion_id": row[6],
                "querstion_name": row[7],
                "answer_id": row[8],
                "answer_name": row[9]
            }
            list_options.append(dict_options)

        return list_options

    def get_link_options_pid(self, category_id, product_id, channel):

        SQL = "select b.channel, b.category_id, b.brand_id, b.brand_name, p.product_id, p.product_name, o.querstion_id, o.querstion_name, o.answer_id, o.answer_name " \
              "from t_bi_options o, t_bi_products p, t_bi_brands b " \
              "where o.product_id = p.product_id " \
              "and p.brand_id = b.brand_id " \
              "and b.category_id = {} and p.channel = {} and o.channel = {} and o.product_id = {}".format(category_id, channel, channel, product_id)

        self.cursor.execute(SQL)
        results = self.cursor.fetchall()
        list_options = []
        for row in results:
            dict_options = {
                "channel": row[0],
                "category_id": row[1],
                "brand_id": row[2],
                "brand_name": row[3],
                "product_id": row[4],
                "product_name": row[5],
                "querstion_id": row[6],
                "querstion_name": row[7],
                "answer_id": row[8],
                "answer_name": row[9]
            }
            list_options.append(dict_options)

        return list_options


    def add_brands(self, obj_brand):
        channel = obj_brand['channel']
        category_id = obj_brand['category_id']
        brand_id = obj_brand['brand_id']
        brand_name = obj_brand['brand_name']
        create_date = datetime.datetime.now()
        update_date = datetime.datetime.now()

        # SQL语句
        SQL = "insert into t_bi_brands(channel, category_id, brand_id, brand_name, create_date, update_date) values (%s, %s, %s, %s, %s, %s)"

        # SQL参数
        args = (channel, category_id, brand_id, brand_name, create_date, update_date)

        # 执行SQL
        res = self.cursor.execute(SQL, args)

        # 提交执行
        self.db.commit()

        if res != 1:
            print('%s, %s, 入库失败' % (brand_id, brand_name))

        pass

    def add_product(self, obj_product):
        channel = obj_product['channel']
        brand_id = obj_product['brand_id']
        product_id = obj_product['product_id']
        product_name = obj_product['product_name']
        create_date = datetime.datetime.now()
        update_date = datetime.datetime.now()

        # SQL语句
        SQL = "insert into t_bi_products(channel, brand_id, product_id, product_name, create_date, update_date) values (%s, %s, %s, %s, %s, %s)"

        # SQL参数
        args = (channel, brand_id, product_id, product_name, create_date, update_date)

        # 执行SQL
        res = self.cursor.execute(SQL, args)

        # 提交执行
        self.db.commit()

        if res != 1:
            print('%s, %s, 入库失败' % (product_id, product_name))

        pass

    def add_option(self, obj_option):
        # 解析参数
        channel = obj_option['channel']
        product_id = obj_option['product_id']
        querstion_id = obj_option['querstion_id']
        querstion_name = obj_option['querstion_name']
        answer_id = obj_option['answer_id']
        answer_name = obj_option['answer_name']
        create_date = datetime.datetime.now()
        update_date = datetime.datetime.now()

        SQL = "insert into t_bi_options(channel, product_id, querstion_id, querstion_name, answer_id, answer_name, create_date, update_date) values (%s, %s, %s, %s, %s, %s, %s, %s)"

        # SQL参数
        args = (channel, product_id, querstion_id, querstion_name, answer_id, answer_name, create_date, update_date)

        # 执行SQL
        res = self.cursor.execute(SQL, args)

        # 提交执行
        self.db.commit()

        if res != 1:
            print('%s, %s, 入库失败' % (product_id))

        pass
