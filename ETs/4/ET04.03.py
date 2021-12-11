def main():
    vetor_comparacao = []
    
    sequencia1 = input().split()
    sequencia2 = input(). split()
    
    for i in range(len(sequencia1)):
        sequencia1[i] = int(sequencia1[i])
        sequencia2[i] = int(sequencia2[i])
        
    for i in range(len(sequencia1)):
        vetor_comparacao.append(sequencia1[i])
        
    for i in range(len(sequencia2)):
        if (sequencia2[i] in vetor_comparacao):
            vetor_comparacao.remove(sequencia2[i])
        
    if (len(vetor_comparacao) == 0):
        print("É uma permutação!")
    else:
        print("Não é uma permutação!")
        
        
main()

"""
def main():
    Leia(tamanho)
    
    vetor_comparacao = [0] * tamanho
    
    Leia(sequencia1, sequencia2)
    
    contador = 0
    for i in range(tamanho):
        vetor_comparacao[contador] = sequencia1[i]
        contador = contador + 1
        
    for i in range(tamanho):
        for j in range(tamanho):
            if (sequencia2[i] == vetor_comparacao[j]):
                vetor_comparacao[j] = vetor_comparacao[tamanho - 1]
        
    if (tamanho(vetor_comparacao) == 0):
        print("É uma permutação!")
    else:
        print("Não é uma permutação!")
        
        
main()

"""