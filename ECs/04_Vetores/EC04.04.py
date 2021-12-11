def main():
    tamanho = int(input())
    
    vetor = []
    
    for i in range(tamanho):
        vetor.append(int(input()))
        
    soma = 0
    for i in range(tamanho):
        if (vetor[i] == 1 and i == 0):
            soma = soma + vetor[i + 1]       
        elif (vetor[i] == 1 and i < (tamanho - 1)):
            soma = soma + vetor[i - 1] + vetor[i + 1]
        elif (vetor[i] == 1):
           soma = soma + vetor[i - 1]
            
    print(soma)
    
main()