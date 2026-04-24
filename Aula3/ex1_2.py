'''Faça um programa que leia um vetor de 15 posicoes 
de numeros inteiros e divida todos os seus elementos
 pelo maior valor do vetor. mostre o vetor apos os 
 calculos.'''

def divideMaiorDosInteiros(inteiros):
    maior = max(inteiros)
    for i in range(len(inteiros)):
        inteiros[i] /= maior
    return inteiros
inteiros = []
for i in range(15):
    inteiro = int(input(f"Digite o {i+1}º número inteiro: "))
    inteiros.append(inteiro)
resultado = divideMaiorDosInteiros(inteiros)
print("Vetor após os cálculos:")
print(resultado)

    