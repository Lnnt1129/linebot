import requests
from bs4 import BeautifulSoup

def read( word ):
    url = f'https://sutian.moe.edu.tw/zh-hant/tshiau/?lui=tai_su&tsha={word}#table d-md-none'

    html = requests.get( url )
    bs = BeautifulSoup(html.text,'lxml')
    data = bs.find('table', id='table d-md-none')
    try:
        row = data.find_all('tr')[1]
        chinese = row.find('a').text.strip()
        phones = data.find_all('td')[2]
        phone = [e.text for e in phones]
        s = " ".join( phone ).split()[0]
        # s = row.find('sub')
        #print( chinese, s )
        return chinese + ' => ' + s
    except:
        print( '查無此字' )