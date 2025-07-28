def main():
    nome = input("Digite o seu nome")
    idade = int ( input("Digite a sua idade"))
    altura = float ( input("Digite a sua altura"))
    isMasculino = input ("Você é homem (H) ou mulher (M)?")
    print("0 ", nome, "tem ", idade, " de idade,", altura ," de altura")
    if isMasculino == "H" or isMasculino == "h":
     print("Ele é um homem")
    else:
       print("É uma mulher")
    return 0
main()