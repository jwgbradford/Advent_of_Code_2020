import re

input_file = open('input2.txt', 'r')
input_data = input_file.readlines()
input_file.closed

success = 0 
for line in input_data:
    pattern = '\d+'
    first, last = re.findall(pattern, line)
    pattern = '\D:'
    letter_code = re.findall(pattern, line)[0]
    letter_code = letter_code[0]
    line_parts = re.split('\s+', line)
    password = line_parts[2]
    if len(password) >= int(first):
        if password[int(first) - 1] == letter_code:
            if len(password) < int(last) or password[int(last) - 1] != letter_code:
                print('success')
                success += 1
        elif password[int(first) - 1] != letter_code:
            if len(password) >= int(last) and password[int(last) - 1] == letter_code:
                print('success')
                success += 1
    else:
        print('failure')
print(success)