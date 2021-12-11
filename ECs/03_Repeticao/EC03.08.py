'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

'''
def main():
    numero = int(input())
    
    total_primos = 0
    valor = 2
    soma_multiplos = 0
    
    while (total_primos < numero):
        testando_valor = valor
        for i in range(testando_valor, 0, -1):
            if (valor % i == 0):
                soma_multiplos = soma_multiplos + 1
        if (soma_multiplos == 2):
            total_primos = total_primos + 1
            print(valor)
        soma_multiplos = 0
        valor = valor + 1
        
main()
