'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

'''

def calculaDistancia(ponto1x, ponto1y, ponto2x, ponto2y):
    distancia = ((((ponto2x - ponto1x)**2) + ((ponto2y - ponto1y)**2))**(1/2))
    return (distancia)

def main():
    carga = float(input())
    ponto1x = float(input()) 
    ponto1y = float(input())    
    ponto2x = float(input())  
    ponto2y = float(input())    
    
    distancia = calculaDistancia(ponto1x, ponto1y, ponto2x, ponto2y)
    
    print("%.2f" % (distancia))
    
    if (carga <= 50000):
        if (distancia <= 18000):
            print("SIM")
        elif(distancia <= (18000 * 1.10)):
            print("TALVEZ")
        else:
            print("NAO")
            
    if ((carga >= 50001) and (carga <= 200000)):
        if (distancia <= 9000):
            print("SIM")
        elif(distancia <= (9000 * 1.10)):
            print("TALVEZ")
        else:
            print("NAO")
            
    if ((carga >= 200001) and (carga <= 250000)):
        if (distancia <= 3000):
            print("SIM")
        elif(distancia <= (3000 * 1.10)):
            print("TALVEZ")
        else:
            print("NAO")
    

main()