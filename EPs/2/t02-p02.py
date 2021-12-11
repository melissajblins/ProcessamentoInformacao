'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

Objetivos do programa: Descobrir o dia da semana a partir de uma data de formato DD/MM/AAAA. 

Dados de entrada: Data no formato DD/MM/AAAA.
Dados de saída: Dia da semana correspondente a data ou "Data Inválida" se o formato estiver incorreto.
'''

def validacao(dia: int, mes: int, ano: int) -> str:
    """
    Essa função tem como objetivo validar a data de entrada da main.
    """
    if ((dia < 1) or (dia > 31)):
        return False
    if ((mes < 1) or (mes > 12)):
        return False
    if (ano < 0):
        return False
    if ((mes == 2) and (dia > 28)):
        return False
    if (((mes == 4) or (mes == 6) or (mes == 9) or (mes == 11)) and (dia > 30)):
        return False
    if (((mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12)) and (dia > 31)):
        return False
    else:
        return True
    
    
    
def descobre_data_numero(dia: int, mes: int, ano: int) -> str:
    """
    Essa função tem como objetivo descobrir o dia da semana em número de uma determinada data.
    """
    chave_mes = descobre_chave_mes(mes) #Chamar a função para descobrir a chave do mês
    chave_ano = descobre_chave_ano(mes, ano) # Chamar a função para descobrir a chave do ano
    total_data = dia + chave_mes + chave_ano
    multiplo_7 = total_data // 7
    return (total_data - (7 * multiplo_7))


    
def descobre_chave_mes(mes: int) -> int:
    """
    Essa função tem como objetivo descobrir a chave do mês.
    """
    if (mes == 1):
        return 28;
    if (mes == 2):
        return 31;
    if (mes == 3):
        return 2;
    if (mes == 4):
        return 5;
    if (mes == 5):
        return 7;
    if (mes == 6):
        return 10;
    if (mes == 7):
        return 12;
    if (mes == 8):
        return 15;
    if (mes == 9):
        return 18;
    if (mes == 10):
        return 20;
    if (mes == 11):
        return 23;
    return 25;
    
    
    
def descobre_chave_ano(mes: int, ano: int) -> int:
    """
    Essa função tem como objetivo descobrir a chave do ano. 
    """
    if((mes == 1) or (mes == 2)):
       ano = ano - 1;
   
    return (5 * (ano % 4)) + (4 * (ano % 100)) + (6 * (ano % 400))



def descobre_data_caracter(data_numero: int) -> str:
    """
    Essa função tem como objetivo descobrir o dia da semana em caracteres de uma determinada data.
    """
    if (data_numero == 0):
        return "Domingo"
    if (data_numero == 1):
        return "Segunda-feira"
    if (data_numero == 2):
        return "Terça-feira"
    if (data_numero == 3):
        return "Quarta-feira"
    if (data_numero == 4):
        return "Quinta-feira"
    if (data_numero == 5):
        return "Sexta-feira"
    return "Sábado"



def main():
    data = input().split("/")
    dia = int(data[0])
    mes = int(data[1])
    ano = int(data[2])
    
    resultado = validacao(dia, mes, ano)

    if (resultado):
        dia_numero = (descobre_data_numero(dia, mes, ano))
        print(descobre_data_caracter(dia_numero))
    else:
        print("Data inválida!")



main()