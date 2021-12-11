def main():
    linhas = int(input())
    colunas = int(input())
    
    matriz_notas = []
    
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(float(input()))   
        matriz_notas.append(linha)       
        
    
    for i in range(linhas):
        soma = 0
        for j in range(colunas):
            soma = soma + matriz_notas[i][j]
        matriz_notas[i].append((soma/colunas))
    
    for i in range(linhas):
       for j in range(colunas + 1):
           print(matriz_notas[i][j], end=" ")
       print()
            
    
main()