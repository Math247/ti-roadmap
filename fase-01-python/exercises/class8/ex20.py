from random import shuffle
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('O primeiro será {}, o segundo {}, o terceiro {} e o quarto {}.'.format(lista[0], lista[1], lista[2], lista[3]))