# Data Mining Projects - Fundos Imobiliários
## Renan Del Buono Brotto
### email: renanbrotto@gmail.com
### LinkedIn Profile: https://www.linkedin.com/in/renan-del-buono-brotto/

Neste projeto, coletaremos dados de diferentes Fundos de Investimento Imobiliário (FII) para, posteriormente, realizarmos análises de interesse dos investidores.

Primeiramente, vamos coletar informações básicas dos fundos, tais como "Razão Social", "Ticker", "CNPJ" e "Patrimônio Líquido". Em seguida, coletaremos o histórico de pagamento de dividendos dos FIIs de interesse.

## Descrição dos Módulos implementados:

1. `webdata.py`: contém a função `get_fii_webpage(ticker)` que recebe o código de negociação de um FII (chamado de ticker), BTLG11, por exemplo, e consulta o site www.fiis.com.br para obter a página web associada ao FII de interesse. A função, então, faz o download da página web, armazenando-a, localmente, como um arquivo .html no diretório 'local_files'.

2. `webscraping.py`: contém as funções `get_fii_dividends_series` e `get_fii_main_indicators`. A primeira delas, recebe o ticker do FII, consulta o arquivo HTML associado, e extrai, usando a biblioteca [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/), os pagamentos mensais de dividendos feitos pelo FII; o resultado é, então, armazenado em um arquivo .csv no diretório 'dividends_history'. 

    Já a segunda, também recebe o ticker do FII, e extrai os principais indicadores, armazendando-os em um arquivo.txt no diretório 'fii_indicators'.