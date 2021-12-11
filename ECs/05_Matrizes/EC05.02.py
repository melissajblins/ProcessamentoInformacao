def main():
    linhas = int(input())
    colunas = int(input())
    
    matriz = []
    
    for i in range(linhas):
        lista = []
        for j in range(colunas):
            lista.append(int(input()))
        matriz.append(lista)
    
    for i in range(linhas):
        for j in range(1, colunas, +2):
            matriz[i][j] = matriz[i][j] * 3
            
    for i in range(linhas):
        for j in range(colunas):
            print(matriz[i][j], end=" ")
        print()
    
main()