'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

Objetivos do programa: Constatar se um número faz parte da sequência de Fibonacci.

Dados de entrada: (1) total de números a serem digitados, (2) números.
Dados de saída: Números que fazem parte da sequência de Fibonacci ou "Sabia que era místico demais!" se nenhum número digitado fizer.
'''
def eh_Fibonacci(numero: int) -> bool:
    """
    Essa função tem o objetivo de definir se um número faz parte da sequência de Fibonacci.
    """
    numero1 = 1
    numero2 = 1
    soma = 0
    
    while (numero1 <= numero or numero2 <= numero or soma <= numero):
        soma = numero1 + numero2
        if (numero == numero1 or numero == 2 or numero == soma ):
            return True
        numero1 = numero2
        numero2 = soma
    
    return False

def main():
    contador = 0
    tamanho = int(input())
    for i in range(tamanho):
        numero = int(input())
        if eh_Fibonacci(numero):
            print(numero, end=" ")
            contador = contador + 1
    if (contador == 0):
        print("Sabia que era místico demais!")
    
main()
