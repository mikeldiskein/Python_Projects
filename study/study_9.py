from useful_things import is_prime
from time import time

start = time()
odd_composite_numbers = [num for num in range(1, 10000) if num % 2 == 1 and not is_prime(num)]
# print(odd_composite_numbers[-1])
primes_to_three_thousand = [num for num in range(1, 10000) if is_prime(num)]
# print(primes_to_three_thousand[-1])


def check(odd_composite_number):
    for prime in primes_to_three_thousand:
        if prime >= odd_composite_number:
            return False
        square_val = 1
        while odd_composite_number >= prime + (2 * (square_val**2)):
            value = prime + (2 * (square_val**2))
            if odd_composite_number == value:
                return True
            else:
                square_val += 1
    return False


for number in odd_composite_numbers:
    if not check(number):
        print(number)
        break
end = time()
print('Time: ', end - start)