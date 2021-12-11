'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

Objetivos do programa: Calcular a distância entre dois pontos 

Dados de entrada: Coordenadas do ponto x e do ponto y.
Dados de saída: Distância entre os pontos x e y.
'''

def calculaDistancia(ponto1_x, ponto1_y, ponto2_x, ponto2_y):
    distancia = ((((ponto2_x - ponto1_x)**2) + ((ponto2_y - ponto1_y)**2))**(1/2))
    print("%.2f" %(distancia))


ponto1_x = float(input("Digite a coordenada x do ponto 1: "))
ponto1_y = float(input("Digite a coordenada y do ponto 1: "))
ponto2_x = float(input("Digite a coordenada x do ponto 2: "))
ponto2_y = float(input("Digite a coordenada y do ponto 2: "))
calculaDistancia(ponto1_x, ponto1_y, ponto2_x, ponto2_y)