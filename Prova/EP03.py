"""
O terceiro exercício calcula os pares ordenados que satisfazem a equação xy − x² + y em seu valor máximo.
"""
def main():
    vetor_x = []
    vetor_y = []
    
    numero_n = int(input())
    numero_m = int(input())
    
    valor_maximo = 0
    
    for numero_x in range(numero_n + 1):
        for numero_y in range(numero_m + 1):
            if (numero_x == 0 and numero_y == 0):
                expressao = (numero_x * numero_y - numero_x * numero_x + numero_y)
                valor_maximo = expressao
            else:
                expressao = numero_x * numero_y - numero_x * numero_x + numero_y
                if (expressao > valor_maximo):
                    valor_maximo = expressao
    
    for numero_x in range(numero_n + 1):
        for numero_y in range(numero_m + 1):
            expressao = numero_x * numero_y - numero_x * numero_x + numero_y
            if (expressao == valor_maximo):
                vetor_x.append(numero_x)
                vetor_y.append(numero_y)
                
    for i in range(len(vetor_x)):
        print("(%d, %d)" %(vetor_x[i], vetor_y[i]))
    
main()

Funçao fatorial(inteiro: numero1, inteiro: numero2):
    #Arranjo para descobrir o tamanho que deve ser suportado pelo vetor: (total)!/(total-parcela)!
    inteiro: total, parcela, fatorial1, fatorial2, i
    total <- numero1 + numero2
    parcela <- total - 2
    fatorial1 <- 1
    fatorial2 <- 1
    
    Para (i <- 1 até total + 1 com i <- i + 1) faça:
        fatorial1 <- fatorial1 * i
    
    Para (i <- 1 até parcela + 1 com i <- i + 1) faça:
        fatorial2 = fatorial2 * i
        
    Devolva(fatorial1/fatorial2)
    

Função principal:
    inteiro: numero_n, numero_m, arranjo, numero_x, numero_y, valor_maximo, expressao, contador, i
    
    Leia(numero_n, numero_m)
    
    arranjo = fatorial(numero_n, numero_m)
    
    inteiro: vetor_x[arranjo], vetor_y[arranjo]
    
    expressao <- 0
    valor_maximo <- 0
    
    Para (numero_x <- 0 ate numero_n + 1 com numero_x <- numero_x + 1) faça:
        Para (numero_y <- 0 ate numero_m + 1 com numero_y <- numero_y + 1) faça:
            Se (numero_x = 0 e numero_y = 0):
                expressao <- (numero_x * numero_y - numero_x * numero_x + numero_y)
                valor_maximo <- expressao
            Senao:
                expressao <- numero_x * numero_y - numero_x * numero_x + numero_y
                Se (expressao > valor_maximo):
                    valor_maximo <- expressao
                    
    contador <- 0
    
    Para (numero_x <- 0 ate numero_n + 1 com numero_x <- numero_x + 1) faça:
        Para (numero_y <- 0 ate numero_m + 1 com numero_y <- numero_y + 1) faça:
            expressao <- numero_x * numero_y - numero_x * numero_x + numero_y
            Se (expressao = valor_maximo):
                vetor_x[contador] <- numero_x
                vetor_y[contador] <- numero_y
                contador <- contador + 1
                
    Para (i <- 0 até contador com i <- i + 1) faça:
        Escreva("(" + vetor_x[i] + "," + vetor_y[i] + ")")
    
principal()
