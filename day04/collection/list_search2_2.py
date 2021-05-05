# a110 : a는 부서를 나타냄, 1: 직급, 뒤에 나머지 10: 내 번호
# 부서가 a: 기획부, b:개발부, c:인사부 / 직급이 1: 사장, 2: 팀장, 3: 사원
# 순차문의 구조 : 입력 -> 처리 -> 출력

# a110, b230, c340 이렇게 3개의 입력을 받아서 판별을 해보자
# 입력
while True:     # 지속적으로 입력을 받기 위해서 while 문을 이용해서 무한이 반복하게 while 문을 생성
    code = input('본인의 사원번호를 입력하세요(종료:0)>> ')    # 입력받은 String 을 code 라는 변수에 저장
    if code == '0':         # while 문이 무한하게 돌기 때문에 while 문에서 나올 수 있도록 종료를 할 수 있게 따로 설정을 해줌
                            # 입력창에 0 이라는 문자를 입력한다면 if문이 참이 되어서 break를 사용해서 while문에서 나올수 있도록함
        print('시스템을 종료합니다.') # 시스템이 종료가 된건지를 알려주는 정보를 출력
        break # while문 전체가 끝나버린다.
    # 처리 1. 입력한 데이터 중에서 부서와 직급을 추출한다. / 2. 부서의 값에 따라서 부서를 판별한다. / 3. 직급의 값에 따라서 직급을 판별
    # 위에 처럼 어떻게 처리할지 차례로 써보는 것을 스크립트라고 한다
    department = code[0]    # code 에 입력된 문자열의 인덱스 0에 위치한 문자를 추출해서 department 변수에 저장
    position = code[1]      # code 에 입력된 문자열의 인덱스 1에 위치한 문자를 추출해서 position 변수에 저장
    result = ''             # result 라는 비어있는 변수를 생성

    if department == 'a':       # department 라는 변수에 'a' 라는 문자가 있는지를 판별
        result = '기획부'              # 'a' 라는 문자가 있다면 result 변수에 '기획부' 를 대입
    elif department == 'b':     # department 라는 변수에 'b' 라는 문자가 있는지를 판별
        result = '개발부'              # 'b' 라는 문자가 있다면 result 변수에 '개발부' 를 대입
    elif department == 'c':     # department 라는 변수에 'c' 라는 문자가 있는지를 판별
        result = '인사부'              # 'c' 라는 문자가 있다면 result 변수에 '인사부' 를 대입
    else:                       # a,b,c를 제외한 나머지
        print('\n해당 부서는 존재하지 않습니다.')    # a,b,c를 제외에 해당하지 않으면 존재하지        break

    result += ' '           # result 에 추가되는 데이터를 구분하기 위해서 공백을 추가
    if position == '1':         # position 변수에 '1' 이라는 문자가 있는지를 판별
        result += '사장'              # '1' 이라는 문자가 있다면 result 변수에 '사장' 을 추가
    elif position == '2':       # position 변수에 '2' 이라는 문자가 있는지를 판별
        result += '팀장'              # '2' 이라는 문자가 있다면 result 변수에 '팀장' 을 추가
    elif position == '3':       # position 변수에 '3' 이라는 문자가 있는지를 판별
        result += '사원'              # '3' 이라는 문자가 있다면 result 변수에 '사원' 을 추가
    else:
        print('\n해당 직급이 존재하지 않습니다.')
        break
    print('당신은', result)

