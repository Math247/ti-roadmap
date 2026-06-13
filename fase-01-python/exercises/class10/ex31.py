distancia = float(input('Qual a distancia da viagem em km? '))
if distancia <= 200:
    print('O preco da passagem é de R${:.2f}'.format(distancia * 0.50))
else:
    print('O preço da passagem é de R${:.2f}'.format(distancia * 0.45))