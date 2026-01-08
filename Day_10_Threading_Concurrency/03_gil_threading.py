## A program that runs 2 threads which performs a cpu intensive task

import threading
import time

def brew_tea():
    print(f"{threading.current_thread().name} has started brewing.")
    time.sleep(2)

    count = 0
    for _ in range(100_000_000):
        count += 1

    print(f"{threading.current_thread().name} has finished brewing...")

#create the thread and give it a name

thread1 = threading.Thread(target=brew_tea, name = "barrister1" )
thread2 = threading.Thread(target=brew_tea, name = "barrister2")

#start and join the thread with a given time

start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()

print(f"Total time taken = {end - start:.2f} seconds")






          