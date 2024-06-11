def contar(num):
    numString = str(num)
    if num < 0:
        numString = numString[1:]
    tam = len(numString)
    return tam

num = int(input('Digite um numero e o programa retornara a quantidade de casa decimal: '))
print(f'O numero digitado tem {contar(num)} casas decimais')