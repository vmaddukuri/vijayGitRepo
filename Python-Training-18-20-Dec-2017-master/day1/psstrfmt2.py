"""demo for the string formatting {:fmt-str}"""

name, age, gender = 'sarah', 3, 'female'  # parallel assignment

print("|{}|{}|{}|".format(name, age, gender))
print("|{:>22}|{:>9}|{:>16}|".format(name, age, gender))
print("|{:<22}|{:<9}|{:<16}|".format(name, age, gender))
print("|{:^22}|{:^9}|{:^16}|".format(name, age, gender))

print("|{:22}|{:9}|{:16}|".format(name, age, gender))  # default justify`
print("|{:22}|{:9.2f}|{:16}|".format(name, age, gender))  # default justify`
