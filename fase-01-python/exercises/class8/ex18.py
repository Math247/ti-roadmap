from math import cos, sin, tan, radians
angulo = float(input('Digite um angulo: '))
print('O seno é: {:.2f}, o coseno é: {:.2f}, e a tangente é: {:.2f}'.format(sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))