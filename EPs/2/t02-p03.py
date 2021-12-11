'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

Objetivos do programa: Determinar quanto dinheiro Robin Sparkles pode gastar no shopping considerando o estacionamento. 

Dados de entrada: Mesada semanal, hora de chegada, hora de saída.
Dados de saída: O valor que Robin Sparkles pode gastar no shopping.

Let's go to the mall everybody! Go!
C'mon Jessica, C'mon Tori
Let's go to the mall you won't be sorry
Put on your jelly-bracelets
And your cool graffiti-coat

'''
import math


def calcula_estacionamento(hora_entrada: int, minuto_entrada: int, hora_saida: int, minuto_saida: int) -> int:
    """
    Essa função tem como objetivo descobrir a taxa do estacionamento.
    """
    data_inicial_minutos = ((hora_entrada * 60) + minuto_entrada)
    data_final_minutos = ((hora_saida * 60) + minuto_saida)
    tempo_minutos = data_final_minutos - data_inicial_minutos
    
    if (tempo_minutos <= 15):
        return 5
    if (tempo_minutos <= 60):
        return 15
    if (tempo_minutos <= 120):
        return 19
    if (tempo_minutos <= 180):
        return 23
    if (tempo_minutos <= 240):
        return 27
    hora_adicional = math.ceil(tempo_minutos / 60)
    return (15 + (3 * hora_adicional)) 
    
    

def calcula_fatura(mesada: float, valor_estacionamento: int) -> float:
    """
    Essa função calcula o valor que Robin Sparkles pode gastar em compras no shopping.
    """
    return (mesada - valor_estacionamento)



def main():
    mesada = float(input())
    data_entrada = input().split(":")
    data_saida = input().split(":")
    
    hora_entrada = int(data_entrada[0])
    minuto_entrada = int(data_entrada[1])
    
    hora_saida = int(data_saida[0])
    minuto_saida = int(data_saida[1])
    
    valor_estacionamento = calcula_estacionamento(hora_entrada, minuto_entrada, hora_saida, minuto_saida)
    
    valor_final = calcula_fatura(mesada, valor_estacionamento)
    
    print("Você pode gastar até R$ %.2f" % (valor_final))
    
    

main()