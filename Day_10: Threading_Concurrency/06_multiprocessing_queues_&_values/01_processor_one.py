# A simple program that uses threads to perform a cpu intensive task; such as crunching a large number.

import threading
import time

def cpu_heavy():
    print("Crunching the numbers.")
    total = 0
    for i in range(10**9):
        total += i
    print("Done with the crunch")

    
#create the thread
threads = []
for t in range(2):
    t = threading.Thread(target=cpu_heavy, )
    threads.append(t)

start = time.time()
for t in threads:
    t.start()
    
for t in threads:
    t.join()

end = time.time()
print(f"Finished in {end-start:.2f} secs.")


