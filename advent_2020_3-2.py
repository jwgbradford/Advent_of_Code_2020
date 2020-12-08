input_file = open('input3.txt', 'r')
input_data = input_file.readlines()
input_file.closed
paths = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
slope_height = len(input_data)
slope_width = len(input_data[0]) - 1
slope_index = slope_width - 1
total = 1
for i in range(len(paths)):
    angle = paths[i][0]
    drop = paths[i][1]
    print(angle, drop)
    position = 0
    height = 0
    tree = 0
    for j in range(slope_height):
        decent = input_data[height]
        if decent[position] == '#':
            tree += 1
        position = position + angle
        height = height + drop
        if height > slope_height:
            break
        if position > slope_index:
            position = position - slope_width
    total = total * tree
    print(total)