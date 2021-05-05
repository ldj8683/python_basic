import DB연결.mysql연결모듈 as db

print('검색할 아이디를 입력하세요')
id1 = input('아이디 입력 << ')
db.read2(id1)
