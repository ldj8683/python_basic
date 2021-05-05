# class의 역할 : 틀의 역할을 해준다. -> object(객체) - 틀을 가지고 만든 실제 대상,우리가 쓸 수있는 부품의 형태
class Dog:
    # 멤버변수
    color = None
    field = ''

    # 생성자 함수(객체생성지 자동호출되는 함수, 초기화를 담당한다.)
    # initialize 의 축약어
    # constructor!!
    def __init__(self, color, field): # self는 자바의 this에 해당한다
        # 생성자에 넣은 가장 많은 초기화 처리는 멤버변수 값 초기화이다.
        self.color = color
        self.field = field
        print('생성자가 호출됨.')

    # 멤버함수
    # def 는 함수를 정의하겠다. 라는 의미
    def jump(self):
        print('강아지가 점프')

    def sleep(self):
        print('강아지가 잔다.')

    # toString 오버라이드(재정의)
    def __str__(self):
        return '클래스 Dog의 속성값들 >> ' + str(self.color) + ', ' + self.field

if __name__ == '__main__':
    # dog1, dog2 라는 객체를 생성
    dog1 = Dog('흰색', '진돗개')    # 참조형(주소): 객체 생성시 dog1에 대한 특성을 저장하기 위해 멤버변수(color, field)들이 복사가 된다.
    print(dog1)     # 참조형 변수 자체를 출력한다면, 원래는 toString으로 기본적으로 내장되어있던 것이 출력되지만
                    # 위에서 __str__로 오버라이드 했기 때문에 재정의 한 것으로 출력이 된다.
    dog1.sleep()

    dog2 = Dog('검은색', '세퍼트')
    print(dog2)
    dog2.jump()
