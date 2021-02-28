# 暴力搜索法/穷取法
# def baiQian():
#   for x in range(0, 20):
#       for y in range(0, 33):
#           z = 100 - x - y
#           if 5 * x + 3 * y +z / 3 == 100:
#               return '公鸡:%d只，母鸡:%d只，小鸡：%d只' % (x, y, z)
# res = baiQian()
# print(res)

# 输出10000以内的完美数

# import math
# def wan_mei_shu():
#     for num in range(1, 10000):
#         result = 0
#         for factor in range(1, int(math.sqrt(num)) + 1):
#             if num % factor == 0:
#                 result += factor
#                 # print(result)
#                 if factor > 1 and num // factor != factor:
#                     result += num // factor
#         if result == num:
#             print(num)
#


# wan_mei_shu()
# import math
# for num in range(1,10000):
#     result = 0
#     for factor in range(1, int(math.sqrt(num)) + 1):
#         if num % factor == 0:
#             result += factor
#             if factor > 1 and num // factor != factor:
#                 result = result + num // factor
#
#     if result == num:
#             print(num)


def is_prime():
    for i in range(2, 100):
        count = 0
        for k in range(1, i + 1):
            if i % k == 0:
                count += 1
        if count == 2:
            print(i, end='-')

# su_shu()
import math
for num in range(2, 100):
    is_prime = True
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end='--')

