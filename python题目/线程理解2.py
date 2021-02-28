# # from threading import Thread
# # from multiprocessing import Process
# # #
# # #
# # # def loop():
# # #     while True:
# # #         print('L love you feier forever')
# # #
# # #
# # # if __name__ == '__main__':
# # #     for i in range(3):
# # #         # t = Thread(target=loop)
# # #         t = Process(target=loop)
# # #         t.start()
# # #
# # #         # t.join()
# # #     while True:
# # #         pass
# # # class MyThreadind(threading.Thread)
# #
# # import _thread
# # import threading
# # import time
# #
# #
# # # def fn1(*args):
# # #     print(args)
# # #     print(threading.current_thread().name)
# # #
# # #
# # # def create_thread():
# # #     print(threading.current_thread().name)
# # #
# # # print('hello')
# # # _thread.start_new_thread(fn1, ('feier', 'love'))
# # #
# # # time.sleep(10)
# #
# # def fn2(*args):
# #     print(args)
# #     print(threading.current_thread().name)
# #
# #
# # def create_thread2():
# #     t = threading.Thread(target=fn2, daemon=False, name='菲儿', args=('feier', 'love'))
# #     t.start()
# #     # t.join()
# #
# #     print('hello')
#
# import threading
# import time
# import random
#
#
# def fn(*arg):
#     time.sleep(random.randint(1, 10))
#     print('子线程', arg)
#
#
# if __name__ == '__main__':
#     # t1 = threading.Thread(target=fn, args=('feier',))
#     # t1.start()
#     # t1.join()
#     # t2 = threading.Thread(target=fn, args=('feierl',))
#     # t2.start()
#     # t2.join()
#     # t3 = threading.Thread(target=fn, args=('feierll',))
#     # t3.start()
#     # t3.join()
#
# # def thread_states():
# #     print('Thread entered in running state')
# #
# # time.sleep(2)
# # T1=threading.Thread(target=thread_states)
# # T1.start()
# # T1.join()
#     t_list=[]
#     t1 = time.time()
#     for i in range(1,10):
#         t=threading.Thread(target=fn,args=('ferier-%d'%i,))
#
#         t_list.append(t)
#         t.start()
#         # t.join()
#     t2 = time.time()
#     print(t2-t1)
#     print(t.name)
#     print(t.ident)
#     print(t.daemon)
#     print(t.is_alive())
#     print(threading.active_count())
#     print(threading.enumerate())
#     for t in t_list:
#         t.join()
import threading

n = 0


def fn():
    global n
    for _ in range(100000):
        n += 1
    print(n)


if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=fn)
        t.start()
        # t.join()
