import multiprocessing
from pprint import pprint as pp
import os
pp(dir(os))


def task_set():
    p_name = multiprocessing.current_process().name
    p_id = multiprocessing.current_process().ident

    print("{} : {}".format(p_name, p_id))


def main():
    print("parent process id :", multiprocessing.current_process().ident)
    for item in range(5):
        p = multiprocessing.Process(target=task_set)
        p.start()

    # join

    for child in multiprocessing.active_children():
        child.join()


if __name__ == '__main__':
    main()
