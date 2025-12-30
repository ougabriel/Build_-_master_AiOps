# A simple program that boils milk and toasts the bun

import threading
import time

def boil_milk():
    print(f"The milk is boiling. ")
    time.sleep(4)
    print(f"The milk is boiled.")


def bun_toast():
    print(f"The bun is on the toaster.")
    time.sleep(2)
    print(f"The bun is toasted.")


t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=bun_toast)

start = time.time()
t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"Breakfast is now ready in {end-start:.2f} seconds.")