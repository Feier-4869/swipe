import multiprocessing
import time
def child_process():
    print('starting functing')
    time.sleep(5)
    print('Finished function')
p=multiprocessing.Process(target=child_process)
p.start()
print('my process has terminated, terminating main thread')
print('terminating child process')
# p.join()
p.terminate()
print('child process successfully terminated')
