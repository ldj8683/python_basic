#1. 아이디와 이름을 입력받아 프린트하기
id, name = input('아이디와 이름을 입력하세요(,로 구분해주세요) : ').split(',')
print('아이디가 ' + id + '인 ' + name + '님이 로그인 되었습니다.')

#2. 두 수를 입력받아서 산술연산을 하여 프린트하기
num1 = int(input('첫번째 숫자를 입력하세요 : '))
num2 = int(input('두번째 숫자를 입력하세요 : '))
sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = int(num1 / num2)
rim = num1 % num2
print('-----------------------------------------')
print('두 수의 합은 ', sum, '입니다.')
print('두 수의 차은 ', sub, '입니다.')
print('두 수의 곱은 ', mul, '입니다.')
print('두 수의 나눗셈은 ', div, '입니다.')
print('두 수를 나누고 나서의 나머지는 ', rim, '입니다.')
print('-----------------------------------------')

#3 이름과 현재 나이를 입력받아서 프린트하기
name, age = input('이름과 현재 나이를 입력하세요.(,로 구분해주세요) : ').split(',')
age_int = int(age)
age_sum = age_int + 10
print(name, '님의 10년 후의 나이는 ', age_sum, '세입니다.')

#4 다음과 같이 판별되도록 프린트(10000원 기준)
money = int(input('엄마 용돈 주세요 : '))
if money >= 10000:
    print('엄마 용돈이 너무 많아요.')
else:
    print('엄마 용돈이 너무 적어요.')


#5 숫자를 입력하여 짝/홀을 판별해보세요
num = int(input('원하는 숫자를 입력해주세요(짝/홀판별) : '))
rim = num % 2
if rim == 0:
    print('입력하신 숫자 ', num, '은(는) 짝수입니다.')
else:
    print('입력하신 숫자 ', num, '은(는) 홀수입니다.')

#6 실적목표 달성여부 확인
goal = int(input('실적을 입력하세요>> '))
if goal >= 1000:
    print('-> 축하합니다. 실적을 달성하셧습니다.!')
    bonus = int(goal * 0.2)
    print('-> 당신의 이번달 보너스는 ', bonus, '만원입니다.')
else:
    print('-> 안타깝네요. 다음에는 꼭 달성하세요.!')

#7.
m_name = input('미사일의 이름을 입력하세요. : ')
m_start = float(input('미사일의 시작값을 입력하세요. : '))
m_move = float(input('미사일의 움직이는 값을 입력하세요: '))
m_total = m_start + m_move
print('-------------------------------------------------')
print(m_name, '미사일이 ', m_total,'로 이동되었습니다.')
print('-------------------------------------------------')

#8. 다음 데이터를 입력받아, 영수증을 출력하세요.
cash = int(input('받은 돈 : '))
price = int(input('상품의 총액 : '))
tax = int(price * 0.1)
change = cash - price

print('부가세 : ', tax)
print('잔  돈 : ', change)

#9. 별을 1000개 프린트
for x in range(1, 1001):
    print('*', end = ' ')
    if (x % 25) == 0:
        print()

#10. 1부터20까지 세로로, 가로로 프린트
print('----------------------------')
print('1부터 20까지 세로로 프린트')
for y in range(1, 21):
    print(y)
print('----------------------------')
print()
print('-----------------------------------------------------')
print('1부터 20까지 가로로 프린트')
for x in range(1, 21):
    print(x, end = ' ')
print('-----------------------------------------------------')
