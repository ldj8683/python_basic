import DB연결.mysql연결모듈 as db

# VO 역할
data1 = ("data1", "data1", "data1", "data1")
data2 = ("data2", "data2", "data2", "data2")
data3 = ("data3", "data3", "data3", "data3")

datas = (data1, data2, data3)
print('입력된 데이터 >> ', datas)
db.create3(datas)
