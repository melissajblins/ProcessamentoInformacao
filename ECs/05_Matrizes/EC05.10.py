def main():
    linhas = int(input())
    colunas = int(input())
    
    matriz = []
    
    for i in range(linhas):
        lista = []
        for j in range(colunas):
            lista.append(int(input()))
        matriz.append(lista)
        
    linha_alvo = int(input())
    coluna_alvo = int(input())
    
    contador = 0
    
    if (linha_alvo == 0 and coluna_alvo == 0):
        for i in range(linha_alvo, linha_alvo + 2, + 1):
            for j in range(coluna_alvo, coluna_alvo + 2, + 1):
                if (matriz[i][j] == 1):
                    contador = contador + 1
    elif (linha_alvo == 0 and coluna_alvo == (colunas - 1)):
        for i in range(linha_alvo, linha_alvo + 2, + 1):
            for j in range(coluna_alvo - 1, coluna_alvo + 1, + 1):
                if (matriz[i][j] == 1):
                    contador = contador + 1
    elif (linha_alvo == 0):
        for i in range(linha_alvo, linha_alvo + 2, + 1):
            for j in range(coluna_alvo - 1, coluna_alvo + 2, + 1):
                if (matriz[i][j] == 1):
                    contador = contador + 1
    elif (linha_alvo == (linhas - 1) and coluna_alvo == 0):
         for i in range(linha_alvo - 1, linha_alvo + 1, + 1):
            for j in range(coluna_alvo, coluna_alvo + 2, + 1):
                if (matriz[i][j] == 1):
                    contador = contador + 1
    elif(linha_alvo == (linhas - 1) and coluna_alvo == (colunas - 1)):
        for i in range(linha_alvo - 1, linha_alvo + 1, + 1):
            for j in range(coluna_alvo - 1, coluna_alvo + 1, + 1):
                if (matriz[i][j] == 1):
                    contador = contador + 1
    elif (linha_alvo == (linhas - 1)):
        for i in range(linha_alvo - 1, linha_alvo + 1, + 1):
            for j in range(coluna_alvo - 1, coluna_alvo + 2, + 1):
                if (matriz[i][j] == 1):
                    contador = contador + 1
    elif (coluna_alvo == 0):
        for i in range(linha_alvo - 1, linha_alvo + 2, + 1):
            for j in range(coluna_alvo, coluna_alvo + 2, + 1):
                if (matriz[i][j] == 1):
                    contador = contador + 1
    elif (coluna_alvo == (colunas - 1)):
        for i in range(linha_alvo - 1, linha_alvo + 2, + 1):
            for j in range(coluna_alvo - 1, coluna_alvo + 1, + 1):
                if (matriz[i][j] == 1):
                    contador = contador + 1
    else:
        for i in range(linha_alvo - 1, linha_alvo + 2, + 1):
            for j in range(coluna_alvo - 1, coluna_alvo + 2, + 1):
                if (matriz[i][j] == 1):
                    contador = contador + 1
                    
    if (matriz[linha_alvo][coluna_alvo] == 1):
        print(contador - 1)
    else:
        print(contador)

main()