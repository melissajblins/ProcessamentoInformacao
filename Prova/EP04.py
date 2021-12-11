"""
No último exercício é preciso converter uma matriz de minas que possui os inteiros 0 e 1 (representando a ausência ou presença de minas) em um tabuleiro no qual cada casa simboliza quantas minas há em volta ou se naquela casa há uma mina, nesse caso dela deverá ser preenchida com um "*".
"""
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
        for j in range(colunas):
            if (matriz[i][j] == 1):
               matriz[i][j] = "*" 

    
    for i in range(linhas):
        for j in range(colunas):
            contador = 0
            if (i == 0 and j == 0 and matriz[i][j] != "*"):
                for k in range(i, i + 2, + 1):
                    for l in range(j, j + 2, + 1):
                        if (matriz[k][l] == "*"):
                            contador = contador + 1
                matriz[i][j] = contador
            elif (i == 0 and j == (colunas - 1) and matriz[i][j] != "*"):
                for k in range(i, i + 2, + 1):
                    for j in range(j - 1, j + 1, + 1):
                        if (matriz[k][l] == "*"):
                            contador = contador + 1
                matriz[i][j] = contador
            elif (i == 0 and matriz[i][j] != "*"):
                for k in range(i, i + 2, + 1):
                    for l in range(j - 1, j + 2, + 1):
                        if (matriz[k][l] == "*"):
                            contador = contador + 1
                matriz[i][j] = contador
            elif (i == (linhas - 1) and j == 0 and matriz[i][j] != "*"):
                for k in range(i - 1, i + 1, + 1):
                    for l in range(j, j + 2, + 1):
                        if (matriz[k][l] == "*"):
                            contador = contador + 1
                matriz[i][j] = contador
            elif(i == (linhas - 1) and j == (colunas - 1) and matriz[i][j] != "*"):
                for k in range(i - 1, i + 1, + 1):
                    for l in range(j - 1, j + 1, + 1):
                        if (matriz[k][l] == "*"):
                            contador = contador + 1
                matriz[i][j] = contador
            elif (i == (linhas - 1) and matriz[i][j] != "*"):
                for k in range(i - 1, i + 1, + 1):
                    for l in range(j - 1, j + 2, + 1):
                       if (matriz[k][l] == "*"):
                            contador = contador + 1
                matriz[i][j] = contador
            elif (j == 0 and matriz[i][j] != "*"):
                for k in range(i - 1, i + 2, + 1):
                    for l in range(j, j + 2, + 1):
                        if (matriz[k][l] == "*"):
                            contador = contador + 1
                matriz[i][j] = contador
            elif (j == (colunas - 1) and matriz[i][j] != "*"):
                for k in range(i - 1, i + 2, + 1):
                    for l in range(j - 1, j + 1, + 1):
                        if (matriz[i][j] == 1):
                            contador = contador + 1
            elif(matriz[i][j] != "*"):
                for k in range(i - 1, i + 2, + 1):
                    for l in range(j - 1, j + 2, + 1):
                       if (matriz[k][l] == "*"):
                            contador = contador + 1
                matriz[i][j] = contador
                
    for i in range(linhas):
        for j in range(colunas):
            print(matriz[i][j], end=" ")
        print()
    
main()