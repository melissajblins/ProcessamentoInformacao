'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

'''

def calculaTriangulo(ladoa, ladob, ladoc):
    if ((ladoa + ladob) < ladoc):
        return("INVALIDO")
    elif((ladoa + ladoc) < ladob):
        return("INVALIDO")
    elif((ladob + ladoc) < ladoa):
        return("INVALIDO")
    else:
        return("VALIDO")


def main():
    ladoa = float(input("Digite a medida do lado a: "))
    ladob = float(input("Digite a medida do lado b: "))
    ladoc = float(input("Digite a medida do lado c: "))
    resultado = calculaTriangulo(ladoa, ladob, ladoc)
    print(resultado)
    
main()