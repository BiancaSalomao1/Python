# #Exercício 1: Escreva um programa em Python
# # capaz de ler as primeiras n linhas de um
# # arquivo texto. O número de linhas é
# # informado pelo usuário

file_path = "file.txt"

def read_first_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        for _ in range(n):
            line = file.readline()
            if not line:
                break
            print(line.strip()) 
n = int(input("Número de linhas a ler: "))
read_first_n_lines(file_path, n)    


# #Exercício 2: Escreva um programa que realiza
# a leitura um arquivo e armazena o conteúdo
# em uma lista.
def read_file_to_list(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()
file_content = read_file_to_list(file_path)

list_content = [line.strip() for line in file_content]
print(list_content)


# #Exercício 3: Escreva um programa capaz de
# contar a frequência de palavras em um
# arquivo
def count_word_frequencies(file_path):
    word_freq = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq
frequencies = count_word_frequencies(file_path)
print(frequencies)



# #Exercício 4: Escreva um programa capaz de
# copiar o conteúdo de um arquivo em outro
# arquivo.

def copy_file(source_path, destination_path):
    with open(source_path, 'r') as source_file:
        content = source_file.read()
    with open(destination_path, 'w') as dest_file:
        dest_file.write(content)
source_path = "file.txt"
destination_path = "copy.txt"
copy_file(source_path, destination_path)


# #Exercício 5: Escreva um programa em Python
# capaz de:
# – Carregar um arquivo no formato CSV em um Lista
# – Gravar o conteúdo da Lista em um arquivo JSON

import csv
import json

def create_sample_csv(file_path):
    sample_data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "Los Angeles"},
        {"name": "Charlie", "age": 35, "city": "Chicago"}
    ]
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["name", "age", "city"])
        writer.writeheader()
        writer.writerows(sample_data)

def csv_to_json(csv_file_path, json_file_path):
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        data_list = list(reader)
    with open(json_file_path, 'w') as json_file:
        json.dump(data_list, json_file, indent=4)
csv_file_path = "sample.csv"
json_file_path = "output.json"
create_sample_csv(csv_file_path)
csv_to_json(csv_file_path, json_file_path)
    



