def comparando_vetores(vetora: [int], vetorb: [int]) -> bool:
    multiplo = (vetorb[0] // vetora[0])
    for i in range(len(vetora)):
        if (vetora[i] * multiplo != vetorb[i]):
            return False 
    return True

    
def main():
    tamanho = int(input())
    
    vetora = []
    vetorb = []
    
    for i in range(tamanho):
        vetora.append(int(input()))
    
    for i in range(tamanho):
        vetorb.append(int(input()))
    
    resultado = comparando_vetores(vetora, vetorb)
    
    if (resultado):
        print("SIM")
    else:
        print("NAO")
    
main()