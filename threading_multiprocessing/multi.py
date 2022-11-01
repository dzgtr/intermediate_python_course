from multiprocessing import Process
import os
import time

def square_numbers():
    for i in range(100):
        i*i
        time.sleep(0.1)

processes = []
print(os.cpu_count())
num_processes = os.cpu_count()
# create processes
for i in range(num_processes):
    p = Process(target=square_numbers) # if a function has any arguments it's passed as a tuple with args=
    processes.append(p)
# start
for p in processes:
    p.start()
# join
for p in processes:
    p.join()        # join method in processes/threads means wait for the process to end
print("end main")
#----------------------------------------------------------------------------------------------------------
from threading import Thread
threads = []
num_threads = 10
for i in range(num_threads):
    t = Thread(target=square_numbers) # if a function has arguments it's passed as a tuple with args=
    threads.append(t)
# start
for t in threads:
    t.start()
# join
for t in threads:
    t.join()
print("end main")
