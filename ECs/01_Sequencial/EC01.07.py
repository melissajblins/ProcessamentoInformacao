'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

Objetivos do programa: Encriptação adicionando 1 ao valor de cada casa de um número.

Dados de entrada: Número a ser encriptado.
Dados de saída: Valor Número encriptado. 
'''

numero = int(input("Digite o número a ser encriptado: "))
valor1 = ((((numero%10000) // 1000) + 1) % 10)
valor2 = ((((numero%1000) // 100) + 1) % 10)
valor3 = ((((numero%100) // 10) + 1) % 10)
valor4 = (((numero%10) + 1) % 10)

print("%d%d%d%d" % (valor1, valor2, valor3, valor4))