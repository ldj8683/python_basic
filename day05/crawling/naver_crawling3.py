from bs4 import BeautifulSoup
from urllib import request      # urllib는 기본적으로 갖고있는 라이브러리다

name_list = ['삼성전자', '현대자동차', '카카오', 'LG전자', '셀트리온']
add_code = ['005930', '005380', '035720', '066570', '068270']
print('=============================')
for i in range(len(add_code)):
    name = name_list[i]
    con = request.urlopen('https://finance.naver.com/item/main.nhn?code=' + add_code[i]) # 네이버 증권 페이지에서 삼성전자에 관한 url 오픈

    doc = BeautifulSoup(con, 'html.parser')   # html.parser : html 분석기능
    span_code = doc.select('span.code')     # 검색의 결과를 리스트(무조건)로!

    code = span_code[0].text
    print('종목 번호 :', code)
    print('종목 이름 :', name)
    span_blind = doc.select('span.blind')
    now = span_blind[12].text       # 현재가
    yesterday = span_blind[15].text # 전일
    high = span_blind[16].text      # 고가
    start = span_blind[19].text     # 시가
    low = span_blind[20].text       # 저가
    print('--------------------')
    print('오늘의 주가 :', now)
    print('--------------------')
    print('전일 :', yesterday)
    print('고가 :', high)
    print('시가 :', start)
    print('저가 :', low)
    print()
    print('=============================')

    file = open(name + '.txt', 'w')
    file.write('---------------------------\n')
    file.write('종목 이름 : ' + name + '\n')
    file.write('종목 번호 : ' + code + '\n')
    file.write('오늘의 주가 : ' + now + '\n')
    file.write('전일 : ' + yesterday + '\n')
    file.write('고가 : ' + high + '\n')
    file.write('시가 : ' + start + '\n')
    file.write('저가 : ' + low + '\n')
    file.write('---------------------------\n')
    file.close()


