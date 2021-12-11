'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

'''

def invertendo(numero: int):
    while (numero >= 1):
        print(numero%10)
        numero = numero // 10
        
def main():
    numero = int(input())
    
    invertendo(numero)
    
main()
    