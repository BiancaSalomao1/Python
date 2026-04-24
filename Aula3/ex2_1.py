'''Faça um programa capaz de gerar usernames e
senhas para alunos da FATEC de Ribeirão Preto.
– O programa recebe como entrada o nome completo
do aluno e produzir um username contendo:
• A primeira letra do nome e o sobrenome
– O resultado deve ser armazenado em um estrutura da
sua preferência: Tupla, Lista, Dicionário ou Conjunto.
– O programa deve garantir que não sejam gerados.
username duplicados
– As senhas provisórias deve conter no mínimo 8
caracteres (números, letras e símbolos) com máxima
segurança.'''

import random
import string

alunos = {}

'''
    .strip() -Remove espaços no início e no fim da string
    .split() -Divide a string em uma lista de palavras usando espaços como separadores
    Assim eu consigo remover os espaçoes extras e obter uma lista de itens, onde cada item é uma palavra do nome completo. 
    Depois eu puxo o item -1 para pegar o sobrenome, e o item 0 para pegar a primeira letra do primeiro nome.
'''

def gerar_username_base(nome_completo):
    partes_nome = nome_completo.strip().split()
    
    if len(partes_nome) < 2:
        raise ValueError("O nome completo deve conter pelo menos nome e sobrenome.")
    
    primeiro_nome = partes_nome[0]
    sobrenome = partes_nome[-1]
     
    return (primeiro_nome[0] + sobrenome).lower()


def gerar_username_unico(nome_completo, alunos):
    base = gerar_username_base(nome_completo)
    
    if base not in alunos:
        return base
    
    # tentar de 01 até 99 para obter um username único
    for i in range(1, 100):
        novo_username = f"{base}{i:02d}"
        
        if novo_username not in alunos:
            return novo_username
    
    raise Exception("Não foi possível gerar username único")


def gerar_senha_provisoria():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    senha = ''.join(random.choice(caracteres) for _ in range(10))
    return senha


while True:
    nome_completo = input("Digite o nome completo do aluno (ou 'sair' para encerrar): ")
    
    if nome_completo.lower() == 'sair':
        break

    try:
        username = gerar_username_unico(nome_completo, alunos)
        senha = gerar_senha_provisoria()
        
        alunos[username] = senha
        
        print(f"Username: {username}, Senha Provisória: {senha}")
    
    except ValueError as e:
        print(e)


print("\nDados dos alunos cadastrados:")
for username, senha in alunos.items():
    print(f"Username: {username}, Senha Provisória: {senha}")