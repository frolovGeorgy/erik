from random import randint

arr = [randint(1, 10) for _ in range(10)]
len_arr = len(arr)

print(f'Список до сортировки: {arr}')

for moving_num_index in range(len_arr):
    for compared_num_index in range(moving_num_index, len_arr):
        if arr[moving_num_index] > arr[compared_num_index]:
            arr[compared_num_index], arr[moving_num_index] = arr[moving_num_index], arr[compared_num_index]

print(f'Список после сортировки: {arr}')
