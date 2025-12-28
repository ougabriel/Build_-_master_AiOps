## A simple program that brews a tea based on its name.

from multiprocessing import Process
import time

def brew_tea(name):
    print(f"Start {name} tea brewing.")
    time.sleep(2)
    print(f"End of {name} tea brewing")


if __name__ == "__main__":
    tea_maker = [
        Process(target=brew_tea, args=(f"tea-maker #{i + 1}", ))
        for i in range(3)
    ]


#start all process
for p in tea_maker:
    p.start()

#wait for all to complete
for p in tea_maker:
    p.join()
    