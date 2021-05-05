import pymysql

def create(datas):
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = 'insert into finance values (null, %s, %s, %s)'
    result = cur.executemany(sql, datas)
    print('처리 결과 >>', result, '개')

    con.commit()
    con.close()
