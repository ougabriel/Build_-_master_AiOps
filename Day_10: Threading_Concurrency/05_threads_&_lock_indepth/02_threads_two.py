# A simple program that uses 1cpu processor on 2 threads.
# A simple program that brews tea based on its type in a given time

# This program demonstrates concurrency on a single CPU using threads, not parallelism

from os import wait
import threading
import time

def brew_tea(type, wait_time):
    print(f"Your {type} tea is brewing...")
    time.sleep(wait_time)
    print(f"Your {type} tea is ready.")

# create the threads
t1 = threading.Thread(target=brew_tea, args=("ginger", 2))
t2 = threading.Thread(target=brew_tea, args=("lemon", 4))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print(f"Your {type} tea is ready in {end-start:.2f} secs.")

# Process = building
# Thread = people inside
# Concurrency = switching tasks
# Parallelism = multiple people working at once
