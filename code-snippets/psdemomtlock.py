import threading
from time import sleep
from random import random
import logging

fmt_str = "%(threadName)s: %(message)s"
logging.basicConfig(level=logging.DEBUG, format=fmt_str)


def worker(delay, lock):
    t_id = threading.current_thread().ident
    t_name = threading.current_thread().name
    logging.debug('waiting for the lock')

    with lock:
        """critical section of the code"""
        logging.debug('acquired the lock')
        print(">> {}: waited : {} <<".format(t_name, delay))
        sleep(1)
        logging.debug('releases the lock')


def main():
    list_of_threads = list()
    lock_obj = threading.Lock()

    for item in range(1, 10):
        rand_value = random()
        t = threading.Thread(target=worker, name='T' + str(item), args=(rand_value, lock_obj))
        t.start()
        list_of_threads.append(t)

    # to make the main thread to waits for child to complete
    for threads in list_of_threads:
        threads.join()  # blocked call

    print('main thread terminates')


if __name__ == '__main__':
    main()
