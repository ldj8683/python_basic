hobby = [] # hobby라는 데이터를 넣지않는 리스트를 만들어 줍니다.
hobby.append('코딩') # hobby라는 리스트에 '코딩'이라는 데이터를 추가해줍니다.
print('갯수 >>', len(hobby)) #hobby라는 리스트에 데이터가 몇 개인지 알려줍니다.
hobby.append('등산') # 위에 설명과 마찬가지로 '등산'이라는 데이터를 추가해줍니다.
print('갯수 >>', len(hobby)) # hobby 리스트에 데이터가 몇 개인지 알려줍니다.


for _ in range(3): # _는 for문에서 변수를 설정하지 않을 경우에 사용합니다. range(3)은 범위를 0이상 3미만으로 지정하겠다는 의미입니다.
    data = input('당신의 새로운 취미는 >>') #input으로 데이터를 입력받아 data 변수에 넣습니다.
    hobby.append(data) #입력받은 data라는 변수를 hobby 리스트에 추가합니다.

print('갯수 >>', len(hobby)) #hobby 리스트안에 데이터의 갯수가 얼마인지 알려줍니다.

for index in hobby: # hobby 리스트에서 알아서 순차적으로 찾아서 index 변수에 넣습니다.
    print(index, end=' ') # index변수를 출력합니다.

