def main():
    for numero1 in range(2, 61, 2):
        for numero2 in range(1, 61, 2):
            for numero3 in range(2, 61, 2):
                for numero4 in range(1, 61, 2):
                    for numero5 in range(2, 61, 2):
                        for numero6 in range(1, 61, 2):
                            if (numero1 != numero3 and numero1 != numero5 and numero3 != numero5 and numero2 != numero4 and numero2 != numero6 and numero4 != numero6):
                                print("%d %d %d %d %d %d" %(numero1, numero2, numero3, numero4, numero5, numero6))
        
    
main()