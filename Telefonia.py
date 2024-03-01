### BANCO DE DADOS BASICO, POE NOME E NUMERO EM PEOPLE ###
### E TODA VEZ QUE RODAS

people = {
    "Adolpho Neto": "+55 14 996759177",
    "Leandro Lima": "+55 14 998792481"
}

name = input("Nome: ")
if name in people:
   print(f"Numero: {people[name]}")
else:
   print("Pessoa não encontrada...")
