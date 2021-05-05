import pymysql

con = pymysql.connect(host='localhost', user='root', password='1234', port = 3306, db = 'shop')
print(con)

curs = con.cursor()
print(curs)

sql = 'insert into member values ("python", "python", "python", "python")'
curs.execute(sql)

con.commit()