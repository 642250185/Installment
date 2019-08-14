import os
import xlwt
from spider.base import Base

class Export(Base):

    def __get_spu_option(self, category_id, channel):
        '''
        获取所有的机型选项
        :param channel:     渠道
        :return: 选项列表
        '''
        list_options = self.db.get_allspu_alloption(category_id, channel)
        return list_options

    def _export(self):
        category_id = 1
        channel = 1
        # 获取原数据
        list_options = self.__get_spu_option(category_id, channel)
        print('总共导出数据 : %s' % len(list_options))
        list_final_data = []

        for dict_option in list_options:
            row = []
            row.append('分期乐'),
            row.append('手机'),
            row.append(dict_option['brand_id']),
            row.append(dict_option['brand_name']),
            row.append(dict_option['product_id']),
            row.append(dict_option['product_name']),
            row.append(dict_option['querstion_id']),
            row.append(dict_option['querstion_name']),
            row.append(dict_option['answer_id']),
            row.append(dict_option['answer_name'])
            list_final_data.append(row)


        book = xlwt.Workbook()
        sheet = book.add_sheet('fenqile')

        title = ['渠道', '类别', '品牌ID', '品牌名称', '机型ID', '机型名称', '问题项ID', '问题项名称', '答案项ID', '答案项名称']

        # 设置表头
        col_i = 0
        for content in title:
            sheet.write(0, col_i, content)
            col_i += 1

        # 设置内容
        col_l = 1
        for arr in list_final_data:
            row_i = 0
            for content in arr:
                sheet.write(col_l, row_i, content)
                row_i += 1
            col_l += 1

        book.save('分期乐SPU选项.xls')
        print('>>>>> done.')

