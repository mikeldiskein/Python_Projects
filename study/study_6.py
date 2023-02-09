from time import time
start = time()
largest = 0
for num in range(1, 1000000):
    number_length = 0
    str_number = ''
    n = 0
    while number_length < 9:
        n += 1
        str_number += str(num * n)
        number_length = len(str_number)
    if ''.join(sorted(str_number)) == '123456789' and len(str_number) == 9:
        largest = int(str_number)

print(largest)
end = time()
print('Time: ', end - start)


