# import _thread
# import threading
# import time
# import random
# def fn1(*args):
#     print(args)
#     print(threading.current_thread().name)
#
# # def create_thread():
# #     pass
# #     # print(threading.current_thread().name)
# # _thread.start_new_thread(fn1,('feier','lsyj'))
# # print('hello')
# # time.sleep(10)
#
# def created_thread2():
#     t=threading.Thread(target=fn1,daemon=True,name='feier',args=('ff','lsyj'))
#     t.start()
#     print('jello')
#     # time.sleep(10)
# # created_thread2()
#
#
# def fn(*args):
#     time.sleep(random.randint(1,3))
#     print('子线程',args)
#
#
# if __name__ == '__main__':
#     # t1=threading.Thread(target=fn,args=('feier',))
#     # t1.start()
#     # t1.join()
#     # t3 = threading.Thread(target=fn, args=('feier3',))
#     # t3.start()
#     # t3.join()
#     # t2=threading.Thread(target=fn,args=('feier1',))
#     # t2.start()
#     # t2.join()
#     # start=time.time()
#     # t_list=[]
#     # for i in range(1,10):
#     #
#     #     t=threading.Thread(target=fn,args=('feier-%d' %i,))
#     #     t.start()
#     #     # t.join()
#     #     t_list.append(t)
#     #     # print(t.name)
#         # print(threading.current_thread().name)
#         # print(t.ident)
#         # print(t.is_alive())
#         # print(threading.active_count())
#         # print(threading.enumerate())
#         #
#         # for t in t_list:
#         #     t.join()
#         # end=time.time()
#         # print(end-start)
#         #
#         pass
#
# num=0
# def fei():
#     global num
#     for x in range(10000000):
#         num+=1
#     # print(num)
#
# def thread3():
#     for i in range(5):
#         t=threading.Thread(target=fei)
#         t.start()
#
# # thread3()
# if __name__ == '__main__':
#     t1=[]
#     for i in range(10):
#         t=threading.Thread(target=fei)
#         t.start()
#         t1.append(t)
#         for t in t1:
#             t.join()
#             print(num)
from functools import reduce
a=[3,4,5,1,2,3,4,5,6,7,8,1,3,5]
# c=map(lambda x:x**2 ,a)
# print(list(c))
# d=reduce(lambda x,y:x*y,a)
# print(d)
# b=set(a)
# print(list((b)))

l2=[]
[l2.append(i) for i in a if i not in l2 ]
print(l2)