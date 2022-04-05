from itertools import count
from bs4 import BeautifulSoup
import requests
import pandas as pd

def getStockRecords():

    page = requests.get(
        "https://www.dsebd.org/latest_share_price_scroll_by_ltp.php")

    soup = BeautifulSoup(page.content, 'html.parser')

    html = list(soup.children)[2]

    body = list(html.children)[4]

    rightContainer = soup.find(id="RightBody").find('table')

    tableRows = rightContainer.find_all('tr')

    tableHeader = tableRows[0].find_all('th')

    headerInfo = []
    for th in tableHeader:
        headerInfo.append(th.text.strip())
    # print(headerInfo)
    # exit()

    allInfo = []

    for tr in tableRows[1:]:
        tds = tr.find_all('td')
        tds = list(tds)
        rowInfo = []

        for index, item in enumerate(tds, start=1):
            rowInfo.append(item.text.strip())
        allInfo.append(rowInfo)

    df = pd.DataFrame(allInfo)
    df.columns = headerInfo

    # df.to_csv('file1.csv')
    return df.to_json(orient='records')
    # return allInfo
# print(df)
