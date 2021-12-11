'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

Objetivos do programa: Calcular a média de um aluno.

Dados de entrada: 3 notas.
Dados de saída: Média aritmética do aluno.
'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3)/3
print("%.2f" %(media))