'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

'''

def main():
    pontox = int(input("Digite a coordenada x do ponto: "))
    pontoy = int(input("Digite a coordenada y do ponto: "))
    
    if (((pontox > -800) and (pontox < 22)) and ((pontoy > -20) and (pontoy < 35))):
        print("SIM")
    else:
        print("NAO")
    
    
main()
