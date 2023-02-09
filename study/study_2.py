from time import time


def abundant_check(number):
    counter = 0
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            counter += i
        if counter > number:
            return True
    if counter <= number:
        return False


def number_sum(number):
    for i in range(12, number // 2 + 1):
        if abundant_check(i):
            if abundant_check(number - i):
                return True
    return False


begin = time()
total = 0
for num in range(24, 28124):
    if num % 1000 == 0:
        print(f'Добрались до {num}')
    if not number_sum(num):
        total += num
print(total)
end = time()
print(f'Time: {end - begin} seconds')









