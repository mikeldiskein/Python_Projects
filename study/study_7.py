from time import time
from useful_things import is_prime


def is_pandigital(num):
    num = str(num)
    return len(set(num)) == len(str(num))


start = time()
for num in range(999999999, 0, - 1):
    if is_pandigital(num) and is_prime(num):
        biggest_panprime = num
        break

print(biggest_panprime)
end = time()
print(end - start)







