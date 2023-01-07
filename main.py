import requests
import json
from pprint import pprint



def endereco_cep(cep: str):
    '''
    Somente deve ser informado o CEP. 
     Não há necessidade de se atentar se há hífen ou ponto, pois a função já trata isso.
    OBS: CEP deve ser str
    '''
    
    cep = cep.replace('-','').replace('.','')
    link_cep = f'https://viacep.com.br/ws/{cep}/json/'
    
    requisicao = requests.get(link_cep).json()
    
    return requisicao


def endereco(uf: str, cidade: str, rua: str):
    
    link = f'https://viacep.com.br/ws/{uf}/{cidade}/{rua}/json/'

    requisicao_endereco = requests.get(link).json()
    
    return requisicao_endereco



if __name__ =='__main__':
    pprint(endereco(uf='RJ',cidade='Niterói',rua='Aurelino Leal'))
    
    dados = endereco_cep('24020-110')

