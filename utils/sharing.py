import json, re

class Sharing:


    def loads_jsonp(self, _jsonp):
        """
        解析jsonp数据格式为json
        :return:
        """
        try:
            return json.loads(re.match(".*?({.*}).*", _jsonp, re.S).group(1))
        except:
            raise ValueError('Invalid Input')