def descobrindo_maior(numero1: int, maiornumero: int, menornumero: int):
    if (numero1 > maiornumero):
        numero2 = maiornumero
        maiornumero = numero1
        if (numero2 > menornumero):
            menornumero = numero2
    elif (numero1 > menornumero and numero1 < maiornumero):
        menornumero = numero1
    return (maiornumero, menornumero)


def main():
    numero1 = int(input())
    numero2 = int(input())
    
    if (numero1 > numero2):
        maiornumero = numero1
        menornumero = numero2
    else:
        maiornumero = numero2
        menornumero = numero1
  
    
    numero1 = int(input())
    maiornumero, menornumero = descobrindo_maior(numero1, maiornumero, menornumero)
    
    numero1 = int(input())
    maiornumero, menornumero = descobrindo_maior(numero1, maiornumero, menornumero)
    
    numero1 = int(input())
    maiornumero, menornumero = descobrindo_maior(numero1, maiornumero, menornumero)
    
    numero1 = int(input())
    maiornumero, menornumero = descobrindo_maior(numero1, maiornumero, menornumero)
    
    numero1 = int(input())
    maiornumero, menornumero = descobrindo_maior(numero1, maiornumero, menornumero)
    
    numero1 = int(input())
    maiornumero, menornumero = descobrindo_maior(numero1, maiornumero, menornumero)
    
    numero1 = int(input())
    maiornumero, menornumero = descobrindo_maior(numero1, maiornumero, menornumero)
    
    numero1 = int(input())
    maiornumero, menornumero = descobrindo_maior(numero1, maiornumero, menornumero)
   

    print(menornumero)



main()