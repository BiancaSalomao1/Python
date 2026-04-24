

#Faça um programa que peça o nome do usuário e imprima uma mensagem de boas-vindas.

nome = input("Digite seu nome: ")
print(f"Bem-vindo(a), {nome}!")

#Solicite dois números e mostre a soma deles.

n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
print(f"Soma: {n1 + n2}")

#Peça a idade do usuário e diga se ele é maior ou menor de idade.

idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

#Leia um número e informe se ele é par ou ímpar.

num = int(input("Digite um número: "))
if num % 2 == 0:
    print("Par")
else:
    print("Ímpar")

#Peça um valor em reais e converta para dólares (1 USD = 5.00 BRL).

reais = float(input("Valor em R$: "))
print(f"Valor em US$: {reais / 5.0:.2f}")

#Peça a nota de um aluno e informe a situação.

nota = float(input("Nota: "))
if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

#Leia três números e mostre o maior.

a = int(input("N1: "))
b = int(input("N2: "))
c = int(input("N3: "))
print(f"O maior é: {max(a, b, c)}")

#Peça um número e verifique se é positivo, negativo ou zero.

n = float(input("Número: "))
if n > 0:
    print("Positivo")
elif n < 0:
    print("Negativo")
else:
    print("Zero")


salario = float(input("Salário: "))
print(f"Novo salário (10% aumento): {salario * 1.10:.2f}")

#Peça o sexo (M/F) e mostre mensagem.

sexo = input("Sexo (M/F): ").upper()
if sexo == 'M':
    print("Masculino")
elif sexo == 'F':
    print("Feminino")
else:
    print("Inválido")

#Mostre os números de 1 a 10.

for i in range(1, 11):
    print(i)

#Mostre os números pares de 1 a 20.

for i in range(2, 21, 2):
    print(i)

#Mostre a tabuada de um número.

num = int(input("Tabuada de: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#Some números até digitar 0.


soma = 0
while True:
    n = int(input("Número (0 para sair): "))
    if n == 0: break
    soma += n
    print(f"Total: {soma}")

#Conte números pares até digitar 0.

pares = 0
while True:
    n = int(input("Número (0 para sair): "))
    if n == 0: break
    if n % 2 == 0: pares += 1
    print(f"Qtd de pares: {pares}")

#Jogo de adivinhação.

import random
segredo = random.randint(1, 10)
chute = 0
while chute != segredo:
    chute = int(input("Chute (1-10): "))
    if chute < segredo: print("Maior!")
    elif chute > segredo: print("Menor!")
    print("Acertou!")

#Calculadora simples.

n1 = float(input("N1: "))
op = input("Op (+,-,,/): ")
n2 = float(input("N2: "))
if op == '+': print(n1 + n2)
elif op == '-': print(n1 - n2)
elif op == '': print(n1 * n2)
elif op == '/' and n2 != 0: print(n1 / n2)

#Verificador de senha.

senha = ""
while senha != "1234":
    senha = input("Senha: ")
    print("Acesso liberado")

#Média de notas até -1.

soma = qtd = 0
while True:
    nota = float(input("Nota (-1 para sair): "))
    if nota == -1: break
    soma += nota
    qtd += 1
    print(f"Média: {soma/qtd:.2f}" if qtd > 0 else "Sem notas")

#Contador regressivo.

import time
for i in range(10, -1, -1):
    print(i)
time.sleep(1)
print("Fim!")