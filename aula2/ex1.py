def calcular_desconto(valor):
    if valor < 0:
        return "Valor inválido. O valor deve ser maior ou igual a zero."
    elif valor >= 50 and valor < 200:
        desconto = valor * 0.05
    elif valor >= 200 and valor < 500:
        desconto = valor * 0.06
    elif valor >= 500 and valor < 1000:
        desconto = valor * 0.07
    else:
        desconto = valor * 0.08

    novo_valor = valor - desconto
    return novo_valor       

def main():
    nome_produto = input("Digite o nome do produto: ")
    valor_produto = float(input("Digite o valor do produto: "))

    novo_valor = calcular_desconto(valor_produto)

    if isinstance(novo_valor, str):
        print(novo_valor)
    else:
        print(f"Produto: {nome_produto}")
        print(f"Valor original: R$ {valor_produto:.2f}")
        print(f"Valor com desconto: R$ {novo_valor:.2f}")

main()
