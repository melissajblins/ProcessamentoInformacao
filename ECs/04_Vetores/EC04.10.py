def busca(vetor_auxiliar: [int], chave: int) -> bool:
    if (chave in vetor_auxiliar):
        return False
    else: 
        return True
            
            
def main():
    tamanho = int(input())
    
    vetor = []
    vetor_auxiliar = []
    
    for i in range(tamanho):
        vetor.append(int(input()))
      
    for i in range(tamanho):
        if (i == 0):
            vetor_auxiliar.append(vetor[i])
        elif (busca(vetor_auxiliar, vetor[i])):
            vetor_auxiliar.append(vetor[i])
    
    for i in range(len(vetor_auxiliar)):
        print(vetor_auxiliar[i])
           
    
main()