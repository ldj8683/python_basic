import DB연결.mysql_bbs.bbs_dao as db

print("확인하고 싶은 정보의 아이디를 입력해주세요.")
print('------------------------------------------')
id1 = input('아이디를 입력해주세요 << ')

db.read(id1)

