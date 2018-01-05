import re
from fileinput import input, filename, filelineno


def grep_me(pattern, file_names):
    for current_line in input(file_names):
        if re.search(pattern, current_line, re.I):
            content = "{}:{}:{}".format(filename(), filelineno(), current_line)
            print(current_line, end='')


pattern = '^root'
pattern = 'bash$'
pattern = 'b.t'
pattern = 'b[aeiou]t'  # char set
pattern = 'b[^aeiou]t'  # char set
#grep_me(pattern, ['data.dat'])
pattern = r'\b[789][0-9]{9}\b'
pattern = r'\b([5-9][0-9]{2})\b|\b([1-9][0-9]{3}[0-9]*)\b'
pattern = r'\b([5-9]\d{2})\b|\b([1-9]\d{3}\d*)\b'
pattern = r'\b([5-9]\d{2})\b|\b([1-9]\d\d\d+)\b'
pattern = r'(\d+)?\.\d+\b'
grep_me(pattern, ['passwd.dat'])
