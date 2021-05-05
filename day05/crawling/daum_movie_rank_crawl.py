from bs4 import BeautifulSoup
from urllib import request

name_list = ['소울(2020)', '명탐정코난_진홍의 수학여행(2019)', '나는 나를 해고하지 않는다(2020)', '블라인드(2007)', '키드(1921)']
add_list = ['136715', '145835', '141717', '45494', '13552']
print('=========================================')

for i in range(len(add_list)):
    name = name_list[i]
    print()
    mov = request.urlopen('https://movie.daum.net/moviedb/main?movieId=' + add_list[i])
    doc = BeautifulSoup(mov, 'html.parser')
    span_txt = doc.select('span.txt_name')
    ti = span_txt[0].text
    print('제목 :', ti)

    a_grade = doc.select('div.info_origin a.link_grade')
    grade = a_grade[0].text
    grade_only = grade[3:6]
    gra = grade_only
    print('평점 :', gra, '점')

    a_rank = doc.select('a.link_txt')
    rank_only = a_rank[0].text
    rank = rank_only[:-1]
    print('예매 순위 :', rank, '위')

    a_audience = doc.select('a.link_num')
    audience = a_audience[0].text
    print('누적 관객 :', audience, '명')
    print()
    print('=========================================')

    file = open(name + '.txt', 'w')
    file.write('---------------------------\n')
    file.write('제    목 : ' + ti + '\n')
    file.write('평    점 : ' + gra + '\n')
    file.write('예매 순위 : ' + rank + '\n')
    file.write('누적 관객 : ' + audience + '\n')
    file.write('---------------------------\n')
    file.close()


