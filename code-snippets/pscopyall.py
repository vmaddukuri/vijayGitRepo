# binary
# wb, rb, ab

def copy_all(*args):
    try:
        with open(args[-1], 'w') as fw:
            for file_name in args[:-1]:
                fw.write(file_name.center(60, '-') + '\n')
                fw.write(open(file_name).read())
                fw.write('-' * 60 + "\n")

    except (FileNotFoundError, IOError) as err:
        print(err)


copy_all('/etc/hostname', '/etc/resolv.conf', 'testit')
