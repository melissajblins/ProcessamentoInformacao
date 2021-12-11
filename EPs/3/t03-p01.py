'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

Objetivos do programa: Calcular o número na base 10 de qualquer número em qualquer base. 

Dados de entrada: (1) Base do número, (2) número, (3) digítos do número.
Dados de saída: Número convertido para a base 10.  
'''
def convertendo_base10(base: int, numero_base: int, digitos: int) -> int:
    """
    Converte um número de uma base qualquer em um número de base 10.
    """
    valor_final = 0
    for i in range(digitos):
        unidade = (numero_base % 10)
        valor_final = valor_final + (unidade * base**i)
        numero_base = numero_base // 10
    return valor_final


def main():
    base = int(input())
    numero_base = int(input())
    digitos = int(input())
    
    resultado = convertendo_base10(base, numero_base, digitos)
    
    print(resultado)
    
main()