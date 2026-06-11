from math import pow, hypot
oposto = float(input('Digite o cateto oposto: '))
adjacente = float(input('Digite o cateto adjacente: '))
print('A hipotenusa é: {:.2f}'.format(pow((pow(oposto, 2) + pow(adjacente,2)),0.5)))
print('A hipotenusa usando hypot é: {:.2f}'.format(hypot(oposto, adjacente)))