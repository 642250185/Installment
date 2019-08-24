import json
import time
import base64
import urllib.parse
import urllib.request


APPCODE = '2a3c99cfc75d433a88838f2fdbcabcb3'

def source_data():

    with open('./blackberry.png', 'rb') as f:  # 以二进制读取本地图片
        data = f.read()
        encodestr = str(base64.b64encode(data), 'utf-8')

    dict = {'img': encodestr}
    url_request = "https://ocrapi-advanced.taobao.com/ocrservice/advanced"

    # 请求头
    headers = {
        'Authorization': 'APPCODE {}'.format(APPCODE),
        'Content-Type': 'application/json; charset=UTF-8'
    }

    try:
        params = json.dumps(dict).encode(encoding='UTF8')
        req = urllib.request.Request(url_request, params, headers)
        r = urllib.request.urlopen(req)
        html = r.read()
        r.close()
        return html.decode("utf8")
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read().decode("utf8"))

    time.sleep(1)

def site_section(pos):
    list_y = []
    for xy in pos:
        x = xy['x']
        y = xy['y']
        list_y.append(y)

    return min(list_y), max(list_y)

def analysis(data):
    '''
    解析数据, 以黑莓为例
    :param data: 源数据
    :return:
    '''

    data = json.loads(data)

    # 唯一ID，用于问题定位
    sid = data['sid']
    #
    content = data['content']
    # 识别的文字具体内容
    prism_wordsInfo = data['prism_wordsInfo']

    # 获取列表大小
    data_len = len(prism_wordsInfo)
    print('data_len: ', data_len)

    for item in prism_wordsInfo:
        word = item['word']
        section = site_section(item['pos'])
        _min = section[0]
        _max = section[1]

        if _min < 90:
            continue

        print(_min, _max, word)
        # if _min


    pass

if __name__=="__main__":
    source_d = source_data()
    print(source_d)
    analysis(source_d)