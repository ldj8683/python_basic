import mysql_bbs.bbs_dao as db

print("등록된 게시판에 수정하고 싶은 정보를 입력해주세요.")
print('------------------------------------------')
id1 = input('아이디를 입력해주세요 << ')
title1 = input('제목를 입력해주세요 << ')
content1 = input('내용를 입력해주세요 << ')

datas2 = (title1, content1, id1)

db.update(datas2)