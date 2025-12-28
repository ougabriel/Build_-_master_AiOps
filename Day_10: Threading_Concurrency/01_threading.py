# A basic program that takes an order and brews the tea order
##
#
import threading
import time

def tea_order():
    for i in range(1, 4):
        print(f"We are preparing your tea order {i}")
        time.sleep(3)

def brew_tea():
    for i in range(1, 4):
        print(f"You tea order {i} has been brewed.")
        time.sleep(5)

#create the thread

tea_order_thread = threading.Thread(target = tea_order)
brew_tea_thread = threading.Thread(target = brew_tea)

#start the thread

tea_order_thread.start()
brew_tea_thread.start()

#wait for both to finish

tea_order_thread.join()
brew_tea_thread.join()

print("All orders are taken and brewed")

