'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

'''
def calculaFaixa(temperatura: float):
    if (temperatura < -19):
        return ("Muito baixa")
    elif (temperatura < 29):
        return("baixa")
    elif (temperatura < 199):
        return("Normal")
    elif(temperatura < 249):
        return("Alta")
    else:
        return("Muito alta")


def main():
    temperatura = float(input("Digite a temperatura: "))
    faixa = calculaFaixa(temperatura)
    print(faixa)

main()