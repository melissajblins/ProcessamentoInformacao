'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

'''

def comparandoDatas(dia1, mes1, ano1, dia2, mes2, ano2):
    if (ano1 < ano2):
        return("DATA1")
    elif (ano2 < ano1):
        return ("DATA2");
    else:
        if (mes1 > mes2):
            return("DATA2")
        elif(mes2 > mes1):
            return("DATA1")
        else:
            if(dia1 > dia2):
                return("DATA2")
            elif(dia2 > dia1):
                return("DATA1")
            else:
                return("IGUAIS")


def main():
    dia1 = int(input("Digite o dia da data 1: ")) 
    mes1 = int(input("DIgite o mês da data 1: "))
    ano1 = int(input("Digite o ano da data 1: "))
    dia2 = int(input("Digite o dia da data 2: "))
    mes2 = int(input("DIgite o mês da data 2: "))
    ano2 = int(input("Digite o ano da data 2: "))
    resultado = comparandoDatas(dia1, mes1, ano1, dia2, mes2, ano2)
    print(resultado)
    
main()
    
