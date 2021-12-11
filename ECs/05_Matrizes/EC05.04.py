def testa_vetor(vetor: [int], tamanho: int) -> bool:
    for k in range(tamanho):
        for l in range(k + 1, tamanho, + 1):
            if vetor[k] > vetor[l]:
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
  
    for teste in range(linhas):
        ordenacao = False
        while (ordenacao == False):
            for i in range(colunas):
                for j in range(i + 1, colunas, + 1):
                    if matriz[teste][i] > matriz[teste][j]:
                        auxiliar = matriz[teste][i]
                        matriz[teste][i] = matriz[teste][j]
                        matriz[teste][j] = auxiliar
                        
            ordenacao = testa_vetor(matriz[teste], colunas)
    
    for i in range(linhas):
        for j in range(colunas):
            print(matriz[i][j], end=" ")
        print()
    
    
main()