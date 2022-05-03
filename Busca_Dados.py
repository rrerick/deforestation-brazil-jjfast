from logging import exception
import requests
import urllib.request
from urllib.request import urlopen
import re
import os
from bs4 import BeautifulSoup

#Pega os Dados - LATITUDE, no formato 00 e Longitude, no formato 000
#log=str(input("longitude[000]: "))
lat=str(input("Latitude[00]:"))
#Vendo quais longitudes existem

visualizar_url=requests.get('https://www.eorc.jaxa.jp/jjfast/data_private/shape/S'+lat)
para_o_soup=visualizar_url.text
visualizar=BeautifulSoup(para_o_soup,'html.parser')
visualizar.prettify()
#melhorar a visualização
for link in visualizar.find_all('a'):
    print(link.get('href'))

log=str(input("longitude[000]: "))

#pegando os HREF da pagina
file_url='https://www.eorc.jaxa.jp/jjfast/data_private/shape/S'+lat+'/W'+log+'/'
file=requests.get(file_url)
file1=file.text
#pagina=file.read()

#procurar elementos dentro de pagina
soup=BeautifulSoup(file1,'html.parser')
soup.prettify()
#print(soup)

#corpo do aqruivo
corpo=soup.string

#percorrer e buscar os links
lista=[]
for link in soup.find_all('a'):
    #colocando todos os links numa lista
    lista.append(link.get('href'))
print("Links Adicionados com Sucesso\n")
#criando uma pasta
try:

    path='/home/erick_rodrigues/Downloads/dados_Desmatamento/'
    try:
        diretorio_mae=path+'S'+str(lat)+'/'
        os.mkdir(diretorio_mae)
        print("Pasta Latitude Criada com Sucesso")
    except FileExistsError as E:
        diretorio_mae=path+'S'+str(lat)+'/'

    diretorio=diretorio_mae+str(log)+'/'
    os.mkdir(diretorio)
    print("Pasta Longitude Criada com Sucesso")
except FileExistsError as E:
    diretorio=diretorio_mae+str(log)+'/'
finally:
    #pegar os links da lista que tenham o 21 ou 22
    for id in range(len(lista)+1):
        if id == 0:
            continue
        try:
            x=0
            #caminho da url e caminho da pasta
            file_url='https://www.eorc.jaxa.jp/jjfast/data_private/shape/S'+lat+'/W'+log+'/'
            print(lista[id])
            
            #teste_arquivo=lista[id].split('_')
        
          
            arquivo=''
            arquivo=lista[id]
            #print("hey")
            
            if arquivo.find('_21')>0:
                #arquivo+=lista[id]

            
                #cria o caminho do arquivo e o nome do aruqivo final
            
                url=file_url+arquivo
                nome=diretorio+'longitude'+str(id)+'.zip'
            
                 
                #hora de baixar o arquivo e colocar no diretorio
                
                urllib.request.urlretrieve(url,nome)

                print("Parabens,Arquivo na Pasta\n")
            elif arquivo.find('_22')>0:

            
                #arquivo+=lista[id]
            
                #cria o caminho do arquivo e o nome do aruqivo final
            
                url=file_url+arquivo
                nome=diretorio+'longitude'+str(id)+'.zip'
            
                 
                #hora de baixar o arquivo e colocar no diretorio
                print(arquivo)
                urllib.request.urlretrieve(url,nome)
                print("Parabens,Arquivo na Pasta")
            

            else:
                print("Fora da Data, indo para o proximo\n")
                continue
        except Exception as e:
            print(e)
            continue    