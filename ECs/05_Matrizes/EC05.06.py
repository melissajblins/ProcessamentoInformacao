def main():
    tamanho = int(input())
    
    matriz = []
    
    for i in range(tamanho):
        lista = []
        for j in range(tamanho):
            lista.append(int(input()))
        matriz.append(lista)
    
    for i in range(tamanho):
        for j in range(tamanho):
            matriz[i][j] = matriz[i][j] + matriz[i][(tamanho - 1) - j]
    
    for i in range(tamanho):
        for j in range(tamanho):
            matriz[i][j] = matriz[i][j] + matriz[(tamanho - 1) - i][j]
    
    for i in range(tamanho // 2):
        for j in range(tamanho // 2):
            print(matriz[i][j], end =" ")
        print()
    
main()