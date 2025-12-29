from multiprocessing import Process
import time

def brew_tea():
    print("Start brewing...")

    count = 0
    for _ in range(100_000_000):
        count += 1
    
    print("End of brewing..")

#create the processes
if __name__ == "__main__":

    p1 = Process(target=brew_tea)
    p2 = Process(target=brew_tea)

    # start and join the process in a given time
    start = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()

    print(f"Multiprocessing finished the brewing in {end - start:.2f} seconds.")



