class Cat:
    has_tail = True
    woolliness = 20

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.__class__.__name__}, {self.name}, ' \
               f'хвост есть? {self.has_tail}, пушистость - ' \
               f'{self.woolliness}'


class Bobtail(Cat):
    has_tail = False


class Sphinx(Cat):
    woolliness = 1


murzik = Bobtail(name='Мурзик')
sonya = Sphinx(name='Соня')
# print(murzik)
# print(sonya)


class Robot:

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f'{self.__class__.__name__} {self.model}'

    def operate(self):
        print('Робот ездит по кругу')


class WarRobot(Robot):

    def operate(self):
        print('Робот охраняет военный объект')


class VacuumCleaningRobot(Robot):

    def __init__(self, model):
        super().__init__(model=model)
        self.dust_bug = 0

    def operate(self):
        print('Робот пылесосит пол. Заполненность мешка для'
              ' пыли', self.dust_bug)


roomba = VacuumCleaningRobot(model='roomba M505')
print(roomba)
roomba.operate()
