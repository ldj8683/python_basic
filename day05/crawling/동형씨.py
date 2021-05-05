from bs4 import BeautifulSoup
from urllib import request

name_list = ['소울', '극장판 귀멸의 칼날 무한열차편(2020)', '북스마트', '세자매', '명탐정 코난 진홍의 수학여행(2019)']
code = ['136715', '145371', '129731', '141478', '145835']

for index in range(len(code)):
    name2 = name_list[index]
    mov = request.urlopen('https://movie.daum.net/moviedb/main?movieId=' + code[index])
    doc = BeautifulSoup(mov, 'html.parser')


    span_txt = doc.select('span.txt_name')
    name = span_txt[0].text
    # print(len(span_txt))
    print('제목 :', name)
    # print(mov)

    grade = doc.select('div.info_origin a.link_grade')
    grade1 = grade[0].text
    grade2 = grade1[3:]
    # print(len(grade))
    # print(grade)
    print('평점 :', grade2.strip())

    rank = doc.select('a.link_txt')
    rank1 = rank[0].text
    rank2 = rank1[:-1]
    print('예매 : ', rank2+'위')

    audi = doc.select('a.link_num')
    audi2 = audi[0].text
    print('누적관객 : ', audi2, '명')
    print('----------------------------------')

    file = open(name2 + '.txt', 'w')
    file.write(name + '\n')
    file.write(grade2 + '\n')
    file.write(rank2 + '\n')
    file.write(audi2 + '\n')
    file.close()