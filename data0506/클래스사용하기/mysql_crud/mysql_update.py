import DB연결.mysql연결모듈 as db

print('디비 데이터를 수정 할 정보를 입력해주세요')
id1 = input('수정 할 아이디 입력 << ')
tel1 = input('수정 할 전화번호 입력 << ')

db.update(id1, tel1)
