from 클래스만들기.사람모듈 import *
import 클래스만들기.매일 as my

class WomanDay(Person, my.Day):
    # 클래스간 다중 상속이 가능하다.
    # 자바는 클래스간 단일 상속만 가능하다
    
    def __init__(self, work1, hour1, place1):
        # Person은 입력을 받는 매개 변수가 없기 때문에 굳이 만들어주지 않아도 된다.
        my.Day.__init__(self, work1, hour1, place1) # 다중상속이기 때문에 Day 클래스는 입력받는 매개변수가 있기 때문에 만들어줬다
        
    def __str__(self):
        return self.work1 + ', ' + str(self.hour1) + ', ' + self.place1
        
    def free(self):
        print('쉬다.')


if __name__ == '__main__':
    woman_day1 = WomanDay('진짜놀기', 20, '마포구')
    print(woman_day1)
    woman_day1.free()
    woman_day1.eat()
