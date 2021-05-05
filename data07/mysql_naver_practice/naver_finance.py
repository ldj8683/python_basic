import requests
from bs4 import BeautifulSoup
import finance_curd as db

url = "https://finance.naver.com/sise/sise_quant.nhn?sosok=0"
result = requests.get(url)
print(result)

content = BeautifulSoup(result.content, "html.parser")

title1 = content.findAll('a', {"class": "tltle"})
# print(title1)

title_list = []
for tag in title1:
    # print(tag.text)
    title_data = tag.text
    title_list.append(title_data)

# print(len(title_list))
# print(title_list)

price1 = content.findAll('td', {"class": "number"})
print('현재가격 >> ', price1[0].text)
print('시가총액 >> ', price1[7].text)
print(price1[10].text)

count1 = 1
price1_list = []
for index in range(0, len(price1), 10):
    #print(count1, '의 현재가 >>', price1[index].text)
    count1 = count1 + 1
    price1_list.append(price1[index].text.replace(",", ""))

count2 = 1
price2_list = []
for index in range(7, len(price1), 10):
    #print(count2, '의 시가총액 >>', price1[index].text)
    count2 = count2 + 1
    price2_list.append(price1[index].text.replace(",", ""))

print(len(title_list))
print(len(price1_list))
print(len(price2_list))

for index in range(0,100):
    print('종목 >>', title_list[index], '| 현재가 >>', price1_list[index], '| 시가총액 >>', price2_list[index])


title_list2 = tuple(title_list)
price1_list2 = tuple(price1_list)
price2_list2 = tuple(price2_list)

print(title_list)
print(type(title_list))
print(price1_list)
print(type(price1_list))
print(price2_list)
print(type(price2_list))
print('----------------------------')
print(title_list2)
print(price1_list2)
print(price2_list2)


total_semi = list(zip(title_list, price1_list))
print(total_semi)

total = list(zip(title_list, price1_list, price2_list))
print(total)

db.create(total)
