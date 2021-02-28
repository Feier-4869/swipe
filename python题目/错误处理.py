import logging
g=(x for x in range(5))
while True:
    try:
        print(next(g))
    except StopIteration as e:
        print(e)
        print('执行完毕')
        break
