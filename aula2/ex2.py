def calcular_resistencia_equivalente(r1, r2, r3, r4):
    resistencia_equivalente = r1 + r2 + r3 + r4
    return resistencia_equivalente


def main():
    r1 = float(input("Digite o valor da resistência 1: "))
    r2 = float(input("Digite o valor da resistência 2: "))
    r3 = float(input("Digite o valor da resistência 3: "))
    r4 = float(input("Digite o valor da resistência 4: "))

    resistencia_equivalente = calcular_resistencia_equivalente(r1, r2, r3, r4)
    maior_resistencia = max(r1, r2, r3, r4)
    menor_resistencia = min(r1, r2, r3, r4)

    print(f"Resistência equivalente: {resistencia_equivalente:.2f} ohms")
    print(f"Maior resistência: {maior_resistencia:.2f} ohms")
    print(f"Menor resistência: {menor_resistencia:.2f} ohms")


main()  
