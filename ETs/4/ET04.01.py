
def busca_chave(principal: [int], chave: [int]):
    for i in range(len(principal)):
        if (chave[0] == principal[i]):
            return i
    return -1


def main():
    vetor_principal = []
    vetor_auxiliar = []
    
    tamanho = int(input())
    
    for i in range(tamanho):
        vetor_principal.append(int(input()))
        
    for i in range(tamanho):
        if (i == 0):
            vetor_auxiliar.append(vetor_principal[0])
        else:
            if (vetor_principal[i] in vetor_auxiliar):
                vetor_auxiliar.remove(vetor_principal[i])
            else:
                vetor_auxiliar.append(vetor_principal[i])
    
    posicao = busca_chave(vetor_principal, vetor_auxiliar)
    
    print(posicao)
    
main()

"""
def busca_chave(principal: [int], chave, tamanho):
    for i in range(tamanho):
        if (chave == principal[i]):
            return i
    return -1


def main():
    tamanho = int(input())
    
    vetor_principal = [0] * tamanho
    vetor_auxiliar = [0] * tamanho
    
    contador = 0
    for i in range(tamanho):
        Leia (numero)
        vetor_principal[contador] = numero
        vetor_auxiliar[contador] = numero
        contador = contador + 1
     
    for i in range(tamanho):
        for j in range(tamanho):
             if (vetor_principal[i] == vetor_auxiliar[j]):
                    vetor_auxiliar[j] = vetor_auxiliar[tamanho - 1]

    posicao = busca_chave(vetor_principal, vetor_auxiliar[0], tamanho)
    
    print(posicao)
    
main()

"""