'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

Objetivos do programa: Jogar Street Fighter com Ryu e Ken, quem chegar a 100 de dano primeiro ganha o round, sendo que o jogo acaba quando 0 for digitado.

Dados de entrada: Dano com valor positivo se for golpe de Ryu e dano com valor negativo se for golpe de Ken.
Dados de saída: Se foi Ryu ou Ken quem venceu, caso haja empate: "Houve empate".
'''
def vitoria(vitoria_Ryu: int, vitoria_Ken: int) -> str:
    """
    Essa função tem o objetivo de retornar o ganhador do jogo ou se houve empate.
    """
    if (vitoria_Ryu > vitoria_Ken):
        return("Ryu venceu")
    elif (vitoria_Ken > vitoria_Ryu):
        return("Ken venceu")
    else:
        return("Houve empate")


def main():
    jogada = 1
    vitoria_Ryu = 0
    vitoria_Ken = 0
    while (jogada != 0):
        pontuacao_Ryu = 0
        pontuacao_Ken = 0
        barra_vida = False
        jogada = int(input())
        while (barra_vida == False and jogada != 0):
            if (jogada > 0):
                pontuacao_Ryu = pontuacao_Ryu + jogada
            else:
                pontuacao_Ken = pontuacao_Ken + (jogada * -1)
                
            if (pontuacao_Ryu >= 100 or pontuacao_Ken >= 100):
                barra_vida = True
            else:
                jogada = int(input())  
                
        if (pontuacao_Ryu > pontuacao_Ken):
            vitoria_Ryu = vitoria_Ryu + 1
        elif (pontuacao_Ken > pontuacao_Ryu):
            vitoria_Ken = vitoria_Ken + 1
            
    print(vitoria(vitoria_Ryu, vitoria_Ken))
                
    
main()