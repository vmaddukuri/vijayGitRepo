from pprint import pprint as pp

content = sorted([current_line.split(':')[0] for current_line in open('passwd.txt')])

content = [current_line.split(':')[0] for current_line in open('passwd.txt') if current_line.startswith('a')]
pp(content)

