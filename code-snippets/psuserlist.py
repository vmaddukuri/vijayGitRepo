def get_user_list(data_file, target_file):
    try:
        list_of_users = list()

        for current_line in open(data_file):
            login = current_line.split(':')[0]
            list_of_users.append(login)

        with open(target_file, 'w') as fw:  # context manager
            for line_no, user in enumerate(sorted(list_of_users), 1):
                content = "{:>6}  {}".format(line_no, user)
                print(content)
                fw.write(content + "\n")

    except (FileNotFoundError, IOError) as err:
        print(err)


get_user_list('passwd.txt', 'passwd.dat')
