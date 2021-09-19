# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

def read_file(file):
    with open(file, 'r') as file:
        for line in file:
            line = line[:-1]
            if not line:
                continue
            yield line


def grouped_evens_gen(file_name, count_char=16):
    read_file_gen = read_file(file_name)
    last_data_time = read_file_gen.__next__
    # print(last_data_time)
    count = 0
    for line in read_file_gen:
        # print(line)
        data_time, res = line.split('] ')
        data_time = data_time[1:]
        res = res.strip()
        group_data_time = data_time[:count_char]
        if last_data_time != group_data_time:
            yield last_data_time, count
            last_data_time = group_data_time
            count = 1 if res == 'NOK' else 0
        elif last_data_time == group_data_time and res == 'NOK':
            count += 1
    if count > 0:
        yield last_data_time, count


file_name = 'events.txt'
grouped_events = grouped_evens_gen(file_name, count_char=16)
n = 0
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
