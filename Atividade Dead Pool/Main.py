def main():
    nome = input("Digite o seu nome")
    idade = int ( input("Digite a sua idade"))
    print("0 ", nome, "tem", idade, "de idade,")

    if idade >= 18:
        print("Entrada liberada")
    elif idade >= 16:
        acompanhante = input ("Você está acompanhado?")  
        if acompanhante == "S":  
            print("Entrada liberada")    
        else:
            print("Entrada proibida")
    else:
        print("Entrada proibida")
    return 0
main()