# A simple program that uses 4 processors to increment a count value

from multiprocessing import Process, Value 

def increment(counter):
    for _ in range(100_000):
        with counter.get_lock():
            counter.value += 1


if __name__ == "__main__":
    counter = Value('i', 0)
    processes = []

    for p in range(4):
        p = Process(target=increment, args=(counter, ))
        processes.append(p)

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print(f"The total number value is: {counter.value}")

