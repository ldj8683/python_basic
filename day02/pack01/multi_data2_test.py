food = []
for _ in range(3):
    data = input('원하는 음식을 입력하세요 : ')
    food.append(data)
print('갯수 >>', len(food))
for i in food:
    print(i, end=' ')

print(food[1])
print(food[0:1])
print(food[1:2])
food[0] = '라면'
for i in food:
    print(i, end=' ')

print()
print('------------------------')
sum = 10
for i in range(0,11):
    print(sum)
    sum += 1

