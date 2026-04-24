# #Exercício 6: Escreva um programa que
# determina o preço de um veículo a partir da
# FIPE API. O veículo pode ser informado pelo
#import requests

import requests

BASE_URL = "https://parallelum.com.br/fipe/api/v1/carros"

def buscar_marca_id(nome_marca):
    response = requests.get(f"{BASE_URL}/marcas")
    marcas = response.json()
    
    for marca in marcas:
        if nome_marca.lower() in marca['nome'].lower():
            return marca['codigo']
    
    return None

def buscar_modelo_id(marca_id, nome_modelo):
    response = requests.get(f"{BASE_URL}/marcas/{marca_id}/modelos")
    modelos = response.json()['modelos']
    
    for modelo in modelos:
        if nome_modelo.lower() in modelo['nome'].lower():
            return modelo['codigo']
    
    return None

def buscar_ano_id(marca_id, modelo_id, ano_digitado):
    response = requests.get(f"{BASE_URL}/marcas/{marca_id}/modelos/{modelo_id}/anos")
    anos = response.json()
    
    for ano in anos:
        if ano_digitado in ano['nome']:
            return ano['codigo']
    
    return None

def buscar_preco(marca_id, modelo_id, ano_id):
    url = f"{BASE_URL}/marcas/{marca_id}/modelos/{modelo_id}/anos/{ano_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()['Valor']
    return "Erro ao buscar preço"



marca = input("Digite a marca: ")
modelo = input("Digite o modelo: ")
ano = input("Digite o ano: ")

marca_id = buscar_marca_id(marca)

if not marca_id:
    print("Marca não encontrada")
else:
    modelo_id = buscar_modelo_id(marca_id, modelo)
    
    if not modelo_id:
        print("Modelo não encontrado")
    else:
        ano_id = buscar_ano_id(marca_id, modelo_id, ano)
        
        if not ano_id:
            print("Ano não encontrado")
        else:
            preco = buscar_preco(marca_id, modelo_id, ano_id)
            print(f" Preço FIPE: {preco}")