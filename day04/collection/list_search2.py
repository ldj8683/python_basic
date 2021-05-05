# a110 : a는 부서를 나타냄, 1: 직급, 뒤에 나머지 10: 내 번호
# 부서가 a: 기획부, b:개발부, c:인사부 / 직급이 1: 사장, 2: 팀장, 3: 사원
# 순차문의 구조 : 입력 -> 처리 -> 출력

# a110, b230, c340 이렇게 3개의 입력을 받아서 판별을 해보자
# 입력
code = input('본인의 사원번호를 입력하세요 >> ')     # 입력받은 데이터를 code 라는 변수에 저장
# 처리 1. 입력한 데이터 중에서 부서와 직급을 추출한다. / 2. 부서의 값에 따라서 부서를 판별한다. / 3. 직급의 값에 따라서 직급을 판별
department = code[0]    # department 변수에 code 에 입력된 문자열의 인덱스 0의 위치하는 데이터를 추출하여 저장
position = code[1]      # position 변수에 code 에 입력된 문자열의 인덱스 1의 위치하는 데이터를 추출하여 저장
number = code[2:]       # number 변수에 code 에 입력된 문자열의 인덱스 2 이후에 위치하는 데이터를 추출해서 저장
department_name = ''    # department_name 라는 비어있는 변수를 생성
position_name = ''      # position_name 라는 비어있는 변수를 생성

while True:                         # break 가 나오기 전까지 무한히 반복되는 while 문을 생성
    if department == 'a':           # department 에 저장된 데이터가 'a'와 같은지 여부를 판별
        department_name = '기획부'     # a라는 데이터가 들어있다면 department_name 변수에 '기획부' 라는 데이터를 대입
    elif department == 'b':         # department 에 저장된 데이터가 'b'와 같은지 여부를 판별
        department_name = '개발부'     # b라는 데이터가 들어있다면 department_name 변수에 '개발부' 라는 데이터를 대입
    elif department == 'c':         # department 에 저장된 데이터가 'c'와 같은지 여부를 판별
        department_name = '인사부'     # c라는 데이터가 들어있다면 department_name 변수에 '인사부' 라는 데이터를 대입
    else:                           # a,b,c 를 제외한 나머지
        print('해당 부서가 존재하지 않습니다.')  # 다른 부서는 처음 만들때 넣지 않았기 때문에 부서가 존재하지 않다는 정보를 알려주기 위해서 출력
        break                                   # 존재하지 않기 때문에 더이상 while 문을 반복할 수 없기 때문에 break 를 사용해서 while 문에서 빠져나옴

    if position == '1':             # position 에 저장된 데이터가 '1'과 같은지 여부를 판별
        position_name = '사장'            # 1이라는 데이터가 들어있다면, position_name 변수에 '사장' 이라는 데이터를 대입
    elif position == '2':           # position 에 저장된 데이터가 '2'과 같은지 여부를 판별
        position_name = '팀장'            # 2이라는 데이터가 들어있다면, position_name 변수에 '팀장' 이라는 데이터를 대입
    elif position == '3':           # position 에 저장된 데이터가 '3'과 같은지 여부를 판별
        position_name = '사원'            # 3이라는 데이터가 들어있다면, position_name 변수에 '사원' 이라는 데이터를 대입
    else:                           # 1,2,3 을 제외한 나머지
        print('해당 직급이 존재하지 않습니다.')  # 다른 직급은 처음 만들때 넣지 않았기 때문에 직급이 존재하지 않다는 정보를 알려주기 위해서 출력
        break                       # 존재하지 않기 때문에 더이상 while 문을 반복할 수 없기 때문에 break 를 사용해서 while 문에서 빠져나옴
    break           # 모든 데이터를 올바르게 입력하고 난 뒤 while 문을 빠져나오기 위해서 break 를 사용
print('부서:', department_name, '\n직급:', position_name, '\n번호:', number)  # 저장한 결과를 출력
