from termcolor import cprint
from random import randint


class House:

    def __init__(self):
        self.money = 100
        self.dirt = 0
        self.food = 50
        self.cat_food = 30

    def __str__(self):
        return 'В доме уровень грязи {}, еды осталось {}, денег осталось {}'.format(
            self.dirt, self.food, self.money)


class Man:
    sum_money = 0
    sum_food = 0
    count_fur_coat = 0

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = None

    def pet_the_cat(self):
        cprint('{} погладил кота'.format(self.name), color='green')
        if self.happiness < 100:
            self.happiness += 20

    def eat(self):
        if self.house.food >= 30 and self.fullness < 100:
            self.house.food -= 30
            self.fullness += 30
            cprint('{} поел'.format(self.name), color='green')
        else:
            cprint('{} не поел'.format(self.name), color='green')

    def go_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} вьехал в дом'.format(self.name), color='yellow')

    def __str__(self):
        return self.name + ' сытность ' + str(self.fullness) + ', степень счастья ' + str(self.happiness)


class Husband(Man):

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return super().__str__()

    def act(self):
        dice = randint(1, 3)
        if self.fullness <= 0:
            cprint('{} умер от голода'.format(self.name), color='red')
            return
        elif self.happiness < 10:
            cprint('{} умер от депресии'.format(self.name), color='red')
            return
        elif self.house.dirt > 90:
            self.happiness -= 10

        if self.fullness <= 30:
            self.eat()
        elif self.house.money < 350:
            self.work()
        elif home.dirt >= 90:
            self.happiness -= 10
        elif dice == 1:
            self.gaming()
        elif dice == 2:
            self.work()
        elif dice == 3:
            self.pet_the_cat()

    # def eat(self):
    #     super().eat()

    def work(self):
        salary = 150
        self.house.money += salary
        self.fullness -= 10
        Man.sum_money += salary
        cprint('{} сходил на роботу'.format(self.name), color='magenta')

    def gaming(self):
        self.fullness -= 10
        if self.happiness < 200:
            self.happiness += 20
        cprint('{} играл целый день в WoT'.format(self.name), color='green')


class Wife(Man):

    def __init__(self, name):
        super().__init__(name)
        self.fur_coat = 0

    def __str__(self):
        return super().__str__()

    # def eat(self):
    #     super().eat()

    def shopping(self):
        cprint('{} сходила в магазин'.format(self.name), color='white')
        self.fullness -= 10
        if self.house.food > 200:
            cprint('{} ничего не купила'.format(self.name), color='white')
            return
        self.house.food += 100
        self.house.money -= 100
        Man.sum_food += 100

    def shoping_cat(self):
        cprint('{} сходила в магазин за едой для кота'.format(self.name), color='white')
        self.house.cat_food += 30
        self.house.money -= 30

    def buy_fur_cot(self):
        cprint('{} ходила смотреть на меха'.format(self.name), color='magenta')
        self.fullness -= 10
        if self.house.money > 7000:
            self.fur_coat += 1
            Man.count_fur_coat += 1
            self.house.money -= 3500
            if self.happiness < 150:
                self.happiness += 60

            cprint('{} купила шубу!!!'.format(self.name), color='red')

    def clean_house(self):
        self.fullness -= 10
        if self.house.dirt > 100:
            self.house.dirt -= 100
        else:
            self.house.dirt = 0
        cprint('{} убрала в доме'.format(self.name), color='yellow')

    def act(self):
        dice = randint(1, 3)
        if self.fullness <= 0:
            cprint('{} умерла от голода'.format(self.name), color='red')
            return
        elif self.happiness < 10:
            cprint('{} умерла от депресии'.format(self.name), color='red')
            return
        elif self.house.dirt >= 80:
            self.happiness -= 10

        if self.house.food <= 60:
            self.shopping()
        elif self.fullness < 40:
            self.eat()
        elif self.house.cat_food < 40:
            self.shoping_cat()

        elif self.house.dirt >= 90:
            self.clean_house()
        elif dice == 1:
            self.pet_the_cat()
        elif dice == 2:
            self.buy_fur_cot()
        elif dice == 3:
            self.clean_house()


class Child(Man):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        dice = randint(1, 2)
        if self.fullness <= 0:
            cprint('{} умер от голода'.format(self.name), color='red')
            return
        elif self.fullness < 40:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.eat()



    def eat(self):
        if self.house.food >= 10 and self.fullness < 100:
            self.house.food -= 10
            self.fullness += 10
            cprint('{} поел'.format(self.name), color='green')
        else:
            cprint('{} не поел'.format(self.name), color='green')

    def sleep(self):
        cprint('{} спит'.format(self.name), color='green')
        self.fullness -= 10


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.house = None

    def __str__(self):
        return 'Кот {}, сытность {}'.format(self.name, self.fullness)

    def act(self):
        dice = randint(1, 3)
        if self.fullness <= 0:
            cprint('Кот {} умер'.format(self.name), color='red')
            return
        if self.fullness <= 20:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.sleep()
        elif dice == 3:
            self.soil()

    def eat(self):
        cprint('Кот {} пришел на кухню'.format(self.name), color='yellow')
        if self.fullness < 100 and self.house.cat_food >= 10:
            self.fullness += 20
            self.house.cat_food -= 10
            cprint('Кот {} поел'.format(self.name), color='yellow')

    def sleep(self):
        cprint('Кот {} спит'.format(self.name), color='yellow')
        self.fullness -= 10

    def soil(self):
        cprint('Кот {} дерет обои'.format(self.name), color='yellow')
        self.house.dirt += 5
        self.fullness -= 10

    def cat_to_house(self, house):
        self.house = house
        cprint('Кот {} пришел в дом'.format(self.name), color='yellow')



home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
kolya.go_house(home)
murzik = Cat(name='Мурзик')
serge.go_house(home)
masha.go_house(home)
murzik.cat_to_house(home)
for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    home.dirt += 5
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')
    cprint(home, color='cyan')
cprint(
    'Всего заработано денег {}, куплено шуб {}, куплено еды {}'.format(Man.sum_money, Man.count_fur_coat, Man.sum_food),
    color='green')
