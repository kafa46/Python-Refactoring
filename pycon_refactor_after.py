'''Source Code Description
1. Python Refactoring Tutorial
    - Title: Beautiful Python Refactoring
    - Author: Conor Hoekstra
            Engineer in NVIDIA
    - Presented at: PyCon 2020
    - Video: Youtube -> https://www.youtube.com/watch?v=KTIl1MugsSY

2. Source Codes
    - Title: Web Scraping HTML Tables with Python 
    - Web link: https://towardsdatascience.com/web-scraping-html-tables-with-python-c9baba21059
    - Author: Syed Sadat Nazrul
            Machine Learning Scientist at Amazon
'''

import requests
import lxml.html as lh
import pandas as pd
import pickle


url='http://pokemondb.net/pokedex/all' # 포켓몬 표 주소

page = requests.get(url)               # URL 정보 가져오기
doc = lh.fromstring(page.content)      # 콘텐츠 정보 저장 
tr_elements = doc.xpath('//tr')        # HTML <tr> 정보 
# titles = [(t.text_content(), []) for t in tr_elements[0]] # Column 제목
# titles = ((t.text_content(), []) for t in tr_elements[0]) # Column 제목
titles = [t.text_content() for  t in tr_elements[0]]
# cols = [[] for _ in range(titles)]

# 데이터 뽑아오는 함수
get_data = lambda data: int(data) if data.isnumeric() else data

# Column 데이터 리팩토링 전 (before)
cols1 = [[] for _ in titles]
for T in tr_elements[1:]:
    for i, t in enumerate(T.iterchildren()):
        cols1[i].append(get_data(t.text_content()))

cols_temp1 = [[get_data(t.text_content()) for t in T.iterchildren()] for T in tr_elements[1:]]
cols_temp2 = zip(*[[get_data(t.text_content()) for t in T.iterchildren()] for T in tr_elements[1:]])
cols_temp3 = list(zip(*[[get_data(t.text_content()) for t in T.iterchildren()] for T in tr_elements[1:]]))

# Column 데이터 리팩토링 후(after)
cols2 = list(zip(*[[get_data(t.text_content()) for t in T.iterchildren()] for T in tr_elements[1:]]))

# 크롤링한 정보를 Pandas DataFrame으로 생성
temp_dic1 = {title:column for title, column in zip(titles, cols2)} # 저자 코드 (from Youtube)
temp_dic1 = {
    title: col for title, col in zip(titles, cols2)
}


temp_dic2 = dict(zip(titles, cols2)) # 추가로 가능한 코드 from commet of Youtube

df = pd.DataFrame(temp_dic2)

# DataFrame 정보 확인
print(df.head(50))

# 바이너리(binary) 형태로 저장 -> 향후 Jupyter Notebook에서 활용
with open('poketmon.pkl', 'wb') as f:
    pickle.dump(df, f)

print('Bye, end of computation ^^.')

