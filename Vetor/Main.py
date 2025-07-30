import random
def main():
    tamanho = int(input(""))
    vetor = [0.0] * tamanho

    i = 0
    media /= 4
    while i < tamanho:
        vetor[i] = float(random.uniform(0.0, 10.0))

        i +=1

    print(vetor)

    return 0
main()