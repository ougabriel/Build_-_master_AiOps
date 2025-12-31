# A simple program that uses processor to perform a cpu intensive task; such as crunching a large number.

from multiprocessing import Process
import multiprocessing
import time

def cpu_heavy():
    print("Crunching the numbers.")
    total = 0
    for i in range(10**9):
        total += i
    print("Done with the crunch")

if __name__ == "__main__":
    #create the thread
    processes = []
    for p in range(2):
        p = multiprocessing.Process(target=cpu_heavy, )
        processes.append(p)

    start = time.time()
    for p in processes:
        p.start()
        
    for p in processes:
        p.join()

    end = time.time()
    print(f"Finished in {end-start:.2f} secs.")


