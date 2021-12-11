def main():
    linhas = int(input())
    colunas = int(input())
    
    matriz = []
    
    for i in range(linhas):
        lista = []
        for j in range(colunas):
            if (i == 0):
                lista.append(j+1)
            else:
                lista.append((matriz[i - 1][j]) + colunas)
        matriz.append(lista)
            
    for i in range(linhas):
        for j in range(colunas):
            if (i % 2 == 0):
                print(matriz[i][j], end =" ")
            else:
                print(matriz[i][(colunas - 1) - j], end = " ")
        print()
    
main()