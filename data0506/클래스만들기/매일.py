class Day:
    # 실제값 변수: 인스턴스 변수(동적 변수) <-> 정적변수(static)
    work1 = ''
    hour1 = 0
    place1 = ''
    count = 0

    def __init__(self, work1, hour1, place1):
        self.work1 = work1
        self.hour1 = hour1
        self.place1 = place1
        Day.count += 1  # 객체가 생성될때마다 1씩 증가

        print(str(Day.count) + '개의 객체가 생성되었습니다.')

    def study(self):
        return self.work1 + '공부를 ' + str(self.hour1) + '시간 하다.'

    def where(self):
        return self.place1 + '에서 ' + self.work1 + '공부를 하다'

    def __str__(self):
        return '클래스 Day의 속성값들 >> ' + self.work1 + ', ' + str(self.hour1) + ', ' + self.place1

if __name__ == '__main__':
    print('-------------------------------------------')
    day1 = Day('파이썬 공부', 10, '강남')
    print(day1)
    print(day1.study())
    print(day1.where())

    print('-------------------------------------------')
    day2 = Day('자바 공부', 11, '신촌')
    print(day2)
    print(day2.study())
    print(day2.where())

    print('-------------------------------------------')
    day3 = Day('db 공부', 12, '종로')
    print(day3)
    print(day3.study())
    print(day3.where())
