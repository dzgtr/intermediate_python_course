from threading import Thread, Lock, current_thread
from queue import Queue
import time

database_value = 0

def increase(lock):
    global database_value
    lock.acquire()                  # locked
    local_copy = database_value
    # processing
    local_copy += 1
    time.sleep(0.1)                 # on sleep python switches to another thread, UNLESS locked
    database_value = local_copy
    lock.release()                  # unlocked

# recommended way of using a lock is:
# with lock:
#   ...commands...
# no need to .release() after

def worker(q, lock):
    while True:         # without .daemon=true it will end when the main thread ends, with .daemon=false use break
        value = q.get()
        # processing..
        with lock:      # without lock sometimes threads write on the same line
            print(f"in {current_thread().name} got {value}")
        q.task_done()

if __name__ == "__main__":

    lock = Lock()
    print("start value", database_value)
    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("end value", database_value)
    print("end main")
#----------------------------------------------------------------------------------------------------------

    q = Queue() # queue is FIFO, .put() puts and item into it and .get() pops the first item putted into the queue
    # q.put(1)
    # q.put(2)
    # q.put(3)
    #
    # # 3 2 1 -->
    # first = q.get()
    # print(first)
    # q.task_done() # when done processing always do this if the queue is not empty
    # q.join() # locks the main thread until all items in the queue are processed

    num_threads = 10
    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
#        thread.daemon=True # background thread that dies when the main thread dies
        thread.start()

    for i in range(1, 21):
        q.put(i)

    q.join()