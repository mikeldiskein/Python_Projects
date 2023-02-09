import time


# from pprint import pprint
#
#
# def matrix(some_list):
#     def multiply_column(x):
#         res = []
#         for elem in some_list:
#             res.append(elem * x)
#         return res
#
#     return multiply_column
#
#
# my_numbers = [3, 4, 5, 6, 2, 8, 11]
# matrix_on_my_numbers = matrix(my_numbers)
# # print(matrix_on_my_numbers(2))
#
# pprint(list(map(matrix_on_my_numbers, my_numbers)))


# class Multiplier:
#     def __init__(self, n):
#         self.n = n
#
#     def __call__(self, x):
#         return x * self.n
#
#
# my_numbers = [3, 4, 5, 6, 2, 8, 11]
# by_100500 = Multiplier(100500)
# # result = by_100500(42)
# # print(result)
#
# result = map(by_100500, my_numbers)
# print(*list(result), sep='\n')
#
# print(callable(by_100500))

# декораторы


#
#
# def time_track(func, *args, **kwargs):
#     started_at = time.time()
#     result = func(*args, **kwargs)
#     ended_at = time.time()
#     elapsed = round(ended_at - started_at, 4)
#     print(f'Функция работала {elapsed} секунд(ы)')
#     return result
#
#
# def digits(*args):
#     total = 1
#     for number in args:
#         total *= number ** 5000
#     return len(str(total))
#
#
# result = time_track(digits, 3141, 5926, 2718, 2818)
# print(result)


# def time_track(func):
#     def surrogate(*args, **kwargs):
#         started_at = time.time()
#         result = func(*args, **kwargs)
#         ended_at = time.time()
#         elapsed = round(ended_at - started_at, 4)
#         print(f'Function was working {elapsed} seconds')
#         return result
#
#     return surrogate
#
#
# # timed_digits = time_track(digits)
# # result = timed_digits(3141, 5926, 2718, 2818)
# # print(result)
#
# # digits = time_track(digits)
# # print(digits(3141, 5926, 2718, 2818))
#
#
# @time_track
# def digits(*args):
#     total = 1
#     for number in args:
#         total *= number ** 5000
#     return len(str(total))
#
#
# print(digits(3141, 5926, 2718, 2818))


# продвинутые декораторы


def get_time_track(precision):
    def time_track(func):
        def surrogate(*args, **kwargs):
            started_at = time.time()
            result = func(*args, **kwargs)
            ended_at = time.time()
            elapsed = round(ended_at - started_at, precision)
            print(f'Function was working {elapsed} seconds')
            return result

        return surrogate

    return time_track


#
#
# def digits(*args):
#     total = 1
#     for number in args:
#         total *= number ** 5000
#     return len(str(total))

@get_time_track(precision=6)
def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))


# time_track_precision_6 = get_time_track(precision=4)
# digits = time_track_precision_6(digits)
result = digits(3141, 5926, 2718, 2818)
print(result)
