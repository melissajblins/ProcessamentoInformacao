'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

'''

def calculandoComissao(vendas: int):
    return (vendas * 0.2)


def main():
    salario = float(input("Digite seu salário fixo: "))
    vendas = float(input("Digite o valor de vendas: "))
    comissao = calculandoComissao(vendas)
    print("%.2f" % (comissao))
    if ((salario*0.5) <= comissao):
        print("Atingiu meta de vendas")
    else:
        print("Nao atingiu meta de vendas")
    
main()