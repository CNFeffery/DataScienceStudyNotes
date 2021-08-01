from multiprocessing import Pool
import numpy as np
from pprint import pprint

def job(n):
    return np.mean(np.random.rand(n)), np.std(np.random.rand(n))

if __name__ == '__main__':

    result = []
    for idx in range(10):
        with Pool(5) as p:
            result.append(p.map(job, [i**10 for i in range(1, 6)]))
            pprint(result.__len__())

