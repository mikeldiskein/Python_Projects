# функции encode и decode
# кодировка и декодировка символов
# в определённом стандарте представления (utf-8, utf-16 etc.)

# модуль io - помогает в позиционировании в файле

# file.read() - в символах
# file.seek() - в байтах

# file.name
# file.mode
# file.encoding
# file.closed
#
# file.readable
# file.writable
# file.seekable
#
# file.truncate() ?
# file.flush() ?

# class InOutBlock:
#     def __enter__(self):
#         print('Coming in the code block')
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('Getting out the code block')
#
#
# def ff():
#     with InOutBlock() as in_out:
#         print('Some code')
#         return
#
#
# ff()
import time
import os

path = 'C:/Windows/help'
path_normalized = os.path.normpath(path)
print(path_normalized)

count = 0
for dirpath, dirnames, filenames in os.walk(path_normalized):
    print('*' * 27)
    print(dirpath, dirnames, filenames)
    print(os.path.dirname(dirpath))
    print(__file__, os.path.dirname(__file__))

    # count += len(filenames)
#     for file in filenames:
#         full_file_path = os.path.join(dirpath, file)
#         sec = os.path.getctime(full_file_path)
#         date = time.gmtime(sec)
#         if date[0] == 2021 and date[1] == 6:
#             print(full_file_path, sec, date)
# print(count)







