from webdata import get_fii_webpage
from webscraping import get_fii_main_indicators, get_fii_dividends_series

ticker_list = ['btlg11', 'hglg11', 'rbrp11', 'mxrf11', 'mall11', 'snff11'] #list of FIIs that we want indicators and dividends serie

##First, we get the webpage of each FII as a local HTML file
for ticker in ticker_list:
    get_fii_webpage(ticker)

##Then, we extract, from each page, the main indicators data and dividends series
for ticker in ticker_list:
    get_fii_main_indicators(ticker)
    get_fii_dividends_series(ticker)