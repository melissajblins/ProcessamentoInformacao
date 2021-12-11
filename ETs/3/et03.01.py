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
    primo1 = encontra_primos(numero, 0, -1)
    primo2 = encontra_primos(numero, 0, +1)
    
    print(primo1, primo2)
    
main()
