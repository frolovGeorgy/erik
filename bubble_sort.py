from random import randint

sas = [randint(1, 10) for _ in range(10)]
len_sas = len(sas)

print(f'Список до сортировки: {sas}')

for moving_num_index in range(len_sas):
    for compared_num_index in range(moving_num_index, len_sas):
        if sas[moving_num_index] > sas[compared_num_index]:
            sas[compared_num_index], sas[moving_num_index] = sas[moving_num_index], sas[compared_num_index]
    # print(f'Список после {moving_num_index + 1} сортировки: {sas}')

print(f'Список после сортировки: {sas}')
