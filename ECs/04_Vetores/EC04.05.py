def inverte_posicao(vetor: [int], indice_i: int, indice_j: int) -> int:
    if (indice_i < len(vetor) and (indice_j < len(vetor))):
        auxiliar = vetor[indice_i]
        vetor[indice_i] = vetor[indice_j]
        vetor[indice_j] = auxiliar
    return vetor

def main():
    tamanho = int(input())
    
    vetor = []
    
    for i in range(tamanho):
        vetor.append(int(input()))

    indice_i = int(input())
    indice_j = int(input())
    
    vetor_invertido = inverte_posicao(vetor, indice_i, indice_j)
    
    print(vetor_invertido)
    
    
main()