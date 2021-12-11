'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

'''

def origemEdestino (codigo: int):
    if (codigo == 80):
        return("Marte")
    elif(codigo == 81):
        return("Saturno")
    elif(codigo == 90):
        return("Netuno")
    else:
        return("HD21749b")


def modeloDisco(codigo: int):
    if (codigo == 60):
        return("A6000")
    elif(codigo == 61):
        return("B7500")
    else:
        return("C9000")


def main():
    codigo = int(input("Digite o código do disco voador: "))
    codigo_origem = (codigo // 10000)
    codigo_destino = (codigo // 100) % 100
    codigo_modelo = (codigo % 100)
    
    origem = origemEdestino(codigo_origem)
    destino = origemEdestino(codigo_destino)
    modelo = modeloDisco(codigo_modelo)
    
    print(origem)
    print(destino)
    print(modelo)
    

main()