input_file = open('input4.txt', 'r')
input_data = input_file.readlines()
input_file.closed
input_split = []
for entry in input_data:
    split_data = entry.split()
    input_split.append(split_data)
input_split.append([])
temp_passport_entry = {}
valid_passports = {}
invalid_passports = {}
valid_UID = 1
invalid_UID = 1
required_fields = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
for data_slice in input_split:
    if len(data_slice) == 0:
        key_list = list(temp_passport_entry.keys())
        if 'cid' in key_list:
            key_list.remove('cid')
        key_list.sort()
        if key_list == required_fields:
            valid_passports[valid_UID] = temp_passport_entry
            valid_UID += 1
        else:
            invalid_passports[invalid_UID] = temp_passport_entry
            invalid_UID += 1
        temp_passport_entry = {}
    else:
        for entry in data_slice:
            key, value = entry.split(':')
            temp_passport_entry[key] = value
print(len(valid_passports))