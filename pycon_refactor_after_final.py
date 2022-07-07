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

import pickle
import requests
import lxml.html as lh
import pandas as pd

def main(url:str = 'http://pokemondb.net/pokedex/all') -> None:
    '''The final codes after refactoring'''

    page = requests.get(url)               # get webpage using URL
    doc = lh.fromstring(page.content)      # extract page content
    tr_elements = doc.xpath('//tr')        # parse information of HTML <tr> tag
    titles = [t.text_content() for  t in tr_elements[0]]

    get_data = lambda data: int(data) if data.isnumeric() else data
    cols2 = list(zip(*[[get_data(t.text_content()) for t in T.iterchildren()] for T in tr_elements[1:]]))
    temp_dic = dict(zip(titles, cols2))
    df = pd.DataFrame(temp_dic)

    # Save data onto disk
    with open('poketmon.pkl', 'wb') as f:
        pickle.dump(df, f)
    

if __name__=='__main__':
    main()
