# import _thread
# import time
#
#
# def print_time(threadName, delay):
#     count = 0
#     while count < 0:
#         time.sleep(delay)
#         count += 1
#         print("%s:%s" % (threadName, time.ctime(time.time())))
#
#
# if __name__ == '__main__':
#     _thread.start_new_thread(print_time, ('thread-1', 2))
#     _thread.start_new_thread(print_time, ('thread-2', 4))
import threading
import time

exitFlag = 0


class Mythread(threading.Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter

    def run(self):
        print('Starting' + self.name)
        print_time(self.name, self.counter, 5)
        print('Exiting' + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s:%s" % (threadName, time.ctime(time.time())))
        counter -= 1


if __name__ == '__main__':
    thread1 = Mythread(3, 'Thread-1', 1)
    thread2 = Mythread(4, 'Thread-2', 2)
    thread1.start()
    thread2.start()
    thread1.run()

    thread1.join()
    thread2.run()
    thread2.join()
    print('Exiting Main Thread')
