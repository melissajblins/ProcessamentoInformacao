'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

Objetivos do programa: Simular uma situação de saque de dinheiro com notas de R$1, R$5, R$10 R$50, R$100.

Dados de entrada: Valor a ser sacado.
Dados de saída: Quantidade total de notas e e número de notas para cada valor.
'''

def calculaNotas(valor: int) -> int:
    """
    Função que calcula o total de notas a ser sacado e o total para cada valor. 
    """
    notas_100 = valor // 100
    resto_100 = valor - (notas_100 * 100)
    notas_50 = resto_100 // 50
    resto_50 = resto_100 - (notas_50 * 50)
    notas_10 = resto_50 // 10
    resto_10 = resto_50 - (notas_10 * 10)
    notas_5 = resto_10 // 5
    resto_5 = resto_10 - (notas_5 * 5)
    notas_1 = resto_5 // 1
    total = notas_100 + notas_50 + notas_10 + notas_5 + notas_1
    return("Saque de %d notas: \n%d notas de 1 \n%d notas de 5 \n%d notas de 10 \n%d notas de 50 \n%d notas de 100 "  % (total, notas_1, notas_5, notas_10, notas_50, notas_100))

def main ():
    valor = int(input("Digite o valor a ser sacado: "))
    resultado = (calculaNotas(valor))
    print(resultado)
    
main()