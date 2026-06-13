nome = str(input('Digite seu nome: ')).strip().upper()
idade = int(input('Digite a idade: '))
autorizacao = str(input('O usuario tem autorização? ')).strip().upper()

if len(autorizacao) > 1:
    print('Precisa digitar S ou N.')
else:
    if autorizacao == 'S':
        print('Tem autorização!')
        if idade >= 18:
            print('Liberado!')
        else:
            print('Você tem menos de 18, não está liberado.')
    elif autorizacao == 'N':
        print('Você não tem autorização')
    else:
        print('Precisa digitar S ou N.')