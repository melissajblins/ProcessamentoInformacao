'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

Objetivos do programa: Definir se um gene foi ou não silenciado por um casamento entre uma sequência de mRNA 
e um oligonucleotídeo.

Dados de entrada: (1) Sequência do mRNA e (2) 0ligonucleotídeo.
Dados de saída:  "Não silenciado" caso não haja casamento e "Silenciado em X" quando houver casamento, sendo que X
significa a posição na qual o casamento ocorre. 
'''
def converte_sequencia_vetor(sequencia: str) -> [int]:
    """
    Converter a sequência para vetor.
    """
    vetor_sequencia = []
    for i in range(len(sequencia)):
        vetor_sequencia.append(str(sequencia[i]))
        
    return vetor_sequencia
    
 
    
def inverte_vetor(vetor_inverter: [int]) -> [int]:
     """
     Inverter as posições do vetor.
     """
     vetor_invertido = []
     for i in range(len(vetor_inverter), 0, -1):
         vetor_invertido.append(vetor_inverter[i - 1])
     
     return vetor_invertido
 
    
def inverte_base(vetor_converter: [int]) -> [int]:
    """
    Converter as bases do vetor.
    """
    vetor_convertido = []
    for i in range(len(vetor_converter)):
        if (vetor_converter[i] == "A"):
            vetor_convertido.append("U")
        elif (vetor_converter[i] == "U"):
            vetor_convertido.append("A")
        elif (vetor_converter[i] == "C"):
            vetor_convertido.append("G")
        elif (vetor_converter[i] == "G"):
            vetor_convertido.append("C")
    
    return vetor_convertido
                   
    
def compara_sequencias(sequencia1: [int], sequencia2: [int]) -> (bool, int):
    """
    Compara as sequências e retorna o resultado final.
    """
    posicao = 0
    for i in range(len(sequencia1)):
        if (sequencia1[i] == sequencia2[0]):
            k = i
            posicao = i + 1
            contador = 0
            for j in range(len(sequencia2)):
                if (k < len(sequencia1)):
                    if (sequencia1[k] == sequencia2[j]):
                        contador = contador + 1
                k = k + 1
            if (contador == (len(sequencia2))):
                return True, posicao
    return False, 0
    
    
def main():
    vetor_mRNA = []
    vetor_oligonucleotideo = []
    vetor_invertido_oligonucleotideo = []
    vetor_base_invertido = []
    
    sequencia_mRNA = input()
    oligonucleotideo = input()
    
    vetor_mRNA = converte_sequencia_vetor(sequencia_mRNA)
    vetor_oligonucleotideo = converte_sequencia_vetor(oligonucleotideo)
    
    vetor_invertido_oligonucleotideo = inverte_vetor(vetor_oligonucleotideo)
    
    vetor_base_invertido = inverte_base(vetor_invertido_oligonucleotideo) 
    
    teste, local = compara_sequencias(vetor_mRNA, vetor_base_invertido)
    
    if (teste):
        print("Silenciado em %d" %(local))
    else:
        print("Não silenciado")
    
    
main()