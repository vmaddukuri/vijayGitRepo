from os import listdir
from os.path import join, isfile, getsize, getmtime, basename
from time import ctime
from pprint import pprint as pp


class DirectoryListing:
    def __init__(self, *args):
        self.container = dict()
        self.directories = args
        self.__read_directories()

    def __read_directories(self):
        for dir_name in self.directories:
            directory_items = [join(dir_name, item) for item in listdir(dir_name)]

            for file_name in filter(isfile, directory_items):
                file_properties = [getsize(file_name), ctime(getmtime(file_name))]
                file_name = basename(file_name)
                self.container.setdefault(dir_name, {})[file_name] = file_properties


if __name__ == '__main__':
    dl = DirectoryListing('/tmp', '/data')
    pp(dl.container)
