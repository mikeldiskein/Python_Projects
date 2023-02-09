# def hide_card(card_number):
#     card_number = card_number.replace(' ', '')
#     card_number = '*' * 12 + card_number[12:]
#
#     return card_number
#
# print(hide_card('905 678123 45612 56'))

# def same_parity(numbers):
#     if not numbers:
#         return numbers
#     else:
#         if numbers[0] % 2 == 0:
#             numbers = list(filter(lambda x: x % 2 == 0, numbers))
#             return numbers
#         else:
#             numbers = list(filter(lambda x: x % 2 == 1, numbers))
#             return numbers
#
#
# print(same_parity([-7, 0, 67, -9, 70, -29, 90]))


# def is_valid(string):
#     if not string:
#         return False
#     elif ' ' in string:
#         return False
#     elif len(string) < 4 or len(string) > 6:
#         return False
#     elif not string.isdigit():
#         return False
#     else:
#         return True
#
#
# print(is_valid('49 83'))


# def print_given(*args, **kwargs):
#     for arg in args:
#         print(arg, type(arg))
#     sorted_kwargs = sorted(kwargs.items(), key=lambda x: x[0])
#     sorted_kwargs = dict(sorted_kwargs)
#     for key, val in sorted_kwargs.items():
#         print(key, val, type(val))


# def convert(string):
#     upper_counter = 0
#     lower_counter = 0
#     for i in string:
#         if not i.isalpha():
#             continue
#         if i.islower():
#             lower_counter += 1
#         elif i.isupper():
#             upper_counter += 1
#     if lower_counter >= upper_counter:
#         string = string.lower()
#     else:
#         string = string.upper()
#
#     return string


# def filter_anagrams(word, words):
#     if not words:
#         return []
#     template = sorted(word)
#     anagrams = []
#     for i in words:
#         if sorted(i) == template:
#             anagrams.append(i)
#
#     return anagrams
#
#
# word = 'abba'
# anagrams = ['aabb', 'abcd', 'bbaa', 'dada']
#
# print(filter_anagrams(word, anagrams))


# def likes(names):
#     if not names:
#         return 'Никто не оценил данную запись'
#     if len(names) == 1:
#         return f'{names[0]} оценил(а) данную запись'
#     if len(names) == 2:
#         return f'{names[0]} и {names[1]} оценили данную запись'
#     if len(names) == 3:
#         return f'{names[0]}, {names[1]} и {names[3]} оценили данную запись'
#     if len(names) >= 4:
#         return f'{names[0]}, {names[1]} и {len(names) - 2} других оценили данную запись'


# def index_of_nearest(numbers, number):
#     if not numbers:
#         return -1
#
#     minimal_difference = 10**6
#     indexes_and_differences = {}
#     for ind, num in enumerate(numbers):
#         current_diff = abs(num - number)
#         if current_diff < minimal_difference:
#             minimal_difference = current_diff
#         indexes_and_differences[ind] = current_diff
#
#     needed_values = dict(filter(lambda x: int(x[1]) == minimal_difference, indexes_and_differences.items()))
#     return min(needed_values)
#
#
# print(index_of_nearest([9, 5, 3, 2, 11], 4))


# def spell(*args):
#     if not args:
#         return {}
#     result = {}
#     for word in args:
#         if word[0].lower() in result:
#             if result[word[0].lower()] < len(word):
#                 result[word[0].lower()] = len(word)
#         else:
#             result[word[0].lower()] = len(word)
#
#     return result


# def choose_plural(amount, declensions):
#     if 11 <= amount % 100 < 20:
#         return f'{amount} {declensions[2]}'
#     elif amount % 10 == 1:
#         return f'{amount} {declensions[0]}'
#     elif 2 <= amount % 10 < 5:
#         return f'{amount} {declensions[1]}'
#     elif 5 <= amount % 10 <= 9 or amount % 10 == 0:
#         return f'{amount} {declensions[2]}'
#
#
# print(choose_plural(21, ('пример', 'примера', 'примеров')))

# from itertools import permutations
#
#
# def get_biggest(numbers):
#     if not numbers:
#         return -1
#     numbers_perms = list(permutations(numbers))
#     for i in range(len(numbers_perms)):
#         numbers_perms[i] = tuple(map(str, numbers_perms[i]))
#     result_numbers = list(map(int, [''.join(result_number) for result_number in numbers_perms]))
#     return max(result_numbers)
#
#
# print(get_biggest([1, 2, 3]))


# d1, d2, d3 = int(input()), int(input()), int(input())
#
# sums = set()
#
# sums.add(d1 + d3 + d2)
# sums.add(d1 + d3 + d3 + d1)
# sums.add(d1 + d1 + d2 + d2)
# sums.add(d2 + d3 + d3 + d2)
#
# print(min(sums))


# en, ru = 'AaBCcEeHKMOoPpTXxy', 'АаВСсЕеНКМОоРрТХху'
#
# letters = [input() for _ in range(3)]
#
# count_ru, count_en = 0, 0
# for letter in letters:
#     if letter in en:
#         count_en += 1
#     elif letter in ru:
#         count_ru += 1
# if count_ru == 3:
#     print('ru')
# elif count_en == 3:
#     print('en')
# elif count_en < 3 and count_ru < 3:
#     print('mix')


# n, x, y, a, b = (int(i) for i in input().split())
#
# numbers = [i for i in range(1, n + 1)]
#
# numbers = numbers[:x-1] + numbers[x-1:y][::-1] + numbers[y:]
# numbers = numbers[:a-1] + numbers[a-1:b][::-1] + numbers[b:]
#
# print(*numbers)


# numbers = [int(i) for i in input().split()]
#
# repeated = {}
# for num in numbers:
#     repeated[num] = repeated.get(num, 0) + 1
#
# repeated = dict(filter(lambda x: x[1] > 1, repeated.items()))
# list_of_repeated = sorted([i for i in repeated.keys()])
#
# print(*list_of_repeated)


# numbers = [i for i in range(1, int(input()) + 1)]
# groups = {}
# for num in numbers:
#     digits_sum = 0
#     while num > 0:
#         digits_sum += num % 10
#         num //= 10
#     groups[digits_sum] = groups.get(digits_sum, 0) + 1
# print(max(groups.values()))


# n = int(input())
# common_languages = set(lan for lan in input().split(', '))
# for _ in range(n - 1):
#     languages = set(lan for lan in input().split(', '))
#     common_languages &= languages
#
# if not common_languages:
#     print('Сериал снять не удастся')
# else:
#     print(', '.join(sorted(list(common_languages))))


# str_vov = 'а, у, о, ы, и, э, я, ю, ё, е'.replace(', ', '')
# example = input()
# indexes_vov_ex = []
# for i in range(len(example)):
#     if example[i] in str_vov:
#         indexes_vov_ex.append(i)
# for _ in range(int(input())):
#     word = input()
#     indexes_vov = []
#     for i in range(len(word)):
#         if word[i] in str_vov:
#             indexes_vov.append(i)
#     if indexes_vov == indexes_vov_ex:
#         print(word)


# n = int(input())
# boxes = [input() for _ in range(n)]
# m = int(input())
# names = (input() for _ in range(m))
#
# domen = '@beegeek.bzz'
# for name in names:
#     if name + domen in boxes:
#         index = 1
#         while name + str(index) + domen in boxes:
#             index += 1
#         boxes.append(name + str(index) + domen)
#     else:
#         boxes.append(name + domen)
#
# print(*boxes[-m:], sep='\n')
from pprint import pprint

# def bytes_to(summary):
#     counter = 0
#     while summary >= 1024:
#         summary /= 1024
#         counter += 1
#     if counter == 1:
#         return f'{round(summary)} KB'
#     elif counter == 2:
#         return f'{round(summary)} MB'
#     elif counter == 3:
#         return f'{(round(summary))} GB'
#     else:
#         return f'{(round(summary))} B'
#
#
# with open('files.txt', mode='r', encoding='utf-8') as files:
#     files = list(files)
#     main_dict = {}
#     for i in files:
#         string = i.split()
#         file_name = string[0]
#         file_type = string[0].split('.')[1]
#         memory_number = string[1]
#         memory_value = string[2]
#         main_dict[file_type] = main_dict.get(file_type, {})
#         main_dict[file_type][file_name] = (memory_number, memory_value)
#     main_dict = dict(sorted(main_dict.items()))
#
#     for i in main_dict:
#         main_dict[i] = dict(sorted(main_dict[i].items()))
#
#     for i in main_dict:
#         summary_in_bytes = 0
#         print(*main_dict[i].keys(), sep='\n')
#         for j in main_dict[i]:
#             if main_dict[i][j][1] == 'B':
#                 summary_in_bytes += int(main_dict[i][j][0])
#             elif main_dict[i][j][1] == 'KB':
#                 summary_in_bytes += int(main_dict[i][j][0]) * 1024
#             elif main_dict[i][j][1] == 'MB':
#                 summary_in_bytes += int(main_dict[i][j][0]) * 1024**2
#             elif main_dict[i][j][1] == 'GB':
#                 summary_in_bytes += int(main_dict[i][j][0]) * 1024**3
#         print('-' * 10)
#         print(f'Summary: {bytes_to(summary_in_bytes)}')
#         print()


# from datetime import date
#
# dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11), date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]
#
# for date in dates:
#     if date.month < 4:
#         Q = 1
#     elif 3 < date.month < 7:
#         Q = 2
#     elif 6 < date.month < 10:
#         Q = 3
#     else:
#         Q = 4
#     print(f'{date.year}-Q{Q}')

# from datetime import date
#
#
# def get_min_max(dates):
#     if not dates:
#         return ()
#     min_date = min(dates)
#     max_date = max(dates)
#     return min_date, max_date
#
#
# dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
#
# print(get_min_max(dates))

# from datetime import date
#
#
# def get_date_range(start, end):
#     start_in_num = start.toordinal()
#     end_in_num = end.toordinal()
#     if start_in_num > end_in_num:
#         return []
#     for i in range(start_in_num, end_in_num + 1):
#         print(date.fromordinal(i))
#
#
# date1 = date(2021, 10, 1)
# date2 = date(2021, 10, 5)
#
# get_date_range(date1, date2)


# from datetime import date
#
#
# def saturdays_between_two_dates(start, end):
#     counter = 0
#     if start < end:
#         for i in range(start.toordinal(), end.toordinal() + 1):
#             if date.fromordinal(i).weekday() == 5:
#                 counter += 1
#     else:
#         for i in range(end.toordinal(), start.toordinal() + 1):
#             if date.fromordinal(i).weekday() == 5:
#                 counter += 1
#     return counter
#
#
# date1 = date(2020, 7, 26)
# date2 = date(2020, 7, 2)
# print(saturdays_between_two_dates(date1, date2))

# from datetime import date
#
# # присваиваем самую раннюю дату урагана в переменную first_date
# florida_hurricane_dates = [date(2000, 10, 12), date(2001, 8, 25)]
#
# first_date = min(florida_hurricane_dates)
#
# # конвертируем дату в ISO и RU формат
# iso = 'Дата первого урагана в ISO формате: ' + first_date.isoformat()
# ru = 'Дата первого урагана в RU формате: ' + first_date.strftime('%d.%m.%Y')
# us = 'Дата первого урагана в US формате: ' + first_date.strftime('%m/%d/%Y')
#
# print(iso)
# print(ru)
# print(us)


# from datetime import date
#
# dates = [date.fromisoformat(input()) for _ in range(2)]
#
# print(min(dates).strftime('%d-%m (%Y)'))


# from datetime import date
#
# n = int(input())
#
# dates = [date.fromisoformat(input()) for _ in range(n)]
#
# for date in sorted(dates):
#     print(date.strftime('%d/%m/%Y'))


from datetime import date

# def print_good_dates(dates):
#     good_dates = []
#     for dat in dates:
#         if int(dat.year) == 1992 and int(dat.month) + int(dat.day) == 29:
#             good_dates.append(dat)
#
#     for good in sorted(good_dates):
#         print(good.strftime('%B %d, %Y'))


# from datetime import date
#
#
# def is_correct(dat):
#     try:
#         day, month, year = dat.split('.')
#         my_date = date(int(year), int(month), int(day))
#         return True
#     except ValueError:
#         return False
#
#
# counter = 0
# while True:
#     dat = input()
#     if dat == 'end':
#         break
#     if is_correct(dat):
#         print('Корректная')
#         counter += 1
#     else:
#         print('Некорректная')
# print(counter)


# from datetime import datetime
#
# times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26),
#                       datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59),
#                       datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53),
#                       datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3),
#                       datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5),
#                       datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54),
#                       datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45),
#                       datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57),
#                       datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42),
#                       datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12),
#                       datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27),
#                       datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41),
#                       datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44),
#                       datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]

# counter_1 = 0
# counter_2 = 0
# for time in times_of_purchases:
#     if time.hour >= 12:
#         counter_2 += 1
#     else:
#         counter_1 += 1
#
# if counter_1 > counter_2:
#     print('До полудня')
# else:
#     print('После полудня')


# from datetime import date, time, datetime
#
# dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4),
#          date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24),
#          date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]
#
# times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59),
#          time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2),
#          time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]
#
#
# datetimes = []
# for date_, time_ in zip(dates, times):
#     datetimes.append(datetime.combine(date_, time_))
#
# for datetime_ in sorted(datetimes, key=lambda x: x.second):
#     print(datetime_)


from datetime import datetime

data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28' ),
        'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'),
        'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'),
        'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'),
        'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'),
        'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'),
        'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'),
        'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'),
        'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'),
        'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'),
        'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}

time = 10**6
for student in data.items():
    start = datetime.timestamp(datetime.strptime(student[1][0], '%d.%m.%Y %H:%M:%S'))
    end = datetime.timestamp(datetime.strptime(student[1][1], '%d.%m.%Y %H:%M:%S'))
    if end - start < time:
        time = end - start
        name = student[0]

print(name)


from datetime import datetime

with open('C:/Users/mikha/Downloads/diary.txt', mode='r', encoding='utf-8') as file:
    notes = file.read().split('\n\n')
    notes = sorted(notes, key=lambda x: datetime.strptime(x.split('\n')[0], '%d.%m.%Y; %H:%M'))
    for note in notes:
        print(note)
        print()

print('Bye!')




