import urllib.request
import sys, json, re

import dictionary as dictionary


def getStockData():
    stockSymbol = input("Enter a Stock Symbol or type q to quit: ")
    q = ""
    outFile = open('japi.txt', 'w')
    while stockSymbol != 'q':
        full_url = 'https://www.alphavantage.co/query/?function=TIME_SERIES_DAILY&symbol=' + stockSymbol + '&apikey=31DUVB9MCYEI9D9N'
        con = urllib.request.urlopen(full_url)
        res = con.read().decode()
        json_res = json.dumps(res)
        data_out = json.loads(res)
        print(data_out)
        print('Stock: ', stockSymbol, data_out.get('Meta Data'))
        print('The Prices of the stock: ', stockSymbol, 'are ', data_out.get('Time Series (Daily)'))
        stockSymbol = input("Enter a Stock Symbol or type q to quit: ")
        outFile.write('\n' + str(data_out.get('Stock: ', stockSymbol)))

        outFile.write('\n' + str(data_out.get('Time Series (Daily)')))
    print('Stock Quotes Retrieved Successfully!')
    outFile.close()
getStockData()
