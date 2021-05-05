import pymysql  # 패키지가 없을경우 alt + enter 를 누르면 설치를 하는 창이 나오는데 install package pymysql을 클릭을 해주면 알아서 설치를 해준다.

# DAO 역할 모듈 : CRUD(DML)

# 정형데이터 => mySQL, Oracle, sqlite3 (관계형 데이터베이스 관리 시스템, RDBMS)
def create(id, pw, name, tel):
    # 1. mysql과 연결
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    print(con)
    print("호스트 정보 출력 >> ", con.get_host_info())
    print('DB 연결 완료')

    # 2. 스트림안의 데이터를 다룰 수 있는 부품인 cursor를 획득한다.
    curs = con.cursor() # 연결후 corsor()함수를 이용해서 연결(연결통로: Stream)되어 왔다갓다하는 데이터를 가져올 데이터를 가르쳐 어떠한 행동을 할 수 있게함
    print(curs)
    print('cursor객체 사용 가능!')

    # 3. SQL문을 만들어서 전송함
    # SQL문 생성
    sql = 'insert into member values ("' + id + '","' + pw + '","' + name + '","' + tel + '")'
    result = curs.execute(sql)
    print(result)
    print('sql문 생성 완료! DB로 보냈어요!')

    # 4. auto-commit 설정이 되어있지 않아서 commit을 해서 디비에 반영을 해야함
    con.commit()
    print('commit 완료!')

    con.close()
    print('연결끊기 완료!')

def read():
    # 1. mysql과 연결
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    print(con)
    print("호스트 정보 출력 >> ", con.get_host_info())
    print('DB 연결 완료')

    # 2. 스트림안의 데이터를 다룰 수 있는 부품인 cursor를 획득한다.
    curs = con.cursor()  # 연결후 corsor()함수를 이용해서 연결(연결통로: Stream)되어 왔다갓다하는 데이터를 가져올 데이터를 가르쳐 어떠한 행동을 할 수 있게함
    print(curs)
    print('cursor객체 사용 가능!')

    # id가 apple인것에 대한 레코드를 가져와라
    sql = "select * from member where id = 'apple'"
    curs.execute(sql)


    row = curs.fetchone() # fetchone은 조건에 맞는 목록을 하나만 가져온다
    # curs.fetchall()   # 조건에 맞는 목록을 모두 가져온다
    # curs.fetchmany(개수)  # 조건에 맞는 목록을 개수만큼 가져온다
    print(row)
    #print(type(row))
    #print(row['id'])

    con.close()

def read2(id1):
    # 1. mysql과 연결
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    print(con)
    print("호스트 정보 출력 >> ", con.get_host_info())
    print('DB 연결 완료')

    # 2. 스트림안의 데이터를 다룰 수 있는 부품인 cursor를 획득한다.
    curs = con.cursor()  # 연결후 corsor()함수를 이용해서 연결(연결통로: Stream)되어 왔다갓다하는 데이터를 가져올 데이터를 가르쳐 어떠한 행동을 할 수 있게함
    print(curs)
    print('cursor객체 사용 가능!')

    # id가 apple인것에 대한 레코드를 가져와라
    sql = "select * from member where id = %s"
    curs.execute(sql, id1)  # element, item, field, property

    row = curs.fetchone()  # fetchone은 조건에 맞는 목록을 하나만 가져온다
    # curs.fetchall()   # 조건에 맞는 목록을 모두 가져온다
    # curs.fetchmany(개수)  # 조건에 맞는 목록을 개수만큼 가져온다
    print(row)
    print(type(row))
    print(row[0])

    con.close()

def read3():
    # 1. mysql과 연결
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    print(con)
    print("호스트 정보 출력 >> ", con.get_host_info())
    print('DB 연결 완료')

    # 2. 스트림안의 데이터를 다룰 수 있는 부품인 cursor를 획득한다.
    curs = con.cursor(pymysql.cursors.DictCursor)  # 연결후 corsor()함수를 이용해서 연결(연결통로: Stream)되어 왔다갓다하는 데이터를 가져올 데이터를 가르쳐 어떠한 행동을 할 수 있게함
    # cursor의 기본값은 tuple 이지만, Dictionary 형식으로 바꾸고 싶을때는 corsor()의 괄호 안에 pymysql.cursors.DictCursor를 넣어주면 Dictionary 형식으로 데이터를 가져오게 된다.
    print(curs)
    print('cursor객체 사용 가능!')

    # id가 apple인것에 대한 레코드를 가져와라
    sql = "select * from member"
    curs.execute(sql)  # element, item, field, property

    # curs.fetchone()  # fetchone은 조건에 맞는 목록을 하나만 가져온다
    rows = curs.fetchall()   # 조건에 맞는 목록을 모두 가져온다
    # curs.fetchmany(개수)  # 조건에 맞는 목록을 개수만큼 가져온다
    print(rows)
    print(type(rows))

    for row in rows:
        print(row)

    con.close()

def update(id, tel):
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    print(con)
    print("호스트 정보 출력 >> ", con.get_host_info())
    print('DB 연결 완료')

    curs = con.cursor()  # 연결후 corsor()함수를 이용해서 연결되어 왔다갓다하는 데이터를 가져올 데이터를 가르쳐 어떠한 행동을 할 수 있게함
    print(curs)
    print('cursor객체 사용 가능!')

    data = (tel, id)
    sql = "update member set tel = %s where id =%s"
    result = curs.execute(sql, data)
    print(result)
    print('SQL문을 만들어서 DB로 보냈음!')

    con.commit()
    print('commit 완료!')

    con.close()
    print('연결 끊기 완료!')

def delete(id):
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    print('호스트 입력정보 >> ', con.get_host_info())
    print('DB연결 완료')

    curs = con.cursor()
    print(curs)
    print('cursor 객체 사용 가능')

    sql = 'delete from member where id="' + id + '"'
    result = curs.execute(sql)
    print(result)
    print('sql문을 DB로 보냄')

    con.commit()
    print('commit 완료')

    con.close()
    print('연결 해제')

def create2(data):
    print(data)

    # 1. mysql과 연결
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    print(con)
    print("호스트 정보 출력 >> ", con.get_host_info())
    print('DB 연결 완료')

    # 2. 스트림안의 데이터를 다룰 수 있는 부품인 cursor를 획득한다.
    curs = con.cursor() # 연결후 corsor()함수를 이용해서 연결(연결통로: Stream)되어 왔다갓다하는 데이터를 가져올 데이터를 가르쳐 어떠한 행동을 할 수 있게함
    print(curs)
    print('cursor객체 사용 가능!')

    # 3. SQL문을 만들어서 전송함
    # SQL문 생성
    sql = 'insert into member values (%s, %s, %s, %s)'
    result = curs.execute(sql, data)
    print('처리 결과 ' + str(result) + '개')
    print('sql문 생성 완료! DB로 보냈어요!')

    # 4. auto-commit 설정이 되어있지 않아서 commit을 해서 디비에 반영을 해야함
    con.commit()
    print('commit 완료!')

    con.close()
    print('연결끊기 완료!')

def create3(datas):
    print(datas)

    # 1. mysql과 연결
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    print(con)
    print("호스트 정보 출력 >> ", con.get_host_info())
    print('DB 연결 완료')

    # 2. 스트림안의 데이터를 다룰 수 있는 부품인 cursor를 획득한다.
    curs = con.cursor() # 연결후 corsor()함수를 이용해서 연결(연결통로: Stream)되어 왔다갓다하는 데이터를 가져올 데이터를 가르쳐 어떠한 행동을 할 수 있게함
    print(curs)
    print('cursor객체 사용 가능!')

    # 3. SQL문을 만들어서 전송함
    # SQL문 생성
    sql = 'insert into member values (%s, %s, %s, %s)'
    result = curs.executemany(sql, datas)
    print('처리 결과 ' + str(result) + '개')
    print('sql문 생성 완료! DB로 보냈어요!')

    # 4. auto-commit 설정이 되어있지 않아서 commit을 해서 디비에 반영을 해야함
    con.commit()
    print('commit 완료!')

    con.close()
    print('연결끊기 완료!')

