"""
O segundo exercício apresenta o maior e o menor primo que estão depois e antes, respectivamente, do número digitado pelo o usuário. Caso esse número seja primo, o programa deverá imprimir o número duas vezes.
"""
def eh_primo(numero: int) -> bool:
    contador_multiplos = 0
    for i in range(numero, 0, -1):
        if (numero % i == 0):
            contador_multiplos = contador_multiplos + 1
    if (contador_multiplos == 2):
        return True
    else:
        return False
    
    
def encontra_primos(numero: int, contador_primos: int, passo: int) -> int:
    while (contador_primos < 1):
        contador_multiplos = 0
        numero = numero + passo
        for i in range(numero, 0, -1):
            if (numero % i == 0):
                contador_multiplos = contador_multiplos + 1
        if (contador_multiplos == 2):
            return numero
            contador_primos = contador_primos + 1
    

def main():
    numero = int(input())
    
    if (eh_primo(numero)):
        primo1 = numero
        primo2 = numero
    else: 
        primo1 = encontra_primos(numero, 0, -1)
        primo2 = encontra_primos(numero, 0, +1)
    
    print(primo1, primo2)
    
main()

Função eh_primo(inteiro: numero):
    inteiro: contador_multiplos, i 
    contador_multiplos <- 0
    Para (i <- numero até 0 com i <- i - 1) faça: 
        Se (numero mod i = 0):
            contador_multiplos <- contador_multiplos + 1
    Se (contador_multiplos = 2):
        Devolva verdadeiro
    Senão:
        Devolva Falso
    
    
Funçao encontra_primos(inteiro: numero, inteiro: contador_primos, inteiro: passo):
    inteiro: contador_multiplos, i
    Enquanto (contador_primos < 1) faça:
        contador_multiplos <- 0
        numero <- numero + passo
        Para (i <- numero até 0 com i <- i - 1) faça: 
            Se (numero mod i = 0):
                contador_multiplos <- contador_multiplos + 1
        Se (contador_multiplos = 2):
            Devolva numero
            contador_primos <- contador_primos + 1
    

Funçao principal():
    inteiro: numero, primo1, primo2
    
    Leia (numero)
    
    Se (eh_primo(numero)):
        primo1 <- numero
        primo2 <- numero
    Senão: 
        primo1 <- encontra_primos(numero, 0, -1)
        primo2 <- encontra_primos(numero, 0, +1)
    
    Escreva(primo1, primo2)
    
principal()
