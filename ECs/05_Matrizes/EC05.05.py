def main():
    tamanho = int(input())
    
    matriz = []
    
    for i in range(tamanho):
        lista = []
        for j in range(tamanho):
            lista.append(int(input()))
        matriz.append(lista)
        
    soma = 0    
    for i in range(tamanho):
        for j in range(tamanho):
            if (i > j and (matriz[i][j] % 2 == 0)):
                soma = soma + matriz[i][j]
        
    print(soma)
    
main()