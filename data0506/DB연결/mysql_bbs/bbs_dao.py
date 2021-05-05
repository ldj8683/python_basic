import pymysql

def create(datas1):
    print("DB와 연결 전 입력 데이터 확인 >> " + str(datas1))

    # 1. mysql과 연결
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    print(con)
    print('DB 연결 완료')

    # 2. 스트림안의 데이터를 다룰 수 있는 부품인 cursor를 생성(획득)
    cur = con.cursor()
    print('cursor 객체 생성 완료')

    # 3. SQL문을 만들어서 전함
    sql = 'insert into bbs values (%s, %s, %s, %s)'
    result = cur.execute(sql, datas1)
    print('처리 결과 >> ' + str(result) + '개')
    print('SQL문 생성 완료, DB로 전송!')

    # 4. auto-commit 설정이 되어있지 않아서 commit을 해서 디비에 반영
    con.commit()
    print('commit 완료')

    con.close()
    print('DB 연결 종료')

def read(id1):
    print("DB와 연결 전 입력 데이터 확인 >> " + str(id1))

    # 1. mysql과 연결
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    print(con)
    print('DB 연결 완료')

    # 2. 스트림안의 데이터를 다룰 수 있는 부품인 cursor를 생성(획득)
    cur = con.cursor(pymysql.cursors.DictCursor)
    print('cursor 객체 생성 완료')

    # 3. SQL문을 만들어서 전함
    sql = 'select * from bbs where id = %s'
    cur.execute(sql, id1)
    print('SQL문 생성 완료, DB로 전송!')

    # 4. 가져온 레코드들을 확인
    row = cur.fetchone()
    print(row)

    con.close()
    print('DB 연결 종료')

def update(datas2):
    print("DB와 연결 전 입력 데이터 확인 >> " + str(datas2))

    # 1. mysql과 연결
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    print(con)
    print('DB 연결 완료')

    # 2. 스트림안의 데이터를 다룰 수 있는 부품인 cursor를 생성(획득)
    cur = con.cursor()
    print('cursor 객체 생성 완료')

    # 3. SQL문을 만들어서 전함
    sql = 'update bbs set title = %s, content = %s where id = %s'
    result = cur.execute(sql, datas2)
    print('처리 결과 >> ' + str(result) + '개')
    print('SQL문 생성 완료, DB로 전송!')

    # 4. auto-commit 설정이 되어있지 않아서 commit을 해서 디비에 반영
    con.commit()
    print('commit 완료')

    con.close()
    print('DB 연결 종료')

def all():
    # 1. mysql과 연결
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    print(con)
    print('DB 연결 완료')

    # 2. 스트림안의 데이터를 다룰 수 있는 부품인 cursor를 생성(획득)
    # 딕셔너리 형식으로 가져온다.
    cur = con.cursor(pymysql.cursors.DictCursor)
    print('cursor 객체 생성 완료')

    # 3. SQL문을 만들어서 전함
    sql = 'select * from bbs'
    cur.execute(sql)
    print('SQL문 생성 완료, DB로 전송!')

    # 4. 가져온 레코드들을 확인
    rows = cur.fetchall()
    for x in rows:
        print(x)

    con.close()
    print('DB 연결 종료')
