
from adição import adição
from divisão import divisão
from subtração import subtração
from multiplicação import multiplicação
def main():
    numero1 = int (input("Numero 1 "))
    numero2 = int (input("Numero 2 "))
    
    resultado = 0


    

    operação = input("Operação: ")

    if operação == "+": 
        resultado = adição(numero1, numero2)
    
    elif operação == "-":
        resultado = subtração(numero1, numero2)

    elif operação == "*":
     resultado = multiplicação(numero1, numero2)

    elif operação == "/":
     resultado = divisão(numero1, numero2)


    print(resultado)



    return 0 
main()
