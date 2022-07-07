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

# 포켓몬 표 주소
url='http://pokemondb.net/pokedex/all'

# 해당 주소에서 URL 정보 가져오기
page = requests.get(url)

# doc 변수에 URL 정보 중 콘텐츠 정보를 doc 변수에 저장
doc = lh.fromstring(page.content)

# HTML의 <tr>..</tr> 사이에 존재하는 데이터 추출(파싱, parsing)
tr_elements = doc.xpath('//tr')

# 처음 12개 데이터 길이 확인
temp1 = [len(T) for T in tr_elements[:12]]
print(f'Lenth of header in first 10 rows: {temp1}') 
# 각 행(row)는 10개의 테이블 데이터 보유
# 아래와 같은 형태의 출력 확인
# 출력 형태 -> [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]


##################################################
# 포켓몬 표에서 컬럼 정보 (table header) 추출하기 #
##################################################

# 표 제목 정보를 담기 위한 리스트 생성
# 각각의 행에서, 첫번째 요소의 이름을 header 이름으로 저장하고
# 나중에 각 header 정보를 담기 위한 빈 리스트를 추가
col = [] # -> 각 header 세로축 정보를 담기 위한 빈 리스트
i = 0    # -> coloum 인덱스    
for t in tr_elements[0]:
    i += 1
    name = t.text_content()
    print('{}: {}'.format(i, name)) # 각 column header 이름 출력 (디버깅 목적)
    col.append((name, []))

'''# 표 제목이 정상적으로 출력되었는지 확인
# 출력 형태->
# 1:"#"
# 2:"Name"
# 3:"Type"
# 4:"Total"
# 5:"HP"
# 6:"Attack"
# 7:"Defense"
# 8:"Sp. Atk"
# 9:"Sp. Def"
# 10:"Speed"'''


#########################
# Pandas DataFrame 생성 #
#########################

# 첫번째 행은 헤더 정보이므로 별도로 저장하고,
#   두번째 행부터 표 데이터가 실제로 저장됩니다.
for j in range(1, len(tr_elements)): # -> 첫번째 행 이후 모든 행을 방문
    
    T = tr_elements[j] # -> 변수 T는 j번째 행을 의미
    
    # 만약 행의 길이가 10이 아니라면,
    #   해당 데이터는 우리가 수집한 데이터가 아님
    if len(T) != 10:
        break
    
    i = 0 # -> i는 각 행의 컬럼(column, 표 header) 인덱스
    
    # 각 행에서 각 열에 해당하는 요소를 방문
    for t in T.iterchildren():
        data = t.text_content() 
        
        # 행이 비어 있는지 확인
        if i > 0: 
            try:
                data = int(data) # -> 글자형태의 숫자 정보가 있다면 정수로 변환
            except:
                pass
        
        col[i][1].append(data)  # -> 추출한 데이터를 i번째 컬럼의 리스트에 추가
        i += 1                  # -> 다음 컬럼으로 이동하기 위해 인덱스 i 값을 1만큼 증가

# 데이터가 정상적으로 추출되었는지 확인
temp2 = [len(C) for title, C in col]
print(f'Lenth of each column: {temp2}') 
# 각 행(row)는 10개의 테이블 데이터 보유
# 아래와 같은 형태의 출력 확인  (디버깅 목적)
# 출력 형태-> [1075, 1075, 1075, 1075, 1075, 1075, 1075, 1075, 1075, 1075] 
#   (해석: 각 컬럼은 1075개 데이터를 가지고 있음)


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
