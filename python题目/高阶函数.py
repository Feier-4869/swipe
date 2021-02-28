# # def map2(func, iter1):
# #     res = []
# #     for x in iter1:
# #         res.append(func(x))
# #     return iter(res)
# #
# #
# # list1 = ['1','2','3','4','5']
# # def func(list1):
# #     list2=[]
# #     for x in list1:
# #         list2.append(int(x))
# #     return list2
# # # res = func(list1)
# # # print(res)
# #
# # obj = map2(int, list1)
# # print(obj)
# # print(list(obj))
#
# # list2 = [1,2,3,-4,-5]
# # res = map(abs,list2)
# # print(res)
# # print(list(res))
# # list3 = [1,2,3,4,5]
# # res2=map(lambda x :x * x ,list3)
# # print(res2)
# # print(list(res2))
#
#
# from functools import reduce
# import functools
# import operator
# # def func(n):
# #     res = 0
# #     for x in range(1, n+1):
# #         res += x
# #     return res
# # print(func(100000000))
# # print(reduce(operator.add, range(1,101000000)))
# print(reduce(operator.mul, range(1,6)))
# list3 = [1,2,'3','4','5',6, 7]
# print(reduce(lambda x,y:str(x)+str(y), list3))
# print(reduce(operator.add, map(str,list3)))


# list1 = [1,2,4,5,6,7,3]
# def func(num):
#     if num % 2==0:
#         return True
#     return False
# l = filter(func,list1)
# print(l)
# print(list(l))
# data = [["姓名", "年龄", "爱好"],
#         ["tom", 25, "无"],
#         ["hanmeimei", 26, "金钱"]]
#
# def func(list1):
#         if '无' in list1:
#                 return  False
#         return True

# res = filter(func, data)
# print(res)
# print(list(res))

#
# list1 = [4,3,5,6,1,6,5]
# print(list(set(list1)))
# list2=sorted(list1)
# print(list2)
#
# list3 =[4,-3,5,2,9]
# list4=sorted(list3,key=abs)
# print(list4)
# list5=sorted(map(abs,list3))
# print(list5)



a = [1,2,3]
b= [4,5,6]
c=[7,4,5,6,7,8]
zipped=zip(a,b)
print(zipped)
print(list(zipped))
zip1=zip(a,c)
print(list(zip1))