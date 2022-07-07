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

############################
# 포켓몬 표에서 셀 값 추출하기
############################

url='http://pokemondb.net/pokedex/all' # 포켓몬 표 주소

page = requests.get(url)               # URL 정보 가져오기
doc = lh.fromstring(page.content)      # 콘텐츠 정보 저장 
tr_elements = doc.xpath('//tr')        # HTML <tr> 정보 

# col = [(t.text_content(), []) for t in tr_elements[0]] # Column 제목///
titles = [(t.text_content()) for t in tr_elements[0]] # Column 제목

# Pandas DataFrame 생성
cols = [] * len(titles) # 자자의 오타인 듯
cols = [[]] * len(titles) # 메모리 참조 오류 주의
cols = [[] for _ in range(titles)] # 정상 작동

for T in tr_elements[1:]:
  for i, t in enumerate(T.iterchildren()):
    data = t.text_content() 
    cols[i].append(int(data) if data.isnumeric() else data)


#########################
# Pandas DataFrame 생성 #
#########################

# 크롤링한 정보를 Pandas DataFrame으로 생성
temp_dic = {title:column for title,column in col}
df = pd.DataFrame(temp_dic)

# DataFrame 정보 확인
print(df.head())

# 바이너리(binary) 형태로 저장 -> 향후 Jupyter Notebook에서 활용
with open('poketmon.pkl', 'wb') as f:
    pickle.dump(df, f)

print('Bye, end of computation ^^.')

col = [(t.text_content(), []) for t in tr_elements[0]]
