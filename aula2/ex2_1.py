def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc
def main():
    while True:
        try:
            peso = float(input("Digite o peso (kg): "))
            altura = float(input("Digite a altura (m): "))
            if peso <= 0 or altura <= 0:
                raise ValueError("Peso e altura devem ser maiores que zero.")
            imc = calcular_imc(peso, altura)
            print(f"O IMC é: {imc:.2f}")
        except ValueError as e:
            print(f"Erro: {e}")
        
        continuar = input("Deseja continuar? (s/n): ").strip().lower()
        if continuar != 's':
            break
main()
