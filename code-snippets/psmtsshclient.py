import pyexcel

book = pyexcel.get_book(file_name='hosts.xlsx')
for sheet in book:
    for row in sheet:
        print(row[0], row[-1])