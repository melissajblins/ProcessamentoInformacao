def main():
    tamanho = int(input())
    
    vetor = []
    
    for i in range(tamanho):
        vetor.append(int(input()))
    
    pares = 0
    impares = 0
    for i in range(tamanho):
        if (vetor[i] % 2 == 0):
            pares = pares + 1
        else:
            impares = impares + 1
    
    print(pares)
    print(impares)
    
main()