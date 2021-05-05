class Person:
    name1 = None
    age1 = 0

    def eat(self):
        print('먹다')

    def __str__(self):
        return self.name1 + ', ' + str(self.age1)


class Man(Person):
    speed1 = 0

    def run(self):
        print('빨리 달리다')

    def __str__(self):
        return self.name1 + ', ' + str(self.age1) + ', ' + str(self.speed1)

class SuperMan(Man):
    fly1 = False

    def sky(self):
        print('하늘을 날다')

    def __str__(self):
        return self.name1 + ', ' + str(self.age1) + ', ' + str(self.speed1) + ', ' + str(self.fly1)
