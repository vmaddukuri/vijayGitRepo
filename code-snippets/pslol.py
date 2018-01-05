from pprint import pprint as pp


def by_uid(user):
    return int(user[2])


content = [current_line.rstrip().split(':') for current_line in open('passwd.txt') if current_line.strip()]
content = sorted(content, key=by_uid, reverse=True)

captions = ['login', 'passwd', 'uid', 'gid', 'gecos', 'home', 'shell']

for user_info in content:
    for title, value in zip(captions, user_info):  # parallel iteration
        print("{:>12} : {}".format(title, value))
    print()
