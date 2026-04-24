"""teste aula  """
str= "Joao da Silva "
for c in str:
    print(c, end=" ")


"""Exercicio 1:
Crie uma aplicação que receba o valor da base e
da altura de um triângulo retângulo e apresente
na tela sua área."""
def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))
area = calcular_area_triangulo(base, altura)
print(f"A área do triângulo retângulo é: {area}")               

"""
Exercicio 2: Crie um programa para calcular e exibir na tela o
peso ideal. IMC = (peso / (altura^2))
"""
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc                  
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))
imc = calcular_imc(peso, altura)
print(f"O seu IMC é: {imc:.2f}")    

"""
Exercicio 3 : Uma farmácia precisa ajustar os preços de seus
produtos em 12%. Elabore uma aplicação que
receba o valor do produto e aplique o percentual
de acréscimo.
– O novo valor a ser calculado deve ser
arredondado e apresentado com duas casas
decimais. 
"""
def ajustar_preco(preco):
    novo_preco = preco * 1.12
    return round(novo_preco, 2)
preco = float(input("Digite o valor do produto: "))                     
novo_preco = ajustar_preco(preco)
print(f"O novo valor do produto com o acréscimo de 12% é:R$ {novo_preco:.2f}")

