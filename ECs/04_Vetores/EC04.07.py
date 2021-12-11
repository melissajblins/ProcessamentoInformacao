def identifica_espelhado(vetor: [int], tamanho: int) -> bool:
    if (tamanho % 2 == 0):
        contador = 0
        while (contador != (tamanho/2)):
            for i in range(tamanho):
                if (vetor[i] != vetor[(tamanho - 1) - i]):
                    return False
                contador = contador + 1
            return True
    else:
        contador = 0
        while (contador != ((tamanho - 1) /2)):
            for i in range(tamanho):
                if (vetor[i] != vetor[(tamanho - 1) - i]):
                    return False
                contador = contador + 1
            return True


def main():
    tamanho = int(input())
    
    vetor = []
    
    for i in range(tamanho):
        vetor.append(int(input()))
        
    resultado = identifica_espelhado(vetor, tamanho)
    
    if(resultado):
        print("SIM")
    else:
        print("NAO")
    
main()