dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos km o carro percorreu? '))
print('O preço a pagar é: {:.2f}'.format((60*dias)+(km*0.15)))