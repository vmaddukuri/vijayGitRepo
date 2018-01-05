from pprint import pprint as pp

content = {}


for line in open('passwd.txt'):
    user_info = line.rstrip().split(':')
    user_name, shell = user_info[0], user_info[-1]

    # print(user_name, shell)

    if shell not in content:
        content[shell] = []

    content[shell].append(user_name)

pp(content)
