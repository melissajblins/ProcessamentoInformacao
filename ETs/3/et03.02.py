def inverte_numero(numero: int, digitos: int) -> int:
    numero_invertido = 0
    for i in range(digitos, 0, -1):
        numero_invertido = numero_invertido + ((numero % 10) * pow(10, i-1))
        numero = numero // 10
    return numero_invertido

def main():
    numero = int(input())
    digitos = int(input())
    
    numero_invertido = inverte_numero(numero, digitos)
    
    print(numero_invertido)
    
main()