import requests
import pandas as pd
from bs4 import BeautifulSoup
import mysql_movie.movie_curd2 as db3

url = "https://movie.naver.com/movie/running/current.nhn"
result = requests.get(url)
print(result)
# print(result.content)

# content 는 html documnet를 DOM Tree형식으로 익식을 하게 끔 해주는 주소
content = BeautifulSoup(result.content, "html.parser")

# <dt class="tit">인 것들을 찾아주는 findALL
# dt_list : ResultSet class의  객체, List의 상속!
# 인덱싱과 슬라이싱이 된다!
dt_list = content.findAll("dt", {"class": "tit"})
print(type(dt_list))    # ResultSet 클래스의 객체
# print(dt_list)      # 전체 목록 프린트
print('리스트의 갯수 >> ', len(dt_list))
tag = dt_list[0].find("a") # find("a")는 a태그를 찾을때 사용
print(tag)
print(type(tag))
print(tag.text)     # a tag 사이에 있는 text를 가져옴

span_num = content.findAll("span", {"class": "num"})
print(len(span_num))
print(span_num)
tag2 = span_num[0]
print(tag2.text)


print('-----------------------------------')
for index in range(0, len(span_num), 2):
    print(index, ": ", span_num[index].text)
print('-----------------------------------')
for index in range(0, len(dt_list)):
    print(index + 1, ": ", dt_list[index].find("a").text)
print('-----------------------------------')

title_list = []
for tag3 in dt_list:
    print(tag3.find('a').text)
    data = tag3.find('a').text
    title_list.append(data)

print("title_list의 길이", len(title_list))
print(title_list)

jumsu_list = []
for index in range(0, 146):
    data = span_num[index].text
    jumsu_list.append(data.strip())
print("jumsu_list의 길이", len(jumsu_list))
print(jumsu_list)

title_list2 = tuple(title_list)
print(title_list2)
jumsu_list2 = tuple(jumsu_list)
print(jumsu_list2)

jumsu_list3 = list(jumsu_list2)
total = list(zip(title_list, jumsu_list2))
print("1", len(title_list))
print("2", len(title_list2))

print(type(total))
print(len(total))
print(total)
total2 = tuple(total)
print(type(total2))
print(len(total2))
print(total2)
print('========================')

# db3.create(jumsu_list2)
# db3.create2(title_list2)
# db3.create2(total)


