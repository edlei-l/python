file = open('i have a dream.txt', 'r', encoding='  utf-8')
txt = file.read()
file.close()
txt = txt.lower()
for biaodian in ',.?!':
    txt = txt.replace(biaodian, ' ')
words = txt.split()
number = {}
for word in words:
    if word in number:
        number[word] = number[word] + 1
    else:
        number[word] = 1
items = list(number.items())  #元组换列表
items.sort(key=lambda x: x[1], reverse=True)  #key为排列参数，返回第二个参数，由大到小
sum = 0
for item in items:
    sum += 1
    if sum <= 10:
        print(item[0], item[1])
    else:
        break
