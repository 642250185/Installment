import xlwt

book = xlwt.Workbook()
sheet = book.add_sheet('fish·cc')

title = ['姓名', '班级', '住址', '手机号']

shuzu = [
    ['bred', 'class1', 'mingdong', 188109],
    ['shade', 'class2', 'gugong', 3332],
    ['dd', 'class3', 'changcheng', 6666]
]

i = 0
for j in title:
    sheet.write(0, i, j)
    i += 1

l = 1
for d in shuzu:
    c = 0
    for dd in d:
        sheet.write(l, c, dd)
        c += 1
    l += 1
book.save('fish.xls')







