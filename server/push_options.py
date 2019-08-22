
from spider.base import Base

class pushOptions(Base):

    def _get_data(self):

        list_options = self.db.get_allspu_alloption(self.category_id, self.channel)
        return list_options

    def _pushData(self):

        list_options = self._get_data()
        list_options = list_options[0]

        print('len: %s, list_options: %s' % (len(list_options), list_options))

        list_filter_options = []
        for dict_options in list_options:
            list_key = []
            product_id = dict_options['product_id']
            list_key.append(product_id)




            pass
        pass