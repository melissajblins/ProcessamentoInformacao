def main():
    tamanho = int(input())
    
    vetor = []
    
    for i in range(tamanho):
        vetor.append(int(input()))
     
    maior = 0
    for i in range(tamanho):
        if i == 0:
            maior = vetor[i]
        elif (vetor[i] > maior):
            maior = vetor[i]
            
    print(maior)
    
main()