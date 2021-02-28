# import queue
#
# q = queue.Queue()
# print(q, type(q))
# for i in range(8):
#     q.put('item' + str(i))
# print(q.put('item' + str(i)))
# # print(list(q))
# while not q.empty():
#     print(q.get(), end=' ')

import threading
import threading
import time
import random
import queue
def myqueue(queue):
    while not queue.empty():
        item=queue.get()
        if item is None:
            break
        print('%sremoved%sfrom the queue'%(threading.current_thread(),item))
        queue.task_done()
        time.sleep(2)
q = queue.LifoQueue()
for i in range(5):
    q.put(i)
    threads=[]
for i in range(4):
    thread=threading.Thread(target=myqueue,args=(q,))
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()