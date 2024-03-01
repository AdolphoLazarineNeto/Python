def main():
    i = get_positive_int()
    print("Número inserido:", i)

def get_positive_int():
    while True:
        try: # Chamado para quando nao digitar valor mesmo assim o codigo continuará
            n = int(input("Por favor, insira um número inteiro positivo: "))
            if n > 0:
                break
            else:
                print("O número deve ser positivo. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

    return n

main()
