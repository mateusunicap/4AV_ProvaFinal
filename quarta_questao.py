def maior(* numeros):
    maior = numeros[0]
    for i in range(1,len(numeros)):
        if numeros[i] > maior:
            maior = numeros[i] 
        print(maior)

maior(123,12)
maior(1,12)
maior(-1,1231)
            
