'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

'''

def calculaMedia(nota1: float, nota2: float):
    media = (nota1 + nota2)/2
    return (media)

def main():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    resultado = calculaMedia(nota1, nota2)
    if (resultado >= 5.0):
        print("%.2f" % (resultado))
        print("APROVADO")
    else:
        notarec = float(input("Digite a nota da recuperação: "))
        resultadorec = calculaMedia(resultado, notarec)
        print("%.2f" % (resultado))
        print("%.2f" % (resultadorec))
        if (resultadorec >= 5 ):
            print("APROVADO")
        else:
            print("REPROVADO")
            
main()