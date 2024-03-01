import csv

# Abre o arquivo CSV em modo de adição
with open("phonebook.csv", "a", newline="") as file:
    # Pede ao usuário para fornecer o nome e o número
    name = input("Nome: ")
    number = input("Número: ")

    # Cria um escritor CSV
    writer = csv.writer(file)

    # Escreve a linha no arquivo CSV
    writer.writerow([name, number])

print("Entrada adicionada ao arquivo phonebook.csv.")
