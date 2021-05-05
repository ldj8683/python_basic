# 딕셔너리(사전), {key:value, key:value, key:value, ...}
me = {'이름':'hong', 'age':100, 'height':180.5}
you = {'이름':'kim', 'age':90, 'height':170.5}

# 출력을 할때는 []를 사용한다
# me 라는 곳에서 이름을 찾고 싶다면 me['이름'] 이러한 방식이다.
print(me['이름'])
print(me['age'])
# age에 해당하는 value를 변경할 때
me['age'] = 101
print(me)
print(you)

# 비어있는 딕셔너리를 만들 경우
he = dict()
he['이름'] = 'song'
he['age'] = 200
he['height'] = 130.4
he['weight'] = 100.5
print(he)
del he['height']
print(he)
print(len(he))

# key 목록만 가져오고 싶을 경우
print(he.keys())

for x in he:
    #print(x) #key만 프린트
    #print(he[x]) #value만 프린트
    print(x,he[x]) # key value 프린트


