'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

Objetivos do programa: Calcular a circunferência de um planeta qualquer por meio do ângulo e da distância
entre duas cidades.

Dados de entrada: Distância entre a cidades e o ângulo.
Dados de saída: Circunferência de um planeta medida em estádios e em kilomêtros
'''

def calculaCircunferenciaEstadios(distancia_estadios: float, angulo: float) -> float:
    """
    Calcula a circunferência de um planeta em estádios a partir da distância entre duas cidades e o ângulo.
    """
    return ((360 * distancia_estadios)/angulo)

def converteKilometros(circunferencia_estadios: float) -> float:
    """
    Converte a circunferência de estádios para kilômetros.
    """
    return ((circunferencia_estadios * 176.4)/1000)

def main():
    distancia_estadios = float(input("Digite a distância entre as cidades (estádios): "))
    angulo = float(input("Digite o ângulo (graus): "))
    circunferencia_estadios = calculaCircunferenciaEstadios(distancia_estadios, angulo)
    circunferencia_kilometros = converteKilometros(circunferencia_estadios)
    print("%.1f" %(circunferencia_estadios))
    print("%.1f" %(circunferencia_kilometros))


main()
    
    

    