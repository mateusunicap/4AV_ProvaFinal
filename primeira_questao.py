def RevNum(num):
    numString = str(num)
    if num < 0:
        numString = numString[1::]
    strRevertida = numString[::-1]
    if num < 0:
        strRevertida = '-' + strRevertida
    return int(strRevertida)

num = int(input('Digite um numero inteiro: '))
print(f'O numro digitado foi {num}, e o inverso dele é{RevNum(num)}')
