num_1 = int(input("Digite um número:"))
num_2 = int(input("Digite um número:"))
num_3 = int(input("Digite um número:"))
ordem = input("Agora, digite 'c' crescente e 'd' para decrescente:")
if ordem == 'd' or ordem == 'D':
    if num_1 > num_2 > num_3:
        print(num_1,num_2,num_3)
        
    elif num_2 > num_3 > num_1:
        print(num_2,num_3,num_1)
        
    elif num_3 > num_1 > num_2:
        print(num_3,num_1,num_2)

    elif num_1 > num_3 > num_2:
        print(num_1,num_3,num_2)

    elif num_2 > num_1 > num_3:
        print(num_2,num_1,num_3)

    elif num_3 > num_2 > num_1:
        print(num_3,num_2,num_1)
        
if ordem == 'C' or ordem == 'c':
    if num_1 > num_2 > num_3:
        print(num_3,num_2,num_1)
        
    elif num_2 > num_3 > num_1:
        print(num_1,num_3,num_2)
        
    elif num_3 > num_1 > num_2:
        print(num_2,num_1,num_3)

    elif num_1 > num_3 > num_2:
        print(num_2,num_3,num_1)

    elif num_2 > num_1 > num_3:
        print(num_3,num_1,num_2)

    elif num_3 > num_2 > num_1:
        print(num_1,num_2,num_3) 
    
