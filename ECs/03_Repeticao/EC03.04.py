'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

'''
def main():
    numero = int(input())
    
    for i in range(1, numero+1):
        for j in range(1, i+1):
            print(i, end="")
        print(end = "\n")    
        
main()