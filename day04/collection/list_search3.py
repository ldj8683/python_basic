member = ['a110', 'b230', 'c340', 'a220']

for x in range(len(member)):    # 리스트안의 데이터 갯수만큼 for 문을 반복하겠다
    data = member[x]    # 인덱스 x에 해당하는 데이터를 data 변수에 저장
    dep = data[0]   # data 변수에 저장된 String 의 인덱스 0에 위치한 데이터를 dep 이라는 변수에 저장
    deg = data[1]   # data 변수에 저장된 String 의 인덱스 1에 위치한 데이터를 deg 이라는 변수에 저장
    result = ''     # result 라는 비어있는 변수를 생성

    if dep == 'a':      # dep 변수에 저장된 데이터가 'a'가 맞는지 비교
        result = '기획부'  # 위의 비교가 참일 경우에 result 변수에 '기획부' 라는 문자열을 대입
    elif dep == 'b':    # dep 변수에 저장된 데이터가 'b'가 맞는지 비교
        result = '개발부'  # 위의 비교가 참일 경우에 result 변수에 '개발부' 라는 문자열을 대입
    elif dep == 'c':    # dep 변수에 저장된 데이터가 'c'가 맞는지 비교
        result = '인사부'  # 위의 비교가 참일 경우에 result 변수에 '인사부' 라는 문자열을 대입
    else:               # 위의 데이터를 제외한 나머지
        print('\n해당 부서가 존재하지 않습니다.')    # 그 나머지에 대한 결과를 출력

    result += ' '       # result 변수에 추가가 되는 단어 사이에 구분을 주기 위해서 공백을 하나 추가

    if deg == '1':      # dep 변수에 저장된 데이터가 '1'가 맞는지 비교
        result += '사장'  # 위의 비교가 참일 경우에 result 변수에 '사장' 라는 문자열을 추가
    elif deg == '2':    # dep 변수에 저장된 데이터가 '2'가 맞는지 비교
        result += '팀장'  # 위의 비교가 참일 경우에 result 변수에 '팀장' 라는 문자열을 추가
    elif deg == '3':    # dep 변수에 저장된 데이터가 '3'가 맞는지 비교
        result += '사원'  # 위의 비교가 참일 경우에 result 변수에 '사원' 라는 문자열을 추가
    else:               # 위의 데이터를 제외한 나머지
        print('\n해당 직급이 존재하지 않습니다.')    # 그 나머지에 대한 결과를 출력
        break           # for 문에서 나오게 되는 명령어입니다.
    print('당신의 사원 번호는', data, '입니다.\n당신은', result, '입니다.\n') # 원하는 결과를 출력
