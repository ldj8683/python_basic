# set(집합)
# 중복을 허용하지 않음

jumsu_list = [100, 30, 50, 60, 30, 100]     # list 생성
print(jumsu_list)               # 출력
jumsu_set = set(jumsu_list)     # list 형을 set 형태로 바꾸어준다
print(type(jumsu_set))          # 어떤 종류일지를 알고 싶을 경우 type을 사용한다
print(jumsu_set)                # 출력

jumsu_lise2 = [50, 60, 30, 90]     # 리스트 생성
jumsu_set2 = set(jumsu_lise2)       # 리스트를 set으로 바꾸어줌
result = jumsu_set2.intersection(jumsu_set)     # 교집합을 이용할때 사용
print('교집합')
print(result)           # 결과 출력