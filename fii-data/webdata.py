from urllib.request import Request, urlopen

def get_fii_webpage(ticker):
    '''Takes the ticker of an FII and saves its fiis.com.br entry as a local HTML file'''

    url_base = 'https://fiis.com.br/' #Site with the information we need
    url = url_base + ticker

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    web_byte = urlopen(req).read()
    webContent = web_byte.decode('utf-8')
    
    #Saves the web page as HTML file
    with open('local_files/' + ticker + '.html', 'w', encoding='utf-8') as local_page:
        local_page.write(webContent)
    
    print(f'{ticker} web page saved')

    
if __name__ == '__main__':
    print(get_fii_webpage.__doc__)

    ticker_list = ['btlg11', 'hglg11', 'rbrp11', 'mxrf11', 'mall11', 'snff11'] #list of FIIs that we want to get information
    for ticker in ticker_list:
        get_fii_webpage(ticker)