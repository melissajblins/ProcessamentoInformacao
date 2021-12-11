def calcula_positivos(numero: int, positivos: int):
    if (numero > 0):
        positivos = positivos + 1
        
    return positivos

def main():
    positivos = 0 
    numero = int(input())
    positivos = calcula_positivos(numero, positivos)
    numero = int(input())
    positivos = calcula_positivos(numero, positivos)
    numero = int(input())
    positivos = calcula_positivos(numero, positivos)
    numero = int(input())
    positivos = calcula_positivos(numero, positivos)
    numero = int(input())
    positivos = calcula_positivos(numero, positivos)
    numero = int(input())
    positivos = calcula_positivos(numero, positivos)
    numero = int(input())
    positivos = calcula_positivos(numero, positivos)
    
    print(positivos)


main()