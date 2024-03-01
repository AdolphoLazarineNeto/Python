while True:
    s = input("Isso fará o computador digitar a tabuada do 2 para sempre, quer continuar? (Y/N): ")
    if s.lower() == "y":
        i = 1
        while True:
            print(i)
            i *= 2
    elif s.lower() == "n":
        break
    else:
        print("Opção inválida. Por favor, insira 'Y' para continuar ou 'N' para sair.")
