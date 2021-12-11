'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

Objetivos do programa: Determinar se é possível balancear perfeitamente a carga de uma espaçonave,
distribuindo a mesma parcela para a parte traseira e para a dianteira. 


Dados de entrada: Quatro cargas em toneladas.
Dados de saída: "Carga balanceável!" se a distribuição for perfeita ou “Não é possível balancear a carga."
caso não for possível fazer o balanceamento. 
'''

def balanceamento(carga1: int, carga2: int, carga3: int, carga4: int) -> str:
    """
    Essa função tem como objetivo determinar se as 4 cargas em questão podem
    ser divididas perfeitamente entre a parte dianteira e traseira da espaçonave. 

    """
    if (carga1 == (carga2 + carga3 + carga4)):
        return True
    if (carga2 == (carga1 + carga3 + carga4)):
        return True
    if (carga3 == (carga1 + carga2 + carga4)):
        return True
    if (carga4 == (carga1 + carga2 + carga3)):
        return True
    if ((carga1 + carga2) == (carga3 + carga4)):
        return True
    if ((carga1 + carga3) == (carga2 + carga4)):
        return True
    if ((carga1 + carga4) == (carga2 + carga3)):
        return True
    return False


def main():
    carga1 = int(input())
    carga2 = int(input())
    carga3 = int(input())
    carga4 = int(input())
    
    resultado = balanceamento(carga1, carga2, carga3, carga4)
 
    if (resultado):
        print("Carga balanceável!")
    else:
        print("Não é possível balancear a carga.")
        
    
    
main()