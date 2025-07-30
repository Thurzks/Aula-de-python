import random
def main():
    numeroAle = random.randint(0, 1000)

    i = 0

    numero = -1

    while numero != numeroAle:
        numero = int (input("Digite um numero"))

        if numero < numeroAle:
            print("O número aleatório é maior")
        elif numero > numeroAle:
            print("O número aleatório é menor")

        i += 1
    print("Você acertou com", i,"tentativas")
    return 0
main()