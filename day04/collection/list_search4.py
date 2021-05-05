# 피잣집과 햄버거집의 갯수 확인하기
food_list = ['맛나피자', '새로운피자', '그냥피자', '대왕햄버거', '군대햄버거'] # food_list 라고 만든 리스트에 데이터를 임의로 만들어서 저장

count_p = 0     # 확인되는 피자 가게의 갯수를 세기 위해서 count_p 라는 변수를 선언
count_h = 0     # 확인되는 햄버거 가게의 갯수를 세기 위해서 count_h 라는 변수를 선언
for x in range(len(food_list)): # food_list 라고하는 리스트에 데이터 갯수가 몇 개인지를 len() 을 이용해서 범위를 정하고 x 를 1씩 증가시키는 반복문을 생성
    data = food_list[x]     # food_list[x] 에 해당하는 데이터를 data 변수에 저장
    if '피자' in data:        # data 의 String 에 '피자' 라는 문자가 들어있는가를 확인
        count_p += 1            # '피자' 라는 문자가 들어있다면 count_p의 수를 하나 증가시켜준다
    elif '햄버거' in data:     # data 의 String 에 '햄버거' 라는 문자가 들어있는가를 확인
        count_h += 1            # '햄버거' 라는 문자가 들어있다면 count_h의 수를 하나 증가시켜준다
print('피잣집의 갯수는', count_p, '개이고, 햄버거집 갯수는', count_h, '개 입니다.') # 결과를 출력