input_file = open('input3.txt', 'r')
input_data = input_file.readlines()
input_file.closed
angle = 3
position = 0
slope_width = len(input_data[0]) - 1
slope_index = slope_width - 1
tree = 0
for decent in input_data:
    if decent[position] == '#':
        tree += 1
    position = position + angle
    if position > slope_index:
        position = position - slope_width
print(tree)