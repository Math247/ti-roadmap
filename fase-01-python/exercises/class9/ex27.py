nome_completo = str(input('Digite o nome completo: ')).strip().title()
nome_completo = nome_completo.split(' ')
print('O primeiro nome é: {}'.format(nome_completo[0]))
print('O ultimo nome é: {}'.format(nome_completo[len(nome_completo)-1]))