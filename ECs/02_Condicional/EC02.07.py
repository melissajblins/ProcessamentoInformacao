'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

'''

def main():
    A = int(input("Digite o primeiro número: "))
    B = int(input("Digite o segundo número: "))
    C = int(input("Digite o terceiro número: "))
    
    if (A > B):
        auxiliar = A
        A = B
        B = auxiliar
    if(B > C):
        auxiliar = B
        B = C
        C = auxiliar
    if (A > B):
        auxiliar = A
        A = B
        B = auxiliar
        
    print("%d %d %d" % (A, B, C))
    
main()
    