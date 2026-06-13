vel = float(input('Qual a velocidade do carro? '))
if vel > 80:
    print('Você foi multado! O valor é de {}.'.format((vel - 80) * 7))
else:
    print('Sua velocidade está dentro do permitido.')