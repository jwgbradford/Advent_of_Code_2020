import json

input_file = open('input.txt', 'r')
input_data = input_file.read()
input_file.closed
data_list = input_data.split()
big_numbers = []
little_numbers = []
for data in data_list:
    if int(data) > 1010:
        big_numbers.append(int(data))
    elif int(data) < 1010:
        little_numbers.append(int(data))
    else:
        print('Number =', data)
print(big_numbers)
print(little_numbers)
for big_number in big_numbers:
    for little_number in little_numbers:
        if big_number + little_number == 2020:
            print('big number is', big_number)
            print('little_number is', little_number)
            print('big x little is', big_number * little_number)
            break