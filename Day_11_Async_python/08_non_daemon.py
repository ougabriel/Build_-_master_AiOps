import threading
import time

def temp_check():
    while True:
        print("Checking temperature")
        time.sleep(2)


threading.Thread(target=temp_check, daemon=False).start()

print("Main program done.")