import re

input_file = open('input2.txt', 'r')
input_data = input_file.readlines()
input_file.closed

success = 0 
for line in input_data:
    pattern = '\d+'
    lower, upper = re.findall(pattern, line)
    pattern = '\D:'
    letter_code = re.findall(pattern, line)[0]
    letter_code = letter_code[0]
    pattern = '[' +letter_code + ']'
    password_match = re.findall(pattern, line)
    if len(password_match) >= int(lower) and len(password_match) <= int(upper):
        print('success')
        success += 1
    else:
        print('failure')

print(success)