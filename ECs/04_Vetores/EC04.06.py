def testa_vetor(vetor: [int], tamanho: int) -> bool:
    for k in range(tamanho):
        for l in range(k + 1, tamanho, + 1):
            if vetor[k] > vetor[l]:
                return False
    return True          

def main():
    tamanho = int(input())
    
    vetor = []
    
    for i in range(tamanho):
        vetor.append(int(input()))
    
    ordenacao = False
    while (ordenacao == False):
        for i in range(tamanho):
            for j in range(i + 1, tamanho, + 1):
                if vetor[i] > vetor[j]:
                    auxiliar = vetor[i]
                    vetor[i] = vetor[j]
                    vetor[j] = auxiliar
                    
        ordenacao = testa_vetor(vetor, tamanho)

    
    print(vetor)           
                
main()

