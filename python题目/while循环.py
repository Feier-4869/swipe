import random

answer = random.randint(1, 100)
# print(answer)
count = 0
while True:
    count += 1
    number = int(input('请输入：'))
    if number < answer:
        print('大一些')
    elif number > answer:
        print('小一些')
    else:
        print('恭喜您猜对了')
        break
if __name__ == '__main__':
    print('你总共猜了%d次' % count)
    if count > 7:
        print('您的智商余额明显不足')