try:
    fp = open(r'passwd.txt')

    for ln_no, current_line in enumerate(fp, 1):
        if ln_no % 5  == 0:
            print("{}:{}".format(ln_no, current_line), end='')


    fp.close()
except (FileNotFoundError, IOError) as err:
    print(err)