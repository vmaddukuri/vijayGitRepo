#   demo for IO
try:
    name = input('enter the name :')
    city = input('enter the area :')
    zip_code = int(input('enter the postal zip code :'))

    print('name :', name)
    print('city :', city)
    print(zip_code)
    print(type(zip_code))
except ValueError as err:
    print(err)

# print('next stat after try except block')
