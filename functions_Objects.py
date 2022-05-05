"""
    FUNÇÕES E OBJETO EM USO NO PROGRAMA 'BUSCA_DADOS.PY'
    VERSAO2- maior organização 




"""
class Longitude(object):
    """
        Objeto para as longitudes, ficando mais facil pegar varias longitudes dentro de uma longitude
        dessa forma iremos tambem diminuir nossas linhas for 
        
    """
    def __init__(self,lat_inicio, lat_fim):
        self.lat_fim=lat_fim
        self.lat_inicio=lat_inicio
        
    def __iter__(self):            
        if self.lat_inicio < self.lat_fim:
            
            for i in range(self.lat_inicio,self.lat_fim+1):
                yield i
        
        else:
            
            raise StopIteration


class BaixaArquivo(object):
    """
    Criei esse objeto para ele ser responsavel em baixar e organizar os arquivos na pasta
    
        uma função de criar a pasta do arquivo 
        uma função para baixar o arquivo e colocar na pasta correspondente
        
    arg:
        url- link para baixar o arquivo
        nome- caminho para salvar o arquivo
        
    """
    def __init__(self, url,nome):
        self.url=url
        self.nome=nome
    def CriaPasta(self, longitude):
        """
        Criar a pasta de acordo com o link(longitude) do documento 
        
        arg:
            longitude - função Longitude
        
        """
        import os
        
        try:
            
            path=str(input("Digite o nome do caminho: "))
            diretorio_mae=(path+'S'+str(lat)+'/')
            os.mkdir(diretorio_mae)
            
            #criando a sub-pasta:
            for pasta in longitude:
                diretorio=diretorio_mae+str(pasta)+'/'
                os.mkdir(diretorio)  
            
        except FileExistsError as er:
            diretorio=diretorio_mae+str(log_final)+'/'
            
        return BaixaArquivo(self, diretorio)
    
    def BaixaArquivo(self, diretorio):
        """
        Baixa o arquivo e coloca na pasta correspondente 
        
        ARG:
            Vai receber os caminhos existentes, para baixar e colocar nas pastas
        
        """
class ulr(object):
    """
    Responsavel por cuidar de todo e qualquer ulr
    requisitar
    e organizar para o download
    
    
    """
    
            




            
            

