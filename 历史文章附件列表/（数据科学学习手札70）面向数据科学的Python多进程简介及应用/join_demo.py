import multiprocessing
import os
import datetime
import time

def job():

    print(f'进程{os.getpid()}开始：', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(5)
    print(f'进程{os.getpid()}结束：', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == '__main__':

    process1 = multiprocessing.Process(target=job)
    process2 = multiprocessing.Process(target=job)

    process1.start()
    process1.join()

    process2.start()
    process2.join()
    print('='*200)
    process3 = multiprocessing.Process(target=job)
    process4 = multiprocessing.Process(target=job)

    process3.start()
    process4.start()

    process3.join()
    process4.join()