#!/usr/bin/env python
#importar pyquery
from pyquery import *


#html = PyQuery(url='http://bitcoinity.org/markets/btce/EUR')



#lprice = html('#last_price').text()
#lbuy = html('#last_buy').text()
#lsell = html('#last_sell').text()



#print lprice #,lbuy,lsell

html = PyQuery(url='https://btc-e.com/exchange/btc_eur')



lprice = html('div#orders-stats').text()

print "BTC-E " + lprice[12:-27]


