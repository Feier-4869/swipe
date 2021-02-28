chars = ['f', 'e', 'i', 'e', 'r']
name = ''.join(chars)
print(name, type(name))
#用生成式生成密码
data = [7, 20, 3, 15, 11]
result = [num * 3 for num in data if num > 10]
print(result)
#用zip组合键和值来创建字典
keys = ['0001', '0002', '0003']
values = ['fieer', 'baoer', 'me']
d = dict(zip(keys, values))
print(d, type(d))
#使用enumerate进行迭代
fruits = ['orange', 'grape', 'pitaya', 'blueberry']
for index, fruit in enumerate(fruits):
    print(index, ':', fruit)
#善于使用in运算符
name = 'Fei er'
if 'F' in name:
    print('This name has an F in it')
#善于使用if X或者if not x这样的表达式
keys = ['0001', '0002', '0003']
values = ['fieer', 'baoer', 'me']
name = 'feier'
if keys and values and name:
    print('I love feier')