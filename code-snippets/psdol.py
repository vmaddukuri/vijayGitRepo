"""demo for the csv parser"""
from csv import reader
from pprint import pprint as pp


def parse_csv_file(csv_file):
    """
    parse_csv_file, parsers the given csv file and returns the dict
    :param csv_file: str
    :return: dict
    """
    container = dict()

    try:
        for user_info in reader(open(csv_file), delimiter=':'):
            login, shell = user_info[0], user_info[-1]
            container.setdefault(shell, list()).append(login)

        return container

    except (FileNotFoundError, IOError) as err:
        print(err)


data_set = parse_csv_file('passwd.txt')
#pp(data_set)

for shell, list_of_user_names in data_set.items():
    print(shell)

    for user in list_of_user_names:
        print("\t", user)
    print()
    