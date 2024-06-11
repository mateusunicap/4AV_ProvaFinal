def pot(a,b):
    tot = 1
    for i in range(b):
        tot *= a
    return tot


a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
resultado = pot(a,b)
print(f'O resultado da operação é {resultado}')