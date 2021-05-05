from 클래스만들기.사람모듈 import *
import 클래스만들기.매일 as my

day5 = my.Day('주식', 6, '여의도')
print(day5)
print(day5.study())
print(day5.where())


super_man = SuperMan()
super_man.name1 = '클라크'
super_man.age1 = 1000
super_man.fly1 = True
print(super_man)
super_man.eat()
super_man.run()
super_man.sky()
