import multiprocessing
import time

def CPU_heavy_math(number):
    print(f"Processing large number {number}...")
    # Simulate a heavy math calculation
    count = 0
    for i in range(10000000):
        count += i
    print(f"Finished number {number}")
    return count

if __name__ == "__main__":
    processes = []
    # Spawning 3 separate processes across multiple CPU cores
    for i in range(3):
        p = multiprocessing.Process(target=CPU_heavy_math, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()