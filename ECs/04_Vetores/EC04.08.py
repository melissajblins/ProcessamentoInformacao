def vetor_ordenado(vetor:[int], tamanho: int) -> bool:
    for i in range(tamanho):
        for j in range(i + 1, tamanho, +1):
            if (vetor[j] < vetor[i]):
                return False
    return True


def main():
    tamanho = int(input())
    
    vetor = []
    
    for i in range(tamanho):
        vetor.append(int(input()))
    
    resultado = vetor_ordenado(vetor, tamanho)
    
    if (resultado):
        print("SIM")
    else:
        print("NAO")
    
main()