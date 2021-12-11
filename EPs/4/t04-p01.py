'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

Objetivos do programa: Registrar se o disjuntor aguenta a corrente gerada pelos equipamentos da The Big Bang Party. 

Dados de entrada: Primeira linha: (N) Quantidade de equipamentos, (M) Tamanho da sequência de operações, capacidade máxima suportada pelo disjutor. Próximas N linhas: corrente consumida por cada equipamento. Próximas M linhas: sequências de operações. 
Dados de saída: Se o disjuntor aguentar a festa: corrente máxima registrada. Caso o disjuntor não suporte a carga: índice do equipamento e da operação.
'''

def bazinga(capacidade_maxima: int, vetor_corrente: [int], vetor_manipulacao: [int]) -> (bool, int, int):
    """
    Essa função confere se o disjuntor aguenta a corrente gerada pelos equipamentos da The Big Bang Party.
    Caso não, retorna em o índice do equipamento que foi ligado quando ocorreu o desarme do disjuntor e também
    o índice da operação correspondente.
    Caso o disjuntor aguente a carga, retorna qual foi o consumo máximo registrado. 
    """
    vetor_controle = []
    controle_capacidade = 0
    maior_capacidade = 0
    for i in range(0, len(vetor_manipulacao)):
        if (i == 0):
            vetor_controle.append(vetor_manipulacao[i])
            equipamento = (vetor_manipulacao[i] - 1)
            controle_capacidade = controle_capacidade + vetor_corrente[equipamento]
            maior_capacidade = vetor_corrente[equipamento]
            if (controle_capacidade > capacidade_maxima):
                return False, vetor_manipulacao[i], i
        else:
            if (vetor_manipulacao[i] in vetor_controle):
                vetor_controle.remove(vetor_manipulacao[i])
                equipamento = (vetor_manipulacao[i] - 1)
                controle_capacidade = controle_capacidade - vetor_corrente[equipamento]
            else:
                vetor_controle.append(vetor_manipulacao[i])
                equipamento = (vetor_manipulacao[i] - 1)
                controle_capacidade = controle_capacidade + vetor_corrente[equipamento]

                if (controle_capacidade > maior_capacidade):
                    maior_capacidade = controle_capacidade
                if (controle_capacidade > capacidade_maxima):
                    return False, vetor_manipulacao[i], i
    return True, 0, maior_capacidade       



def main():
    vetor_corrente = []
    vetor_manipulacao = []
    
    vetor_operacoes = input().split()
    for i in range(3):
        vetor_operacoes[i] = int(vetor_operacoes[i])
    
    for i in range(0, vetor_operacoes[0]):
        vetor_corrente.append(int(input()))
    
    for i in range(0, vetor_operacoes[1]):
        vetor_manipulacao.append(int(input()))
    
    teste, final, dado_final = bazinga(vetor_operacoes[2], vetor_corrente, vetor_manipulacao)
    
    if (teste == True):
        print("Bazinga! O maior consumo foi %d." %(dado_final))
    else:
        print("Oh no! O disjuntor sobrecarregou na operação (%d, %d)." %(final, dado_final + 1))
    
    
main()