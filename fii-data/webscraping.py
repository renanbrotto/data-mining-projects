from bs4 import BeautifulSoup
import pandas as pd

def get_fii_main_indicators(ticker):
    '''Takes the FII ticker and saves its main indicators in a .txt file
    Output Directory: fii_indicators
    '''

    path = './local_files/' #Path to the HTML files with the data
    page_name = path + ticker + '.html'

    with open(page_name, 'r', encoding='utf-8') as html_file:
        content = html_file.read()    
        soup = BeautifulSoup(content, 'lxml')
        indicators_list = soup.find_all('div', class_='indicators__box')
        with open('./fii_indicators/' + ticker + '.txt', 'w') as file:
            for indicator in indicators_list:
                indicator_value, indicator_name = indicator.text.split('\n')[1:3]
                file.write(f'{indicator_name} = {indicator_value}\n')
    
    print(f'{ticker} indicators data saved')

def get_fii_dividends_series(ticker):
    '''Takes the FII ticker and saves its dividends series as a .csv file
    Output Directory: dividends_history
    '''

    path = './local_files/' #Path to the HTML files with the data
    page_name = path + ticker + '.html'

    with open(page_name, 'r', encoding='utf-8') as html_file:
        content = html_file.read()    
        soup = BeautifulSoup(content, 'lxml')
        dividends_table = soup.find_all('div', class_='dividends-table')
        for data in dividends_table:
            content = data.text.split('\n')
            data_content = [value for value in content if value]

        data_base_list = data_content[0::5]
        data_pagamento_list = data_content[1::5]
        cotacao_base_list = data_content[2::5]
        dividend_yield_list = data_content[3::5]
        rendimento_list = data_content[4::5]
        
        df = pd.DataFrame({data_base_list[0]:data_base_list[1::],
                        data_pagamento_list[0]:data_pagamento_list[1::],
                        cotacao_base_list[0]:cotacao_base_list[1::],
                        dividend_yield_list[0]:dividend_yield_list[1::],
                        rendimento_list[0]:rendimento_list[1::]})
        
        df.to_csv('./dividends_history/' + ticker + '_dividends.csv')

    print(f'{ticker} dividends series saved')

if __name__ == '__main__':
    print(get_fii_dividends_series.__doc__)
    print(get_fii_main_indicators.__doc__)
    
    ticker_list = ['btlg11', 'hglg11', 'rbrp11', 'mxrf11', 'mall11', 'snff11'] #list of FIIs that we want indicators and dividends serie
    for ticker in ticker_list:
        get_fii_main_indicators(ticker)
        get_fii_dividends_series(ticker)