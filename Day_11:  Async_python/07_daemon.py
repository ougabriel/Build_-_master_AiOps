import threading
import time

def temp_check():
    while True:
        print("Checking temperature")
        time.sleep(2)


threading.Thread(target=temp_check, daemon=True).start()

print("Main program done.")