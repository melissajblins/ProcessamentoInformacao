'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

Objetivos do programa: Diferença entre kilo e kibi.

Dados de entrada: Tamanho do arquivo.
Dados de saída: Tamanho do arquivo por GB, Tamanho do arquivo por GiB, diferença entre os tamanhos. 
'''

tamanho = int(input("Digite o tamanho do arquivo: "))
tamanho_GB = (tamanho * (10**9))
tamanho_GiB = (tamanho * (2**30))
print(tamanho_GB)
print(tamanho_GiB)
print((tamanho_GiB - tamanho_GB))