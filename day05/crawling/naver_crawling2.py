#import bs4
from bs4 import BeautifulSoup
from urllib import request      # urllib는 기본적으로 갖고있는 라이브러리다

#BeautifulSoup()
con = request.urlopen('https://finance.naver.com/item/main.nhn?code=005930') # 네이버 증권 페이지에서 삼성전자에 관한 url 오픈
print('1. 연결 성공\n', con)
print('----------------')
name = '삼성전자'
print(name)
doc = BeautifulSoup(con, 'html.parser')   # html.parser : html 분석기능
# print('2. 받은 것을 프린트>>', doc)  # 너무 많아서 일단 주석처리
    # doc 안에는 naver.com의 첫페이지인 index.heml 파일의 소스가 통째로 들어있다.

span_code = doc.select('span.code')     # 검색의 결과를 리스트(무조건)로!
print('code의 갯수 >>> ', (len(span_code)))
code =  span_code[0].text
print('종목 번호: ', code)

# div_today = doc.select('div.today')
# print('today의 주가 >>> ', (len(div_today)))
# today = div_today[0]
# print('today: ', today)

span_blind = doc.select('span.blind')
print('span.blind 갯수 >>> ', (len(span_blind)))

for x in range(len(span_blind)):
    print(x, '번째 : ', span_blind[x].text)

print('-----------------------')
#전일, 고가, 시가, 저가
now = span_blind[12].text       # 현재가
yesterday = span_blind[15].text # 전일
high = span_blind[16].text      # 고가
start = span_blind[19].text     #시가
low = span_blind[20].text       # 저가
print('오늘의 주가 :', now)
# print('전일대비 :', span_blind[13].text)
# print('전일대비(비율) :', span_blind[14].text)
print('전일 :', yesterday)
print('고가 :', high)
# print('상한가 :', span_blind[17].text)
# print('거래량 :', span_blind[18].text)
print('시가 :', start)
print('저가 :', low)
# print('거래대금 :', span_blind[21].text)

# 한번에 찾을 경우 ' '(공백) 을 주어서 하위로 구분해서 한다.
all = doc.select('div.today span.blind')
print(len(all))
print(all[0])
for x in range(len(all)):
    print(x, " :", all[x].text)

file = open(name + '.txt', 'w')
file.write('종목 번호: ' + code + '\n')
file.write('오늘의 주가 : ' + now + '\n')
file.write('전일 : ' + yesterday + '\n')
file.write('고가 : ' + high + '\n')
file.write('시가 : ' + start + '\n')
file.write('저가 : ' + low + '\n')
file.close()
