from os import listdir
from os.path import join, isfile, isdir, getsize, getmtime
from time import ctime

path = '/tmp'  # unix
print(listdir(path))

abs_path = path +'/'+'+~JF5091943612261187301.tmp'
print(abs_path)
abs_path = join(path, '+~JF5091943612261187301.tmp')
print(abs_path)
print()
print(isdir(abs_path))
print(isfile(abs_path))
print()
print(getsize(abs_path))
print(getmtime(abs_path))
print(ctime(getmtime(abs_path)))

