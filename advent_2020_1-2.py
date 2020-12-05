input_file = open('input.txt', 'r')
input_data = input_file.read()
input_file.closed
data_list = input_data.split()
sorted_numbers = []
for data in data_list:
    sorted_numbers.append(int(data))
sorted_numbers.sort(reverse=True)
for large_number in sorted_numbers:
    for small_count in range(len(sorted_numbers) - 1, 0, -1):
        for mid_count in range(small_count - 1, 0, -1):
            number_sum = large_number + sorted_numbers[mid_count] + sorted_numbers[small_count]
            if number_sum == 2020:
                print('large number is', large_number)
                print('mid number is', sorted_numbers[mid_count])
                print('small number is', sorted_numbers[small_count])
                print('product is', large_number * sorted_numbers[mid_count] * sorted_numbers[small_count])
                raise SystemExit
            elif number_sum > 2020:
                break