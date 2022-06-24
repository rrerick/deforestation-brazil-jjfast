"""
FINALIDADE: Pegar e baixar os dados shapefile de desmatamento no site https://www.eorc.jaxa.jp/jjfast/jj_mapmonitor_phase1.html
e colocar organizados em pasta dentro da pasta local do usuario



Este arquivo esta sendo modificado!!!!!!

"""








#  IMPORTAÇÕES

from logging import exception
from multiprocessing import log_to_stderr
from urllib.error import URLError
import requests
import urllib.request
from urllib.request import urlopen
import re
import os
from bs4 import BeautifulSoup
import functions_Objects  #arquivo de funçoes e objetos que deve funcionar aqui 





def main():
    lat=str(input("Latitude[00]:")) #formato 00


#Vendo quais longitudes existem e separando:

visualizar_url=requests.get('https://www.eorc.jaxa.jp/jjfast/data_private/shape/S'+lat)
para_o_soup=visualizar_url.text


visualizar=BeautifulSoup(para_o_soup,'html.parser')
visualizar.prettify()

#pegandos os links que existem e printando para saber quais longitutes existem nessa latitude:

#for link in visualizar.find_all('a'):
    #print(link.get('href'))

#pegando as longitudes e iterando:

log=int(input("longitude Inicial [000]: "))
log_final=int(input("Longitude Final [000]: "))

log_total= functions_Objects.Longitude(log, log_final)


#pegando os links de dowload da pagina, colocando numa lista para poder usar depois:

try:
    lista=[] # vamos usar na hora de baixar
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
#criando uma pasta mae e outra menor, caso exista ele vai continuar
try:
    #local para a criação da pasta 
    cria_path=str(input("Digite a pasta destino: "))
    path=cria_path
    print(path)
    
    try:
              
        diretorio_mae=path+'S'+str(lat)+'/'
        os.mkdir(diretorio_mae)
        print("Pasta Latitude Criada com Sucesso")
        
    except FileExistsError as E:
        diretorio_mae=path+'S'+str(lat)+'/'
        
    #criando a sub-pasta:
    
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
                    print(lista[id])        
                                                            
                    arquivo=lista[id] #esse arquivo é o endereço para o download
                    
                    if str(algoritimo) in file_url:
                        if arquivo.find('_21')>0: #se o arquivo  começar ou terminar em 2021                  
                            #cria o caminho do arquivo e o nome do arquivo final
            
                            url=file_url+arquivo
                            nome=diretorio+'longitude'+str(id)+'.zip'
            
                 
                            #hora de baixar o arquivo e colocar no diretorio 'nome'
                
                            urllib.request.urlretrieve(url,nome)
                            print("OK!,Arquivo na Pasta\n")
                            
                        elif arquivo.find('_22')>0: #se o arquivo começar ou terminar em 2022    
                        
                            #cria o caminho do arquivo e o nome do aruqivo final
            
                            url=file_url+arquivo
                            nome=diretorio+'longitude'+str(id)+'.zip'
            
                 
                            #hora de baixar o arquivo e colocar no diretorio
                            urllib.request.urlretrieve(url,nome)
                            print("Parabens,Arquivo na Pasta")
            

                        else:
                            print("Fora da Data, indo para o proximo\n")
                            continue
                    else:
                        continue
            except URLError as e:
                print(e)                
                continue    
        
    except Exception as e:
                print(e)

        
