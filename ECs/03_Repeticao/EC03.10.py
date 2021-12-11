'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

'''
def main():
    numero_linha = int(input())
    
    contador = 1
    
    for i in range(numero_linha-1, -1, -1):
        print("-" * i, end = "")
        print("1" * contador, end="")
        print("-" * i)
        contador = contador + 2
    
main()