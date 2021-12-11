def main():
    tamanho = int(input())
    
    matriz = []
    
    for i in range(1, tamanho + 1, +1):
        lista = []
        for j in range(i, tamanho + i, + 1):
            lista.append(j)
        matriz.append(lista)
        
    for i in range(tamanho):
        for j in range(tamanho):
            print(matriz[i][j], end=" ")
        print()
    
main()