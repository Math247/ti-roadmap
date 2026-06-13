salario = float(input('Qual seu salário? '))
if salario > 1250:
    aumento = salario * 1.10
else:
    aumento = salario * 1.15

print('Seu novo salário é: R${:.2f}'.format(aumento))