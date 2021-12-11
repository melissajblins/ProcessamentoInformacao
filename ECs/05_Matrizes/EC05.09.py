def confere_multiplo(matriz: int):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
           if (matriz[i][j] % 10 != 0):
               return False
    return True

def confere_ordenacao(matriz: int):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            for k in range(j + 1, len(matriz[0]), + 1):
                if (matriz[i][j] > matriz[i][k]):
                    resultado = testa_vetor(matriz[i], len(matriz[0]), 1)
                    if (resultado == False):
                        return resultado
                else:
                    resultado = testa_vetor(matriz[i], len(matriz[0]), 0)
                    if (resultado == False):
                        return resultado
    return True
    
def testa_vetor(vetor: [int], tamanho: int, operacao: int) -> bool:
    if (operacao == 0):
        for k in range(tamanho):
            for l in range(k + 1, tamanho, + 1):
                if vetor[k] > vetor[l]:
                    return False
    else:
        for k in range(tamanho):
            for l in range(k + 1, tamanho, + 1):
                if vetor[k] < vetor[l]:
                    return False
    return True 

def main():
    linhas = int(input())
    colunas = int(input())
    
    matriz = []
    
    for i in range(linhas):
        lista = []
        for j in range(colunas):
            lista.append(int(input()))
        matriz.append(lista)
    
    multiplo = confere_multiplo(matriz)
    
    ordenado = confere_ordenacao(matriz)
    
    if (multiplo and ordenado):
        print("SIM")
    else:
        print("NAO")
    
main()