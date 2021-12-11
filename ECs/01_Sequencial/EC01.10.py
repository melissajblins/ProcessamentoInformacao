'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

Objetivos do programa: Calcular a acurácia, precisão e sensibilidade de uma matriz de confusão.

Dados de entrada: VP, VN, FP, VN.
Dados de saída: Acurácia, precisão e sensibilidade. 
'''

def acuracia(VP, FN, FP, VN):
    acuracia_resultado = (VP + VN) / (VP + VN + FP + FN)
    print("%.2f" % (acuracia_resultado))
    
def precisao(VP, FP):
    precisao_resultado = (VP) / (VP + FP)
    print("%.2f" % (precisao_resultado))
    
def sensibilidade(VP, FN):
    sensibilidade_resultado = (VP) / (VP + FN)
    print("%.2f" % (sensibilidade_resultado))

VP = int(input("Digite os verdadeiros positivos: "))
FN = int(input("Digite os falsos negativos: "))
FP = int(input("Digite os falsos positivos: "))
VN = int(input("Digite os verdadeiros negativos: "))
acuracia(VP, FN, FP, VN)
precisao(VP, FP)
sensibilidade(VP, FN)

