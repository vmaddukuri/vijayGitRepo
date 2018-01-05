from fileinput import input, filename, filelineno

for line in input([r'C:\Users\madduv\Desktop\tmp.json']):
    print('{}:{}:{}'.format(filename(), filelineno(), line))
