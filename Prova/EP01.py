"""
O primeiro exercício calcula a data seguinte à data fornecida pelo o usuário. 
Desconsidera-se anos bissextos por simplicidade e assume-se que a data de entrada é válida.
Se o valor de entrada é (31, 12, 2020), o valor de saída será (01, 01, 2021).

"""
def calcula_dia(dia_entrada: int, mes_entrada: int, ano_entrada: int) -> (int, int, int):
    if (mes_entrada == 1 or mes_entrada == 3 or mes_entrada == 5 or mes_entrada == 7 or mes_entrada == 8 or mes_entrada == 10 or mes_entrada == 12):
        if (dia_entrada == 31):
            dia_entrada = 1
            if (mes_entrada == 12):
                mes_entrada = 1
                ano_entrada = ano_entrada + 1
            else:
                mes_entrada = mes_entrada + 1
        else:
            dia_entrada = dia_entrada + 1
    else:
        if (dia_entrada == 30):
            dia_entrada = 1
            mes_entrada = mes_entrada + 1
        else:
            dia_entrada = dia_entrada + 1

    return dia_entrada, mes_entrada, ano_entrada

def main():
    data_entrada = input().split()
    dia_entrada = int(data_entrada[0])
    mes_entrada = int(data_entrada[1])
    ano_entrada = int(data_entrada[2])
    
    dia_saida, mes_saida, ano_saida = calcula_dia(dia_entrada, mes_entrada, ano_entrada)
    
    
    print(dia_saida, mes_saida, ano_saida)
    
main()

Função calcula_dia(inteiro: dia_entrada, inteiro: mes_entrada, inteiro: ano_entrada):
    Se (mes_entrada = 1 ou mes_entrada = 3 ou mes_entrada = 5 ou mes_entrada = 7 ou mes_entrada = 8 ou mes_entrada = 10 ou mes_entrada = 12):
        Se (dia_entrada = 31):
            dia_entrada <- 1
            Se (mes_entrada = 12):
                mes_entrada <- 1
                ano_entrada <- ano_entrada + 1
            Senao:
                mes_entrada <- mes_entrada + 1
        Senao:
            dia_entrada <- dia_entrada + 1
    Senao:
        Se (dia_entrada = 30):
            dia_entrada <- 1
            mes_entrada <- mes_entrada + 1
        Senao:
            dia_entrada <- dia_entrada + 1

    Devolva dia_entrada, mes_entrada, ano_entrada

Função principal():
    inteiro: dia_entrada, mes_entrada, ano_entrada, dia_saida, mes_saida, ano_saida
        
    Leia (dia_entrada, mes_entrada, ano_entrada) 
    
    dia_saida, mes_saida, ano_saida <- calcula_dia(dia_entrada, mes_entrada, ano_entrada)
    
    Escreva(dia_saida, mes_saida, ano_saida)
    
principal()