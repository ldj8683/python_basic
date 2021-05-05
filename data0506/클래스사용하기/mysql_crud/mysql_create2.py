import DB연결.mysql연결모듈 as db

print('디비에 넣을 정보를 입력해주세요')
id1 = input('아이디 입력 << ')
pw1 = input('패스워드 입력 << ')
name1 = input('이름 입력 << ')
tel1 = input('전화번호 입력 << ')

data = (id1, pw1, name1, tel1)  # VO 역할
print('입력된 데이터 >> ', data)

db.create2(data)
