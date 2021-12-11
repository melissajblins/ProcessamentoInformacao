'''
Nome: Melissa Junqueira de Barros Lins
RA: 11201920583

'''
def main():
    quantidade_total = int(input())
    pedidos = int(input())
    
    pedidos_atendidos = 0
    
    for i in range(1, pedidos+1):
        valor_pedido = int(input())
        if (valor_pedido <= quantidade_total):
            quantidade_total = quantidade_total - valor_pedido
            pedidos_atendidos = pedidos_atendidos + 1
            
    print(pedidos_atendidos)
    
main()