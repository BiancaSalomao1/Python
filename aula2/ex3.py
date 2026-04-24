def calcular_tabuada(numero):
    tabuada = []
    for i in range(1, 11):
        resultado = numero * i
        tabuada.append(f"{numero} x {i} = {resultado}")
    return tabuada

def main():
    numero = int(input("Digite um número para calcular a tabuada: "))
    tabuada = calcular_tabuada(numero)
    
    print(f"Tabuada do {numero}:")
    for linha in tabuada:
        print(linha)

main()
