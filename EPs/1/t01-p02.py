'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

Objetivos do programa: Imprimir em ordem crescente e descrescente três números inteiros

Dados de entrada: Três números inteiros (na mesma linha).
Dados de saída: Duas linhas: a primeira em ordem decrescente e a segunda em ordem crescente.
'''

def ordenando(numero1: int, numero2: int, numero3: int) -> str:
    """
    Função que ordena em ordem decrescente e crescente três números inteiros positivos.
    """
    maior1 = max(numero1, numero2) #Maior entre 1 e 2
    menor1 = ((numero1 + numero2) - maior1) #Menor entre 1 e 2
    maior2 = max(maior1, numero3) #Maior entre maior1 e 3
    menor2 = ((maior1 + numero3) - maior2) #Menor entre maior1 e 3
    maior3 = max(menor1, menor2) #Maior entre menor2 e menor1 
    menor3 = ((menor1 + menor2) - maior3) #Menor de todos
    return("%d %d %d \n%d %d %d" %(maior2, maior3, menor3, menor3, maior3, maior2))
    
def main():
    numeros = input("Digite os três números separados por espaço: ").split()
    numero1 = int(numeros[0])
    numero2 = int(numeros[1])
    numero3 = int(numeros[2])
    decrescente = ordenando(numero1, numero2, numero3)
    print(decrescente)

main()