# try:
#     print(10 / i)
# except:
#     print('На ноль делить нельзя!')

#
# try:
#     print(10 / i)
# except ZeroDivisionError as exc:
#     print(f'вот что пошло не так: {exc}; но мы ещё на плаву. '
#           f'Параметры: {exc.args}')


# стек вызова функций в режиме debug

# try:
#     10 / i
# except ZeroDivisionError:
#     print('на ноль делить нельзя')
# else:
#     print('всё намана')
# finally:
#     print('я делал свою работу старательно')


# def greet_person(person_name):
#
#     if person_name == 'Robert':
#         raise BaseException("We don't like you, Robert")
#     print(f'Hi there {person_name}')
#
#
# greet_person('Dolly')
# greet_person('Robert')

# Проброс исключений
# try:
#     raise NameError('Hi there')
# except NameError as exc:
#     print(f'Исключение типа {type(exc)} пролетело мимо!'
#           f' его параметры: {exc.args}')
#     raise


# try:
#     raise NameError('Hi there')
# except NameError as exc:
#     print(f'Поймано исключение типа {type(exc)}')
#     raise TypeError('Hi here')  # from exc


# class HeroDiedError(Exception):
#     pass
#
#
# class GameOverError(Exception):
#     pass
#
#
# try:
#     raise HeroDiedError('Рядовой Райан')
# except HeroDiedError as exc:
#     print(f'Поймано исключение {exc}')
#     raise GameOverError('Миссия провалена')


# class DivisionError(Exception):
#     def __init__(self, message, input_data=None):
#         self.message = message
#         self.input_data = input_data
#
#     def __str__(self):
#         return self.message
#
#
# def division(a, b):
#     if a < b:
#         raise DivisionError('Нельзя делить меньшее на большее', input_data=dict(a=a, b=b))
#     return a/b
#
#
# try:
#     print(division(5, 2))
# except DivisionError as exc:
#     print(f'Поймано моё исключение {exc}, входные данные при'
#           f' ошибке {exc.input_data}')


import warnings


def greet_person(person_name):  
    if person_name == 'Robert':
        warnings.warn('Again this Robert...')
    print(f'Hi there {person_name}')


greet_person('Robert')
print('Process is running')
for i in range(10):
    print(f'i={i}')
