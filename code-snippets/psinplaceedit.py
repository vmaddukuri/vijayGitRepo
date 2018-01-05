"""inplace edit"""
from fileinput import input, filename
from glob import glob
from pprint import pprint as pp
import re
from sys import stdout

py_files = glob('*.dat')

pattern = r'\bline\b'
replacement = 'current_line'

for current_line in input(py_files, inplace=True, backup='.bak'):
    print(re.sub(pattern, replacement, current_line), end='')
    print('-' * 60, file=stdout)
