def separando(numero1: int, numero2: int) -> int:
    numero1A = ((numero1 % 1000) // 100)
    numero1B = ((numero1 % 100) // 10)
    numero1C = (numero1 % 10)
    numero2A = ((numero2 % 1000) // 100)
    numero2B = ((numero2 % 100) // 10)
    numero2C = (numero2 % 10)
    multiplicando(numero1A, numero1B, numero1C, numero2A, numero2B, numero2C)
    
def multiplicando(numero1A: int, numero1B: int, numero1C: int, numero2A: int, numero2B: int, numero2C: int) -> int:
    
    unidade = (numero2C * numero1C)
    resto_unidade = ((unidade % 100) // 10)
    dezena = ((numero2C * numero1B) + resto_unidade)
    resto_dezena = ((dezena % 100) // 10)
    centena = ((numero2C * numero1A) + resto_dezena)
    primeira_linha = (centena * 100 + (dezena % 10) * 10 + (unidade % 10) * 1)
     
    unidade = 0
    dezena = (numero2B * numero1C)
    resto_dezena = ((dezena % 100) // 10)
    centena = ((numero2B * numero1B) + resto_dezena)
    resto_centena = ((centena % 100) // 10)
    unidade_milhar = ((numero2B * numero1A) + resto_centena)
    segunda_linha = (unidade_milhar * 1000 + (centena % 10) * 100 + (dezena % 10) * 10 + unidade * 1)
    
    unidade = 0
    dezena = 0
    centena = (numero2A * numero1C)
    resto_centena = ((centena % 100) // 10)
    unidade_milhar = ((numero2A * numero1B) + resto_centena)
    resto_milhar = ((unidade_milhar % 100) // 10)
    dezena_milhar = ((numero2A * numero1A) + resto_milhar)
    terceira_linha = (dezena_milhar * 10000 + (unidade_milhar % 10) * 1000 + (centena % 10) * 100 + dezena * 10 + unidade * 1)
    
    print("%d" %(primeira_linha + segunda_linha + terceira_linha))

def main():
    numero1 = int(input("Digite um número de três dígitos: "))
    numero2 = int(input("Digite outro número de três dígitos: "))
    separando(numero1, numero2)
    
main()

