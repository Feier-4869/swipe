
# 5.现有字典 d= {'a':24,'g':52,'i':12,'k':33}
# 请按value值进行排序?
from functools import reduce

d= {'a':24,'g':52,'i':12,'k':33}

def value(d):
    d1=sorted(d.items(), key=lambda x: x[1])
    print(d1,dict(d1))

# value()
# 6.字典推导式
# d={key,value for(key,value) in iterable}




# 8.将字符串 "k:1 |k1:2|k2:3|k3:4"，
# 处理成字典 {k:1,k1:2,...}
d="k:1 |k1:2|k2:3|k3:4"
def str_dict(d):
    a={}
    d_split=d.split('|')
    for i in d_split:
        # print(i,type(i))
        d1=i.split(':')
        a[d1[0]]=int(d1[1])
    return a

    # 2#字典推导式
    # d={k:int(v) for t in str1.split('|')
    #    for k,v in (t.split(':'),)}



    # print(d_split)

#
# res=str_dict(d)
# print(res)


# 9.请按alist中元素的age由大到小排序

alist = [{'name':'a','age':20},
         {'name':'b','age':30},
         {'name':'c','age':25}]


def age_sort(alist):
    d=sorted(alist,key=lambda x:x['age'],reverse=True)
    return d
# res=age_sort(alist)
# print(res)




# 10.下面代码的输出结果将是什么？

# list = ['a','b','c','d','e']
# print(list[10:])


#
# 11.写一个列表生成式，产生一个公差为11的等差数列11.
# 写一个列表生成式，产生一个公差为11的等差数列
# d=[11*x for x in range(10)]
# print(d)

# 12.给定两个列表，怎么找出他们相同的元素和不同的元素？
# list1 = [1,2,3]
# list2 = [3,4,5]
# d1=set(list1)
# d2=set(list2)
#
# d3=d1&d2
# print(d3)
#
# d4=d1^d2
# print(d4)




# 13.请写出一段python代码实现删除list里面的重复元素？
# l1 = ['b','c','d','c','a','a']
# d2=list(set(l1))
# d3=d2.sort(key=l1.index)
# print(d2)

# 16.python中内置的数据结构有几种？
"""
整形，长整形，浮点型,复数型
list,str,tuple,dict,set


"""


# 17.python如何实现单例模式?请写出两种实现方式?


class Single:

    instance=None
    def __new__(cls, *args, **kwargs):

        if not isinstance:
             cls.instance=object.__new__(cls,*args, **kwargs)
        return cls.instance
#
# s1=Single('fffff','rtr')
# s2=Single('fdsg','fgfh')
# print(s1,id(s1))
# print(s2,id(s2))




# 18.反转一个整数，例如-123 --> -321


def reverse(s:int):
    if s>0:
        s1=str(s)
        s2=s1[::-1]
        print(int(s2))
    else:
        s3=str(abs(s))
        s4=s3[::-1]
        print(-int(s4))


# reverse(-1235)


# 20.一行代码实现1-100之和
# count=sum(range(0,101))
# print(count)



# 26.用一行python代码写出1+2+3+10248
num=sum([1,2,3,10248])
print(num)
num1=reduce(lambda x,y:x+y,[1,2,3,10248])
print(num1)













