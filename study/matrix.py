from random import randint, sample
# n = int(input())

# heroes = set()
# while len(heroes) < 6:
#     heroes.add(randint(1, 24))

heroes = sample(range(1, 24), 6)
print(heroes)

