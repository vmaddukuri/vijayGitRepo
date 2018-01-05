"""
PackageManager

name
version

__init__()
get_information()
"""


class PackageManager:
    arch = 'x86_64'  # member variable

    def __init__(self, name, version, arch=None):
        self.__name = name
        self.version = version

        if arch:
            self.arch = arch

    def __get_information(self):
        print('name :', self.__name)
        print('version :', self.version)
        print('system :', self.arch)

    def wrapper(self):
        self.__get_information()

pm = PackageManager(input('enter the name :'), '2.2.18', 'sprac')
pm.wrapper()
# print(pm.__name)
print()
