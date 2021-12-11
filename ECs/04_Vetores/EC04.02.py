def main():
    tamanho = int(input())
    vetor_nome = []
    vetor_nota = []
    
    for i in range(tamanho):
        vetor_nome.append(str(input()))
        vetor_nota.append(float(input()))
        
    soma = 0
    for i in range(tamanho):
        soma = soma + vetor_nota[i]
        
    for i in range(tamanho):
        if vetor_nota[i] > (soma/tamanho):
            print(vetor_nome[i])
            
    
    
main()