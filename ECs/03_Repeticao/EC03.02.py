'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

'''
def main():
    total_numeros = int(input())
    
    soma = 0
    minimo = 0
    maximo = 0
    
    
    for i in range(1, total_numeros+1):
        numero = int(input())
        soma = soma + numero
        if (i == 1):
            maximo = numero
            minimo = numero
        elif (numero > maximo):
            maximo = numero
        elif (numero < minimo):
            minimo = numero
            
    print(soma)
    print("%.2f" %(soma/total_numeros))
    print(minimo)
    print(maximo)
        
    
main()