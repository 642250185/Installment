import os
import configparser

class Config:

    def __init__(self):

        # 获取配置文件路径
        pro_dir = os.path.split(os.path.realpath(__file__))[0]
        config_path = os.path.join(pro_dir, "../config/config.ini")

        # 解析配置文件
        config = configparser.RawConfigParser()
        config.read(config_path)
        self.config = config

    def get_cfg_value(self, section, key):
        try:
            value = self.config.get(section, key)
            return value
        except Exception as e:
            print(e)
            print('%s, %s, 没有该配置内容, 请仔细检查参数是否正确。' % (section, key))
            return ""


