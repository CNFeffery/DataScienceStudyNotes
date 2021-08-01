import multiprocessing
import datetime
import numpy as np
import os

def job():

    print(f'进程{os.getpid()}开始计算：', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    for j in range(100):
        _ = np.sum(np.random.rand(10000000))
    print(f'进程{os.getpid()}结束运算：', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == '__main__':

    process_list = []

    for i in range(multiprocessing.cpu_count() - 1):
        process = multiprocessing.Process(target=job)
        process_list.append(process)

    for process in process_list:
        process.start()

    for process in process_list:
        process.join()