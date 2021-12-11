'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

'''
def main():
    numero = 1
    
    multiplo3 = 0
    multiplo5 = 0
    
    while (numero != 0):
        if (numero % 3 == 0):
            multiplo3 = multiplo3 + 1
        if (numero % 5 == 0):
            multiplo5 = multiplo5 + 1
        numero = int(input())
 
            
    print(multiplo3)
    print(multiplo5)
    
    
main()