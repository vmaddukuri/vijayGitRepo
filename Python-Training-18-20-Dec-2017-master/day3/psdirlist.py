from os import listdir
from os.path import join, isdir, isfile
from pprint import pprint as pp


class ListOfDirectories:
    def __init__(self, *args):
        self.list_of_directories = args
        self.container = dict()
        # print(self.list_of_directories)
        self.read_list_of_directories()

    def get_abs_path_for_directory(self, dir_name, directory_items):
        temp = []

        for file_item in directory_items:
            temp.append(join(dir_name, file_item))

        return temp

    def read_list_of_directories(self):
        for dir_name in self.list_of_directories:

            dir_content = self.get_abs_path_for_directory(dir_name,
                                                          listdir(dir_name))

            file_names = list(filter(isfile, dir_content))
            dir_names = list(filter(isdir, dir_content))
            self.container[dir_name] = dict(files=file_names, dirs=dir_names)


dl = ListOfDirectories('/tmp', '/home/ravi')
pp(dl.container)
