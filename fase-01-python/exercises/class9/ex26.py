frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes.'.format(frase.count('A')))
print('A primeira vez que apaerece é na posição {}.'.format(frase.find('A')))
print('A última vez que aparece é na posição {}.'.format(frase.rfind('A')))