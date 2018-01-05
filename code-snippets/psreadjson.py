from pprint import pprint as pp
from json import load

content = load(open('tmp.json'))  # json to an py object
print(type(content))
pp(content)