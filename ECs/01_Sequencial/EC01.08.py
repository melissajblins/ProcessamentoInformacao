'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

Objetivos do programa: Definir a melhor composição de caixas dentro de um caminhão.

Dados de entrada: Capacidade do caminhão.
Dados de saída: Valores das caixas. 
'''

capacidade = int(input("Digite a capacidade do caminhão: "))

caixas_500 = capacidade // 500
resto_500 = capacidade - (caixas_500 * 500)
caixas_100 = resto_500 // 100
resto_100 = resto_500 - (caixas_100 * 100)
caixas_25 = resto_100 // 25
resto_25 = resto_100 - (caixas_25 * 25)
caixas_1 = resto_25 // 1

print(caixas_500)
print(caixas_100)
print(caixas_25)
print(caixas_1)  
