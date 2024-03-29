# -*- coding: utf-8 -*-
"""파이썬입문.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pUNMn7OA_RpWhZrKt8xNCXTDNM9kRFKX
"""

print('hello')

print('안녕하세요.')
print('저는 홍길동입니다.')

print('안녕하세요.',end=' ')
print('저는 홍길동입니다.')

# 컨트롤 + / : 주석(설명을 하겠다), comment
# 입력 : 데이터를 가지고 와야함, input
# 처리 : 적절한 처리
# 출력 : 처리한 결과를 내보내는 일(모니터 출력, 파일 저장, DB에 저장, 네트워크로 전송), output

input('이름을 입력하세요 >> ')

name = input('이름을 입력하세요 >> ') # 간단한 처리(기호를 씀): 연산 -> 그 기호를 연산 자라고함
#  = : 대입 연산자(값을 넣어주는 연산자)

print(name)

print('----------------------------------------')
name = input('당신의 이름은: ')
age = input('당신의 나이는: ')
sex = input('당신의 성별은: ')
hobby = input('당신의 취미는: ')
motto = input('당신의 좌우명은: ')
print('----------------------------------------')
print(name + '은 ' + age + '세이고, ' + sex + '이고 ' + hobby + '가 취미이고 ' + motto + '라는 좌우명을 가지고 살아간다.')

print('----------------------------------------')
name = input('당신의 이름은: ')
age = input('당신의 나이는: ')
sex = input('당신의 성별은: ')
hobby = input('당신의 취미는: ')
motto = input('당신의 좌우명은: ')
print('----------------------------------------')
print(name, '은 ', age, '세이고, ', sex, '이고 ', hobby, '가 취미이고 ', motto, '라는 좌우명을 가지고 살아간다.')

location = '신촌'

number = 2

height = 195.5

food_lunch = True

age2 = input('나이 입력>> ') # 100을 입력할것임
# 컴퓨터에서 입력한 데이터는 String 타입으로 인식된다

# String을 정수로 바꾸어쓰는 결정은 프로그래머가 한다. -> 타입변화는 '캐스팅' 이라고 한다. (캐스팅은 CPU가 한다.)
# 여기서는 강제로 캐스팅하기 때문에 '강제 캐스팅' 이라고 한다.

# print(int(age2) + 1) # 이렇게 넣어서 해도되고 아이에 처음부터 age2 변수에 정수로 넣어버릴 수 있다.

age_int = int(age2) # casting후 대입을 해주어야한다.
print('내년 나이는', age_int + 1) # 문자열과 정수형은 서로 합할 수 없다.

# 두 수를 입력 받아서 사칙연산을 해보세요
num1 = int(input('첫번째 수를 입력하세요 : '))
num2 = int(input('두번째 수를 입력하세요 : '))
print('--------------------------------')
print('더하기 : ', num1, "+", num2, '=', num1+num2) # int int 끼리 계산을 하는 것을 산술 연산이라고함
print('빼  기 : ', num1, "-", num2, '=', num1-num2)
print('곱하기 : ', num1, "*", num2, '=', num1*num2) # * 아스테리크, 에스테리크 라고함
print('나누기 : ', num1, "/", num2, '=', num1/num2)
print('  몫   : ', num1, "//", num2, '=', num1//num2)
print('나머지 : ', num1, "%", num2, '=', num1%num2)
print('--------------------------------')

me = '커피'
me2 = '우유'
print(me + me2) # 문자열로 결합시켜라(문자열끼리 연산을하면 결합연산자라고함)

price = 1000

print(me + '가격은 ' + str(price) + '원')

# 자바는 값을 선언을 한다
# int test

# 파이썬은 변수를 만들기 위해서는 반드시 변수에 해당하는 값을 넣어주어야한다
# test = 0

price = int(input('커피 값 입력 : '))
count = int(input('커피 인원 수 : ')) # 변수(저장공간, 저장공간이름->변수명), 파이썬에서 변수는 반드시 값이 들어가야 한다.
sum = price * count
if sum >= 20000:
  print('계산 값이 20000원 이상이면 2000원을 할인해 드립니다.')
  print(sum-2000, '원 결제하세요')
else:
  print('계산 값이 20000원 미만이면 계산값을 전부 지불해야 합니다.')
  print(sum, '원 결제하세요')

price = int(input('커피 값 입력 : '))
count = int(input('커피 인원 수 : '))
sum = price * count
if sum >= 20000:
  print('계산 값이 20000원 이상이면 2000원을 할인해 드립니다.')
  print(sum-2000, '원 결제하세요')
else:
  print('계산 값이 20000원 미만이면 계산값을 전부 지불해야 합니다.')
  print(sum, '원 결제하세요')

#1.
principal = int(input('1년 만기 정기 예금을 얼마나 예치하시겠습니까? '))
print('원금이 ' , principal , '원이시군요.!')
interest = int(principal/10)
print('이자는 ' , interest , '원입니다.')
sum = principal + interest
print('원리 합계는' , sum ,'원입니다.')

#2
english = int(input('영어점수 입력: '))
math = int(input('수학점수 입력: '))
korean = int(input('국어점수 입력: '))
sum = english + math + korean
avg = sum // 3
print('--------------------')
print('세 과목의 합은 ', sum,'점')
print('세 과목의 평균은 ', avg,'점')

#3
time = int(input('지금은 몇 시 입니까? '))
if time < 12:
  print('12시 보다 작으면 점심 전입니다. 맛있게 드세요!')
else:
  print('12시 이상이면 점심 후입니다.')

#4
ini_id = 'root'
id = input('로그인할 id를 입력>> ')
if id == ini_id:
  print('로그인 되었습니다.')
else:
  print('로그인 되지 않았습니다.')

#4
ini_id = 'root'
id = input('로그인할 id를 입력>> ')
if id == ini_id:
  print('로그인 되었습니다.')
else:
  print('로그인 되지 않았습니다.')

#5
print('교보문고에 갔습니다.')
sticker_price = 1000
sticker_count = int(input('1000원짜리 스티커 갯수 : '))
bookmark_price = 2500
bookmark_count = int(input('2500원짜리 책갈피 갯수 : '))
print('스티커', sticker_count,'장과 책갈피',bookmark_count,'개를 샀습니다.')
sum = (sticker_price * sticker_count) + (bookmark_price * bookmark_count)
print('가격은 ', sum, '입니다.')
print('우수회원입니다. 10%가 할인됩니다.')
discount = int(sum / 10)
total = sum - discount
print('내가 낸 금액은 얼마일까요?')
print(total,'입니다.')

