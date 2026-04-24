
def century_from_year(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1
    
def main():
    year = int(input("Digite um ano: "))
    century = century_from_year(year)
    print(f"O século do ano {year} é: {century}")

main()
