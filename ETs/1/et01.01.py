def invertendo(numero:int) -> int:
    numero1 = ((numero % 100000) // 10000)
    numero2 = ((numero % 10000) // 1000)
    numero3 = ((numero % 1000) // 100)
    numero4 = ((numero % 100) // 10)
    numero5 = (numero % 10)
    print("%d%d%d%d%d" % (numero5, numero4, numero3, numero2, numero1))

def main ():
    numero = int(input("Digite um número de 5 dígitos: "))
    invertendo(numero)
    
main()