from threading import Thread

def worker(i, j):
    print('worker =', i+j)
    
jobs = [Thread(target=worker, args=(i, j)) for i, j in zip(range(5), range(5, 10))]

for j in jobs:
    print('starting', j)
    j.start()

for j in jobs:
    print('joining', j)
    j.join()


print('use ThreadPoolExecutor   ')

from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(worker, i, j) for i, j in zip(range(5), range(5, 10))]
    # for future in futures:
    #     print('result =', future.result())