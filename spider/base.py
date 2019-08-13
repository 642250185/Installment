from utils.config import *
from utils.sharing import *
from db import dbService

class Base:


    def __init__(self):

        # 初始化
        cfg = Config()
        share = Sharing()
        db = dbService.DBConnect()

        # 初始赋值
        self.db = db
        self.cfg = cfg
        self.share = share
