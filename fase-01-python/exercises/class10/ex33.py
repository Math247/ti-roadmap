val1 = int(input('Insira um valor: '))
val2 = int(input('Insira um valor: '))
val3 = int(input('Insira um valor: '))

menor = val1
if val2 < val1 and val2 < val3:
    menor = val2
if val3 < val1 and val3 < val2:
    menor = val3

maior = val1
if val2 > val1 and val2 > val3:
    maior = val2
if val3 > val1 and val3 > val2:
    maior = val3

print('O menor é {}, e o maior é {}'.format(menor, maior))