from 클래스만들기.사람모듈 import *
import 클래스만들기.매일 as my

class Student(Person):
    study1 = None
    
    def study(self):
        print('나이가 ' + str(self.age1) + '세인 ' + self.name1 + '씨는 ' + self.study1 + '공부를 열심히 함')
    
    def __str__(self):
        return self.name1 + ', ' + str(self.age1) + ', ' + self.study1
    
class Worker(Person):
    work1 = None
    company1 = None
    
    def work(self):
        print('나이가 ' + str(self.age1) + '세인 ' + self.name1 + '씨는 ' + self.work1 + '인 ' + self.company1 + '에 출근했다.')

    def __str__(self):
        return self.name1 + ', ' + str(self.age1) + ', ' + self.work1 + ', ' + self.company1
    
if __name__ == '__main__':
    print('---------------------------------------------')
    study_person = Student()
    study_person.name1 = '홍길동'
    study_person.age1 = 25
    study_person.study1 = 'Python'
    print(study_person)
    study_person.study()
    
    print('---------------------------------------------')
    work_person = Worker()
    work_person.name1 = '김길동'
    work_person.age1 = 30
    work_person.work1 = 'IT 회사'
    work_person.company1 = '네이버'
    print(work_person)
    work_person.work()
    print('---------------------------------------------')

