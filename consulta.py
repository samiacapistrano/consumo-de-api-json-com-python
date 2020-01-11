import requests
import json
import pandas
import csv

url = "http://data.fixer.io/api/latest?access_key=00a97e60ba205803ad30851f49943517"
print("Acessando base de dados do Fixo.io..")
resposta = requests.get(url)
print(resposta)
if resposta.status_code==200: 
    print("Acesso realizado com sucesso")
    print("Buscando informações....")
    dados = resposta.json()
    dolar_real_a = round(dados['rates']['BRL']/dados['rates']['USD'])
    bitcoin_real_a = round(dados['rates']['BRL']/dados['rates']['BTC'])
    euro_real_a = round(dados['rates']['BRL'] / dados['rates']['EUR'])
    real_a = 1

    dolar_real = dados['rates']['BRL']/dados['rates']['USD']
    bitcoin_real = dados['rates']['BRL']/dados['rates']['BTC']
    euro_real = dados['rates']['BRL'] / dados['rates']['EUR']
    real = 1
        
    print("Dolar:",dolar_real ," - ",dolar_real_a)
    print("Bitcoin",bitcoin_real," - ", bitcoin_real_a)
    print("Euro",euro_real," - ", euro_real_a)
    print("Real",real, "- ", real_a)

    tela = pandas.DataFrame({'Moedas':['Dolar','Euro','Bitcoin'],'Valores':[dolar_real,euro_real,bitcoin_real]})
    tela.to_csv('valores.csv',index=False,sep=";",decimal=",")
    
    '''print("Dolar: ",dados['rates']['USD'])
    print("Euro: ",dados['rates']['EUR'])
    print("Bitcoin: ",dados['rates']['BTC'])
    print("Real: ",dados['rates']['BRL'])
    print("Dolar para o real ", dados['rates']['BRL']/dados['rates']['USD'])'''   
    #print(dados)
else:
    print("Erro na base de dados")