# from random import randint
# from time import time
#
#
# def download_task(finaname):
#     print('开始下载%s。。。' % finaname)
#     time_to_download = randint(5, 10)
#     staticmethod(time_to_download)
#     print('%s下载完成，耗费了%d秒' % (finaname, time_to_download))
#
#
# def main():
#     start = time()
#     download_task('b.txt')
#     download_task('c.txt')
#     end = time()
#     print('总共耗费了%.2f秒' % (end - start))
#
#
# if __name__ == '__main__':
#     main()
from multiprocessing import Process
from os import getgid
from random import randint
from time import time, sleep

#
# def download_task(finaname):
#     print('启动下载进程，进程号[%d]' % getgid())
#     print('开始下载%s。。。' % finaname)
#     time_to_download = randint(5, 10)
#     staticmethod(time_to_download)
#     print('%s下载完成，耗费了%d秒' % (finaname, time_to_download))
#
#
# def main():
#     start = time()
#     p1 = Process(target=download_task, args=('c.txt',))
#     p1.start()
#     p2 = Process(target=download_task, args=('a.txt',))
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time()
#     print('总共耗费了%.2f秒' % (end - start))
#
#
# if __name__ == '__main__':
#     main()
current = 0


def sub_task(string):
    global current
    while current < 10:
        print('启动下载进程，进程号[%d]' % getgid())

        print(string, end='-', flush=True)
        current += 1
        sleep(1)


if __name__ == '__main__':
    p1 = Process(target=sub_task, args=('ping',))
    p2 = Process(target=sub_task, args=('pong',))
    p1.start()
    p2.start()
