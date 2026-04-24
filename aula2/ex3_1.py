def calcular_pares_impares(numeros):
    pares = []
    impares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

def calcular_maior_menor(numeros):
    maior = max(numeros)
    menor = min(numeros)
    return maior, menor

def calcular_media(numeros):
    media = sum(numeros) / len(numeros)
    return media

def main():
    numeros = []
    while True:
        try:
            numero = int(input("Digite um número (ou 'sair' para finalizar): "))
            numeros.append(numero)
        except ValueError:
            break

    if numeros:
        pares, impares = calcular_pares_impares(numeros)
        maior, menor = calcular_maior_menor(numeros)
        media = calcular_media(numeros)

        print(f"Números pares: {pares}")
        print(f"Números ímpares: {impares}")
        print(f"Maior número: {maior}")
        print(f"Menor número: {menor}")
        print(f"Média dos números: {media:.2f}")
    else:
        print("Nenhum número foi digitado.")                

main()
