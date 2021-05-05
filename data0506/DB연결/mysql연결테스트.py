import pymysql  # 패키지가 없을경우 alt + enter 를 누르면 설치를 하는 창이 나오는데 install package pymysql을 클릭을 해주면 알아서 설치를 해준다.

con = pymysql.connect(host='localhost', user='root', password='1234', port=3306 , db='shop')
print(con)
print("호스트 정보 출력 >> ", con.get_host_info())
print('DB 연결 완료')

curs = con.cursor() # 연결후 corsor()함수를 이용해서 연결되어 왔다갓다하는 데이터를 가져올 데이터를 가르쳐 어떠한 행동을 할 수 있게함
print(curs)
print('cursor객체 사용 가능!')

# SQL문 생성
sql = 'insert into member values ("python_test1", "python_test1", "python_test1", "python_test1")'
result = curs.execute(sql)
print(result)
print('sql문 생성 완료! DB로 보냈어요!')

# auto-commit 설정이 되어있지 않아서 commit을 해서 디비에 반영을 해야함
con.commit()
print('commit 완료!')

con.close()
print('연결끊기 완료!')


