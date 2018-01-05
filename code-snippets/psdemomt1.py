import threading
from time import sleep
from random import random


def worker(delay):
    t_id = threading.current_thread().ident
    t_name = threading.current_thread().name
    sleep(delay)
    print("{}: waited : {}".format(t_name, delay))


def main():
    list_of_threads = list()

    for item in range(1, 10):
        rand_value = random()
        t = threading.Thread(target=worker, name='T'+str(item), args=(rand_value,))
        t.start()
        list_of_threads.append(t)


    # to make the main thread to waits for child to complete
    for threads in list_of_threads:
        threads.join()  # blocked call

    print('main thread terminates')


if __name__ == '__main__':
    main()