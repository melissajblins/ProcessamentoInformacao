'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

'''
def manutencao(ano: int, motor: int, distancia: float):
    if (((ano >= 1901) and (ano <= 2000)) and ((motor == 100) or (motor == 101))):
        return("SIM")
    elif (((ano >= 2001) and (ano <= 2020)) and (distancia > 5000)):
        return("SIM")
    elif ((ano == 2021) and (distancia > 200) and ((motor == 200) or (motor == 201))):
        return("SIM")
    else:
        return("NAO")


def main():
    ano = int(input("Digite o ano de produção: "))
    motor = int(input("Digite o código do motor principal: "))
    distancia = float(input("Digite a distância percorrida: "))
    revisao = manutencao(ano, motor, distancia)
    print(revisao)
    
main()