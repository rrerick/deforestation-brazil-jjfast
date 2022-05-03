from logging import exception
from multiprocessing import log_to_stderr
import requests
import urllib.request
from urllib.request import urlopen
import re
import os
from bs4 import BeautifulSoup



#################################### FUNÇÕES UTEIS #####################################3

def arruma_longitude(log, log_final):
    #função que vai pegar uma lista e arrumar para ter 3 algorismos]
    x=log_final
    z=log
    
    log_total=list(range(z,x+1))
    
    return log_total
################################### FIM ################################################



#Pega os Dados - LATITUDE, no formato 00 e Longitude, no formato 000

lat=str(input("Latitude[00]:"))


#Vendo quais longitudes existem

visualizar_url=requests.get('https://www.eorc.jaxa.jp/jjfast/data_private/shape/S'+lat)
para_o_soup=visualizar_url.text

#Intervalo de Longitude
visualizar=BeautifulSoup(para_o_soup,'html.parser')
visualizar.prettify()

#melhorar a visualização
for link in visualizar.find_all('a'):
    print(link.get('href'))

log=int(input("longitude Inicial [000]: "))
log_final=int(input("Longitude Final [000]: "))
log_total= arruma_longitude(log, log_final)
print(log_total)

#pegando os HREF da pagina
try:
    lista=[]
    for elemento in log_total:
        file_url='https://www.eorc.jaxa.jp/jjfast/data_private/shape/S'+lat+'/W0'+str(elemento)+'/'
        print(file_url)
        file=requests.get(file_url)
        file1=file.text
        
        #procurar elementos dentro de pagina

        soup=BeautifulSoup(file1,'html.parser')
        soup.prettify()
        
        
        #percorrer e buscar os links
        
        for link in soup.find_all('a'):
            #colocando todos os links numa lista
            lista.append(link.get('href'))
            print("Links Adicionados com Sucesso\n")

except exception as e:
    print(e, "A falha foi quando estava pegando os HREF")

"""
#procurar elementos dentro de pagina

soup=BeautifulSoup(file1,'html.parser')
soup.prettify()


#corpo do aqruivo
corpo=soup.string


#percorrer e buscar os links
lista=[]
for link in soup.find_all('a'):
    #colocando todos os links numa lista
    lista.append(link.get('href'))
print("Links Adicionados com Sucesso\n")
"""
#criando uma pasta
try:

    path='/home/erick_rocha/Downloads/dados_Desmatamento/'
    try:
              
        diretorio_mae=path+'S'+str(lat)+'/'
        os.mkdir(diretorio_mae)
        print("Pasta Latitude Criada com Sucesso")
        
    except FileExistsError as E:
        diretorio_mae=path+'S'+str(lat)+'/'
        
    
    diretorio=diretorio_mae+str(log_final)+'/'
    os.mkdir(diretorio)    
    print("Pasta Longitude Criada com Sucesso")
    
except FileExistsError as E:
    diretorio=diretorio_mae+str(log)+'/'
    
finally:
    #pegar os links da lista que tenham o 21 ou 22, que no caso é o ano. 
    try:
        
        for id in range(len(lista)+1):
            if id == 0:
                continue
            
            try:
                for algoritimo in log_total:  
                    
                    #caminho da url e caminho da pasta
                    file_url='https://www.eorc.jaxa.jp/jjfast/data_private/shape/S'+lat+'/W0'+str(algoritimo)+'/'
                    print(file_url)
                    print(lista[id])
            
                    #teste_arquivo=lista[id].split('_')
        
          
                    arquivo=''
                    arquivo=lista[id]
        
                while not str(algoritimo) in lista[id]:
                    if arquivo.find('_21')>0:
                        #arquivo+=lista[id]

            
                        #cria o caminho do arquivo e o nome do aruqivo final
            
                        url=file_url+arquivo
                        nome=diretorio+'longitude'+str(id)+'.zip'
            
                 
                        #hora de baixar o arquivo e colocar no diretorio
                
                        urllib.request.urlretrieve(url,nome)

                        print("OK!,Arquivo na Pasta\n")
                    elif arquivo.find('_22')>0:

            
                   
            
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
    except Exception as e:
        print(e)

        
