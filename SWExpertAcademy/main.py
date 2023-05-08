# /html/body/div[4]/div[2]/div/div[1]/p/text()
# - 문제 제목

# /html/body/div[4]/div[2]/div/div[7]/div/div[3]/div[1]/div[1]/div/a[2]
# - input

# /html/body/div[4]/div[2]/div/div[7]/div/div[3]/div[2]/div/div/a[2]
# - output

import requests

path = 'https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QSEhaA5sDFAUq&categoryId=AV5QSEhaA5sDFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=&pageSize=10&pageIndex=1'

response = requests.get(path)
print(response.text)