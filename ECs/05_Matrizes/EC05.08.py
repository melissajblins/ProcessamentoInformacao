def cria_matriz(nlin: int, ncol: int) -> [[int]]:
    M = []
    for l in range(nlin):
        M.append([0] * ncol)
    return M

def multiplicando_matrizes(matriz_A: int, matriz_B: int):
    matriz_C = cria_matriz(len(matriz_A), len(matriz_B[0]))
    
    for i in range(len(matriz_A)):
        for j in range(len(matriz_B[0])):
            for k in range(len(matriz_A[0])):
                matriz_C[i][j] = matriz_C[i][j] + (matriz_A[i][k] * matriz_B[k][j])

    for i in range(len(matriz_A)):
        for j in range(len(matriz_B[0])):
            matriz_C[i][j] = matriz_C[i][j] * 3
                
    return matriz_C

def main():
    linhas_A = int(input())
    colunas_A = int(input())
    linhas_B = int(input())
    colunas_B = int(input())
    
    matriz_A = []
    matriz_B = []
    matriz_C = []
    
    for i in range(linhas_A):
        lista = []
        for j in range(colunas_A):
            lista.append(int(input()))
        matriz_A.append(lista)
        
    for i in range(linhas_B):
        lista = []
        for j in range(colunas_B):
            lista.append(int(input()))
        matriz_B.append(lista)
        
    matriz_C = multiplicando_matrizes(matriz_A, matriz_B)
    
    for i in range(len(matriz_C)):
        for j in range(len(matriz_C[0])):
            print(matriz_C[i][j], end = " ")
        print()

main()
