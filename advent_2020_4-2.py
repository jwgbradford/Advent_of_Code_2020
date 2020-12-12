import re 

EYE_COLOURS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def check_byr(passport_data):
    if passport_data.isdigit() and len(passport_data) == 4:
        if 1920 <= int(passport_data) <= 2002:
            #print('pass', 'our digits; at least 1920 and at most 2002', passport_data)
            return True
    #print('fail', passport_data)
    return False

def check_ecl(passport_data):
    if passport_data in EYE_COLOURS and len(passport_data) == 3:
        #print('pass', 'exactly one of: amb blu brn gry grn hzl oth.', passport_data)
        return True
    return False

def check_eyr(passport_data):
    if passport_data.isdigit() and len(passport_data) == 4:
        if 2020 <= int(passport_data) <= 2030:
            #print('pass', 'four digits; at least 2020 and at most 2030', passport_data)
            return True
    #print('fail', passport_data)
    return False

def check_hcl(passport_data):
    pattern = '#[0-9a-f]{6}'
    if re.search(pattern, passport_data) and len(passport_data) == 7:
        return True
    else:
        return False

def check_hgt(passport_data):
    if re.search('cm\Z', passport_data):
        height = int(passport_data[0:(len(passport_data) - 2)])
        if 150 <= height <=193:
            #print('pass', 'If cm, the number must be at least 150 and at most 193.', passport_data)
            return True
    elif re.search('in\Z', passport_data):
        height = int(passport_data[0:(len(passport_data) - 2)])
        if 59 <= height <= 76:
            #print('pass', 'If in, the number must be at least 59 and at most 76.', passport_data)
            return True
    #print('fail', passport_data)
    return False

def check_iyr(passport_data):
    if passport_data.isdigit() and len(passport_data) == 4:
        if 2010 <= int(passport_data) <= 2020:
            #print('pass', 'four digits; at least 2010 and at most 2020.', passport_data)
            return True
    #print('fail', 'four digits; at least 2010 and at most 2020.', passport_data)
    return False

def check_pid(passport_data):
    pattern = '\A\d{9}'
    if re.search(pattern, passport_data) and len(passport_data) == 9:
        return True
    else:
        return False

def validate(passport_entry):
    if (check_byr(passport_entry['byr']) and 
        check_ecl(passport_entry['ecl']) and 
        check_eyr(passport_entry['eyr']) and 
        check_hcl(passport_entry['hcl']) and 
        check_hgt(passport_entry['hgt']) and
        check_iyr(passport_entry['iyr']) and
        check_pid(passport_entry['pid'])):
        return True
    else:
        return False

input_file = open('input4.txt', 'r')
input_data = input_file.readlines()
input_file.closed

input_split = []
for entry in input_data:
    split_data = entry.split()
    input_split.append(split_data)
input_split.append([]) # add a blank line to trigger the last data read

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
        if key_list == required_fields and validate(temp_passport_entry):
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
print(len(invalid_passports))