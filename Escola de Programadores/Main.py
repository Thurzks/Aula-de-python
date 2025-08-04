from MediaAlu import MediaAlu
def main():
    nome = input("Digite o nome da escola: ")

    

    quantSalas = 0
    while quantSalas <= 0:
        quantSalas = int(input(" "))
        if quantSalas <= 0: 
            print("Numero inválido")
    
    mediaEscola = [0.0] * quantSalas
    nomeSalas = [""] * quantSalas

    i = 0

    while i < quantSalas:
      quantAlu = (input("Qual a quantidade de alunos: "))
      print(nomeSalas)

      mediaEscola[i] = MediaAlu(quantSalas)



    







