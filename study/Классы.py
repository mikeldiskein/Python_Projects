class Toyota:
    def __init__(self):
        self.color = "Бардовый металлик"
        self.price = "1 000 000 руб"
        self.max_velocity = "200 km/h"
        self.current_velocity = "0 km/h"
        self.engine_rpm = 0

    def start(self):
        print("Engine is turned on")
        self.engine_rpm = 900

    def go(self):
        print("Let's go!")
        self.engine_rpm = 2000
        self.current_velocity = "20 km/h"


# my_car = Toyota()
# print('color', my_car.color)
# print('price', my_car.price)
# print('max_velocity', my_car.max_velocity)
# print('rpm', my_car.engine_rpm)
# print('current_velocity', my_car.current_velocity)

# my_car.start()
# print('rpm', my_car.engine_rpm)
# my_car.go()
# print('rpm', my_car.engine_rpm)
# print('current_velocity', my_car.current_velocity)


# car = Toyota()

# car.color = 'Green'
# print('color', car.color)

# print('color', my_car.color)

# robot = Toyota()
# print(robot.color)

# car = my_car
# robot = car

# print(robot.color)

# специальные методы классов


robot = Robot()


attr_name = 'model'
if hasattr(robot, attr_name):
    print(robot.model)
else:
    setattr(robot, attr_name, 'android')
print(robot.model)

print(getattr(robot, attr_name))

delattr(robot, attr_name)

print(robot)


class Robot:
    def __init__(self, temperature=0):
        self.name = "R2D2"
        self.content = ['gun']
        if temperature != 0:
            self.temp = temperature

    def hello(self):
        print('hello, world! I am', self.name)

    def __str__(self):
        return 'Robot: ' + ', '.join(self.content)

    def __bool__(self):
        return self.content != []

    def __len__(self):
        return len(self.content)


print(robot.__len__(), robot.__bool__(), sep='\n')


from random import choice


class Backpack:
    def __init__(self, gift=None):
        self.content = []
        if gift:
            self.content.append(gift)

    def __eq__(self, other):
        return self.content == other.content

    def __add__(self, other):
        new_obj = Backpack()
        new_obj.content.extend(self.content)
        new_obj.content.extend(other.content)
        return new_obj.content


my_backpack = Backpack(gift='sandwich')
son_backpack = Backpack(gift='banana')

# if my_backpack == son_backpack:
# print('We are so similar')
# if Backpack.__eq__(self=my_backpack, other=son_backpack):
# print('We are so similar')

# print((my_backpack + son_backpack).content)
our_backpack = my_backpack + son_backpack


# print(our_backpack.content)
# print(*(my_backpack + son_backpack))

# __str__ может помочь выводить то, что нужно


class Bread:
    def __str__(self):
        return 'bread'

    def __add__(self, other):
        return Sandwich(part1=self, part2=other)


class Sausage:
    def __str__(self):
        return 'sausage'

    def __add__(self, other):
        return Sandwich(part1=self, part2=other)


class Sandwich:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'I am a sandwich. I am consist of ' + str(self.part1) + ' and ' + str(self.part2)


borodinsky = Bread()
salami = Sausage()
result = borodinsky + salami
# print(result)


class Lemming:
    names = ['Peter', 'Anna', 'Nik', 'Sofi', 'Den', 'Lora', 'Bred']
    tail_length = 20

    def __init__(self):
        self.name = choice(Lemming.names)

    def __str__(self):
        return 'Lemming' + self.name + ' with tai ' + str(self.tail_length)


print(Lemming.tail_length)

new_lemming = Lemming()
print(new_lemming.tail_length)
print(new_lemming)


from random import choice, randint


class Lemming:
    names = ['Peter', 'Anna', 'Nik', 'Sofi', 'Den', 'Lora', 'Bred']
    tail_length = 20
    total = 0

    def __init__(self):
        self.name = choice(Lemming.names)
        self.tail_length = randint(15, 25)
        Lemming.total = Lemming.total + 1

    def __str__(self):
        return 'Lemming' + self.name + ' with tail ' + str(self.tail_length)


burrow = []
burrow_depth = randint(90, 100)
while len(burrow) < burrow_depth:
    family = []
    family_size = randint(16, 32)
    while len(family) < family_size:
        new_lemming = Lemming()
        family.append(new_lemming)
    burrow.append(family)

print(Lemming.total)
print(len(burrow))
for i in burrow:
    for j in i:
        # print(j.name, j.tail_length)


class SomeClass:
    x = 67

    def __init__(self):
        self.x = 78

    def method_one(self):
        x = 23
        print('method_one', x)

    def method_two(self):
        x = 34

        def func_one():
            x = 56
            print('func_one', x)

        func_one()
        print('method_two', x)


x = 12
obj = SomeClass()
obj.method_one()
obj.method_two()
print('global', x)
