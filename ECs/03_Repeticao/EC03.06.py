'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

'''
def main():
   numero = int(input())
   
   somatorio = 0
   
   for i in range(1, numero + 1):
       for j in range (1, 9):
           somatorio = somatorio + ((i + 1) * j)
           
   print(somatorio)
    
    
main()