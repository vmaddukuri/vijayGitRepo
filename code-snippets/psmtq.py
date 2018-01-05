import requests
from queue import Queue
import threading
import logging

fmt_str = "%(threadName)s: %(message)s"
logging.basicConfig(level=logging.INFO, format=fmt_str)


def robot(q):
    url = q.get()  # read urls form the Q, block's the  exec of the current thread
    payload = requests.get(url).content[:64]
    logging.error(payload)


def main():
    urls = ['http://python.org', 'http://kernel.org', 'http://linux.org']
    queue_obj = Queue()

    for url in urls:
        t = threading.Thread(target=robot, args=(queue_obj,))
        t.start()

    for url in urls:
        queue_obj.put(url)  # write into the Q


if __name__ == '__main__':
    main()
