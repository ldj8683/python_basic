import mysql_bbs.bbs_dao as db

print("게시판에 등록하고 싶은 정보를 입력해주세요.")
print('------------------------------------')
id1 = input('아이디를 입력해주세요 << ')
title1 = input('제목를 입력해주세요 << ')
content1 = input('내용를 입력해주세요 << ')
writer1 = input('지은이를 입력해주세요 << ')

datas1 = (id1, title1, content1, writer1)

db.create(datas1)
