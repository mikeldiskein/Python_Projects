# class Pet:
#     legs = 4
#     has_tail = True
#
#     def __init__(self, name):
#         self.name = name
#
#     def inspect(self):
#         print(self.__class__.__name__, self.name)
#         print('Всего ног:', self.legs)
#         print('Хвост есть -', 'да' if self.has_tail else 'нет')
#         print(self.__dict__)
#
#
# class Cat(Pet):
#     def sound(self):
#         print('Мяу!')
#
#
# class Dog(Pet):
#     def sound(self):
#         print('Гав!')
#
#
# class Hamster(Pet):
#     def sound(self):
#         print('Цццццц!')
#
#
# # print('Котик')
# # my_pet = Cat()
# # my_pet.inspect()
# # my_pet.sound()
#
# # print('Dog')
# # my_pet = Dog()
# # my_pet.inspect()
# # my_pet.sound()
#
# # print('Hamster')
# # my_pet = Hamster()
# # my_pet.inspect()
# # my_pet.sound()
#
#
# # pet = Pet(name='Кузя')
# # pet.inspect()
# # print(pet.__class__ is Pet)
#
#
# class Parent:
#     class_var_1 = 12
#     _class_var_2 = 23
#     __class_var_3 = 34
#
#     def __init__(self):
#         self.var_1 = 45
#         self._var_2 = 56
#         self.__var_3 = 67
#
#     def parent_method(self):
#         print(self.class_var_1)
#         print(self._class_var_2)
#         print(self.__class_var_3)
#         print(self.var_1)
#         print(self._var_2)
#         print(self.__var_3)
#
#
# class Child(Parent):
#
#     def method(self):
#         print(self.class_var_1)
#         print(self._class_var_2)
#         # print(self.__class_var_3)
#         print(self.var_1)
#         print(self._var_2)
#         # print(self.__var_3)


# obj = Child()
# # obj.parent_method()
# obj.method()


class Employee:
    def salary(self):
        return 15000


class Parent:

    def children(self):
        return ['Вася', 'Катя']


class Man(Parent, Employee):
    pass


class Robot(Employee):
    pass


# me = Man()
# print(me.children())
# print(me.salary())


class GrandParent:
    def method(self):
        print('call from Grandparent')


class ParentOne(GrandParent):
    def method(self):
        super().method()
        print('call from ParentOne')


class ParentTwo(GrandParent):
    def method(self):
        super().method()
        print('call from ParentTwo')


class Child(ParentOne, ParentTwo, ):
    def method(self):
        super().method()
        print('call from Child')


obj = Child()
obj.method()
print(obj.__class__.__mro__)  # так можно посмотреть, в каком порядке будут искаться методы







