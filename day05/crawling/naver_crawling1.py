#import bs4
from bs4 import BeautifulSoup
from urllib import request      # urllib는 기본적으로 갖고있는 라이브러리다

#BeautifulSoup()
con = request.urlopen('http://www.naver.com') # 연결부품획득 urlopen은 url을 여는 함수로, 열기세 성공하면 response.status 값이 200이 나옴, 이 200은 http상태코드로 웹서 요청이 제대로 처리되었음을 알려준다.
print('1. 연결 성공\n', con)
print('----------------')

doc = BeautifulSoup(con, 'html.parser')   # html.parser : html 분석기능
# print('2. 받은 것을 프린트>>', doc)  # 너무 많아서 일단 주석처리
    # doc 안에는 naver.com의 첫페이지인 index.heml 파일의 소스가 통째로 들어있다.

a_nav = doc.select('a.nav')     # 검색의 결과를 리스트로!
print(a_nav)
print((len(a_nav)))     # <a > ... </a> -> a 테그라고 함

print(a_nav[0])
print(a_nav[0].text)
print(a_nav[7].text)
print(a_nav[8].text)
print(a_nav[9].text)

print('--전체 텍스트 추출--')
for x in range(len(a_nav)):
    print(a_nav[x].text)
print('--범위 텍스트 추출--')
for x in range(7, 10):
    print(a_nav[x].text)

