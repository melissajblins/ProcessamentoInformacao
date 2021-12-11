'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

Objetivos do programa: Imprimir dois descontos sucessivos de 10%.

Dados de entrada: Valor total.
Dados de saída:Valor com desconto. 
'''

valor_total = float(input("Digite o valor do produto (R$): "))
valor_total = valor_total * 0.9
valor_total = valor_total * 0.9
print("%.2f" %(valor_total))