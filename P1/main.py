#2. Ler nome e exibir saudação:
nome = input('Digite seu nome: ') 
print(f'Olá, {nome}')

#3. Maior valor da lista:
lista = [1,5,3,9,2] 
print(max(lista))

#5. Menu com opções: somar, subtrair, sair:
while True: 
    op = input('1-somar 2-subtrair 0-sair: ') 
    if op=='0': 
        break

#7. Média de 3 notas e status (Aprovado/Recuperação/Reprovado)

n1 = float(input('Digite a primeira nota de 0.0 a 10.0: '))
n2 = float(input('Digite a segunda nota de 0.0 a 10.0: '))
n3 = float(input('Digite a terceira nota de 0.0 a 10.0: '))
m = (n1+n2+n3)/3 
if m>=7: print('Aprovado')
elif m>=5: print('Recuperação')
else: print('Reprovado')


#8.  Verificar se número é par ou ímpar:
n=int(input('Digite um número inteiro: ')) 
print('Par' if n%2==0 else 'Ímpar')

#9. Contar vogais em uma string:
s=input('Digite uma string: ') 
vogais='aeiou' 
print(sum(1 for c in s if c in vogais))

#10. Contar 1 a 10 com for:
for i in range(1,11): print(i)

#11.Função calcular Fatorial:
def fatorial(n):
    if n==0:
        return 1
    else:
        return n*fatorial(n-1)
n=int(input('Digite um número inteiro para calcular o fatorial: '))
print(f'O fatorial de {n} é {fatorial(n)}')

#14. Ler dois números e mostrar soma
a=int(input('Digite o primeiro número: '))
b=int(input('Digite o segundo número: '))
print(f'A soma de {a} e {b} é {a+b}')