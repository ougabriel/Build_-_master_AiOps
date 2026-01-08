# A simple program that counts and locks and gives the final count
# A mutex is a lock that prevents multiple threads from changing the same data at the same time.

import threading

counter = 0
lock = threading.Lock()

def increament():
    global counter
    for _ in range(100_000):
        with lock:
            counter += 1

#create the threads
threads = []
for _ in range(10):
    t = threading.Thread(target=increament)
    threads.append(t)

for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Counting complement: final counter {counter}.")



# What this program is doing 

# You have shared data → counter

# You have multiple threads → 10 threads

# Each thread increments the counter 100,000 times

# A mutex (lock) ensures only one thread updates the counter at a time
# Final answer should be 1000000.... that is 10 * 100_000