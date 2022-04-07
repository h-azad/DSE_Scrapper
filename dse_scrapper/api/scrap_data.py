import enum
from itertools import count
from bs4 import BeautifulSoup
import requests
import pandas as pd
import json

def getStockRecords(filter = 'default'):

    if(filter == 'default'):
        page = requests.get(
            "https://www.dsebd.org/latest_share_price_scroll_l.php")
    elif(filter=='value'):
        page = requests.get(
            "https://www.dsebd.org/latest_share_price_scroll_by_value.php")
    elif(filter=='volume'):
        page = requests.get(
            "https://www.dsebd.org/latest_share_price_scroll_by_volume.php")
    elif(filter=='change'):
        page = requests.get(
            "https://www.dsebd.org/latest_share_price_scroll_by_change.php")
    else:
        return

    soup = BeautifulSoup(page.content, 'html.parser')

    html = list(soup.children)[2]

    body = list(html.children)[4]

    rightContainer = soup.find(id="RightBody").find('table')

    tableRows = rightContainer.find_all('tr')

    tableHeader = tableRows[0].find_all('th')

    headerInfo = ['trading_code', 'ltp', 'high', 'low', 'closep', 'ycp', 'change', 'trade', 'value', 'volume']

    allInfo = []

    for tr in tableRows[1:]:
        tds = tr.find_all('td')
        tds = list(tds)
        rowInfo = []

        for index, item in enumerate(tds, start=1):
            if(index != 1):
                # print(index)
                rowInfo.append(item.text.strip())
        allInfo.append(rowInfo)

    df = pd.DataFrame(allInfo)
    df.columns = headerInfo

    return df.to_dict(orient='records')


def getCircuitBreakerRecords():

    page = requests.get(
        "https://www.dsebd.org/cbul.php")

    soup = BeautifulSoup(page.content, 'html.parser')

    html = list(soup.children)[2]

    body = list(html.children)[4]

    rightContainer = soup.find(id="RightBody").find('table')

    tableRows = rightContainer.find_all('tr')

    tableHeader = tableRows[0].find_all('th')

    headerInfo = ['trade', 'codebreaker', 'tick_size', 'open_adj_price', 'lower_limit', 'upper_limit']

    # exit()

    allInfo = []

    for tr in tableRows[1:]:
        tds = tr.find_all('td')
        tds = list(tds)
        rowInfo = []

        for index, item in enumerate(tds, start=1):
            if(index != 1):
                # print(index)
                rowInfo.append(item.text.strip())
        allInfo.append(rowInfo)

    df = pd.DataFrame(allInfo)
    df.columns = headerInfo

    return df.to_dict(orient='records')


def getTopGainerRecords():

    page = requests.get(
        "https://www.dsebd.org/top_ten_gainer.php")

    soup = BeautifulSoup(page.content, 'html.parser')

    html = list(soup.children)[2]

    body = list(html.children)[4]

    rightContainer = soup.find(id="RightBody").find_all('table')
    rightContainer = list(rightContainer)

    cpy_table_rows = rightContainer[0].find_all('tr')
    opl_table_rows = rightContainer[1].find_all('tr')

    allRecords = {}

    all_cpy_Info = []

    headerInfo = ['trading_code', 'closep', 'high', 'low', 'ycp', 'change']
              
    for tr in cpy_table_rows[1:]:
        tds = tr.find_all('td')
        tds = list(tds)
        rowInfo = []

        for index, item in enumerate(tds, start=1):
            if(index != 1):
                # print(index)
                rowInfo.append(item.text.strip())
        all_cpy_Info.append(rowInfo)
    
    df = pd.DataFrame(all_cpy_Info)
    df.columns = headerInfo
    
    allRecords.update({'cpy': df.to_dict(orient='records')})

    all_opl_Info = []

    headerInfo = ['trading_code', 'closep', 'high', 'low', 'ycp', 'change']

    for tr in opl_table_rows[1:]:
        tds = tr.find_all('td')
        tds = list(tds)
        rowInfo = []

        for index, item in enumerate(tds, start=1):
            if(index != 1):
                # print(index)
                rowInfo.append(item.text.strip())
        all_opl_Info.append(rowInfo)

    df = pd.DataFrame(all_opl_Info)
    df.columns = headerInfo
    
    allRecords.update({'olp': df.to_dict(orient='records')})

    return allRecords


def getTopLooserRecords():

    page = requests.get(
        "https://www.dsebd.org/top_ten_loser.php")

    soup = BeautifulSoup(page.content, 'html.parser')

    html = list(soup.children)[2]

    body = list(html.children)[4]

    rightContainer = soup.find(id="RightBody").find_all('table')
    rightContainer = list(rightContainer)

    cpy_table_rows = rightContainer[0].find_all('tr')
    opl_table_rows = rightContainer[1].find_all('tr')

    allRecords = {}

    all_cpy_Info = []

    headerInfo = ['trading_code', 'closep', 'high', 'low', 'ycp', 'change']

    for tr in cpy_table_rows[1:]:
        tds = tr.find_all('td')
        tds = list(tds)
        rowInfo = []

        for index, item in enumerate(tds, start=1):
            if(index != 1):
                # print(index)
                rowInfo.append(item.text.strip())
        all_cpy_Info.append(rowInfo)

    df = pd.DataFrame(all_cpy_Info)
    df.columns = headerInfo

    allRecords.update({'cpy': df.to_dict(orient='records')})

    all_opl_Info = []

    headerInfo = ['trading_code', 'closep', 'high', 'low', 'ycp', 'change']

    for tr in opl_table_rows[1:]:
        tds = tr.find_all('td')
        tds = list(tds)
        rowInfo = []

        for index, item in enumerate(tds, start=1):
            if(index != 1):
                # print(index)
                rowInfo.append(item.text.strip())
        all_opl_Info.append(rowInfo)

    df = pd.DataFrame(all_opl_Info)
    df.columns = headerInfo

    allRecords.update({'olp': df.to_dict(orient='records')})

    return allRecords


def getListedCompanies():
    page = requests.get(
        "https://www.dsebd.org/company_listing.php")

    soup = BeautifulSoup(page.content, 'html.parser')

    html = list(soup.children)[2]

    # body = list(html.children)[4]

    rightContainer = soup.find(id="RightBody")

    company_categories = rightContainer.find(id = "top")
    company_categories = company_categories.find_all('a', attrs={"name" : "_top"})

    allRecordData = []

    for cmpc in company_categories:
        c_companies = rightContainer.find(id=cmpc.text)
        companies_tc = c_companies.find_all(
            ['a', 'span'], class_=lambda x: x not in ['showClass'])
        i = 1
        n = len(companies_tc[1:])
        while(i <= n):
            if(companies_tc[i].text != "More..."):
                # print(companies_tc[i].text, '-', companies_tc[i+1].text.strip("()"))
                allRecordData.append(
                    {'trade_code': companies_tc[i].text, 'trade_name': companies_tc[i+1].text.strip("()").title()})
            i += 2

    return allRecordData
