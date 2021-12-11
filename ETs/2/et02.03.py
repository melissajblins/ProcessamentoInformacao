def fracao_mista(numerador: int, denominador: int) -> int:
    multiplicador = numerador // denominador
    resto = numerador % denominador
    
    return (multiplicador,resto)



def main():
    numerador = int(input())
    denominador = int(input())
    
    if (denominador == 0):
        print ("Não é uma fraçao válida")
    else:
        multiplicador, numerador = fracao_mista(numerador, denominador)
        if (multiplicador == 0):
            print("(%d / %d)" % ( numerador, denominador))
        else:
            print("%d * (%d / %d)" % (multiplicador, numerador, denominador))
    
    
main()