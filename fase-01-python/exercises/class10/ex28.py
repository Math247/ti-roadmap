import random
numero_computador =  random.randrange(0,5)
numero_usuario = int(input('Em que número pensei? '))
print('Você acertou o numero!'if numero_usuario == numero_computador else 'Você errou, o computador escolheu {}, e você {}'.format(numero_computador, numero_usuario))