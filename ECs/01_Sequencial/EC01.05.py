'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

Objetivos do programa: Adicionar um bit de paridade para deixar o valor de 1s par.

Dados de entrada: 7 valores de 1 ou 0.
Dados de saída: Bit de paridade. 
'''

valor1 = int(input("Digite o primeiro dígito: "))
valor2 = int(input("Digite o segundo dígito: "))
valor3 = int(input("Digite o terceiro dígito: "))
valor4 = int(input("Digite o quarto dígito: "))
valor5 = int(input("Digite o quinto dígito: "))
valor6= int(input("Digite o sexto dígito: "))
valor7 = int(input("Digite o sétimo dígito: "))

valor_final = valor1 + valor2 + valor3 + valor4 + valor5 + valor6 + valor7
print(valor_final % 2)