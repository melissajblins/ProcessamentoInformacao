def soma_vetores(vetorA: [int], vetorB: [int]):
    numero1 = 0
    numero2 = 0
    numero3 = 0
    vetorC = []
    
    for i in range(len(vetorA), 0, -1):
        numero1 = numero1 + (vetorA[i - 1]) * 10 ** (i - 1)
        numero2 = numero2 + (vetorB[i - 1]) * 10 ** (i - 1)
    
    numero3 = numero1 + numero2

    for i in range(len(vetorA)):
        vetorC.append(numero3 % 10)
        numero3 = numero3 // 10
    
    return vetorC


def imprime_numeros(vetor: [int]):
    for i in range(len(vetor), 0, -1):
        print(vetor[i - 1], end ="")


def main():
    vetorA = []
    vetorB = []
    vetorC = []
    
    tamanho = int(input())
    
    for i in range(tamanho):
        vetorA.append(int(input()))
    
    for i in range(tamanho):
        vetorB.append(int(input()))
        
    vetorC = soma_vetores(vetorA, vetorB)
    
    imprime_numeros(vetorA) 
    
    print(" + ", end ="")
    
    imprime_numeros(vetorB)
        
    print(" = ", end="")
    
    imprime_numeros(vetorC)
    
main()

"""
def soma_vetores(vetorA: [int], vetorB: [int], tamanho):
    numero1 = 0
    numero2 = 0
    numero3 = 0
    vetorC = [0] * tamanho
    
    for i in range(tamanho, 0, -1):
        numero1 = numero1 + (vetorA[i - 1]) * 10 ** (i - 1)
        numero2 = numero2 + (vetorB[i - 1]) * 10 ** (i - 1)
    
    numero3 = numero1 + numero2

    contador = 0
    for i in range(tamanho):
        vetorC[contador] = (numero3 % 10)
        numero3 = numero3 // 10
        contador = contsdor + 1
    
    return vetorC


def imprime_numeros(vetor: [int], tamanho):
    for i in range(tamanho, 0, -1):
        print(vetor[i - 1], end ="")


def main():
   
    tamanho = int(input())
    
    vetorA = [0] * tamanho
    vetorB = [0] * tamanho
    vetorC = [0] * tamanho
    
    contador = 0
    for i in range(tamanho):
        Leia(numero)
        vetorA[contador] = numero
        contador = contador + 1
    
    contador = 0
    for i in range(tamanho):
        Leia(numero)
        vetorB[contador] = numero
        contador = contador + 1
        
    vetorC = soma_vetores(vetorA, vetorB, tamanho)
    
    imprime_numeros(vetorA, tamanho) 
    
    print(" + ", end ="")
    
    imprime_numeros(vetorB, tamanho)
        
    print(" = ", end="")
    
    imprime_numeros(vetorC, tamanho)
    
principal()
"""