import multiprocessing
import time
import random
import datetime

def process_function():
    # Generate a random number of seconds to sleep
    sleep_time = random.random()
    time.sleep(sleep_time)
    
    # Get the current time
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    
    # Print the current time
    print(f"Current time: {current_time}")

if __name__ == "__main__":
    # Create three separate processes
    processes = []
    for _ in range(3):
        p = multiprocessing.Process(target=process_function)
        processes.append(p)
        p.start()
    
    # Wait for all processes to finish
    for p in processes:
        p.join()