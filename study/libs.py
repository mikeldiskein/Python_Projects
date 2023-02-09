from collections import defaultdict, OrderedDict

goods = [
    ['мука', 28],
    ['сахар', 15],
    ['сахар', 25],
    ['мука', 34]
]

good_count = defaultdict(lambda: 0)  # either 'int'
for name, quantity in goods:
    good_count[name] += quantity

# print(good_count)


my_pets = OrderedDict()
my_pets['dog'] = 'Zhuchka'
my_pets['cat'] = 'Peach'
my_pets['mouse'] = 'Norushka'
my_pets['parrot'] = 'Kesha'
# print(my_pets)
# for k, v in my_pets.items():
#     print(f'{k}: {v}')

