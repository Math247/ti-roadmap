# Tipos Primitivos e Saida de Dados

## Os quatro fundamentais:
int -> numeros inteiros -> ex: 5, -5
float -> numeros reais -> ex 4.5, -4.5, 7.0
bool -> numeros booleanos -> ex True, False
str -> String -> 'Olá', '7.5', ''

Obs -> 7 e 7.0 são diferentes, 7.0 é float pois tem o '.' e a casa decimal. isso faz ele virar um float.

O tipo primitivo de uma variavel precisa ser indicada ao receber ou utilizar

ex:

n1 = input('Insira um valor: ') 
Insira um valor: 1 
print(type(n1))
<class 'str'>

Como eu nao indiquei que era inteiro, ele continuou como string.

n1 = int(input('Insira um valor: '))
Insira um valor: 1
print(type(n1))
<class 'int'>

Assim, eu indiquei o tipo primitivo.

## Saida de Dados

print() -> comando para printar na tela

print('A soma vale', x)
print('A soma entre {} e {} vale {}'.format(n1, n2, s)) -> sintaxe nova do Python3

As duas formas funcionam.

o booleano agira dessa forma com valores em variaveis:

n1 = bool(input('Insira um valor: '))
Insira um valor: 
print(type(n1))                      
<class 'bool'>
print(n1)      
False

n1 = bool(input('Insira um valor: '))
Insira um valor: 4
print(n1)
True

Caso tenha valor, ele considera True, caso não tenha valor, considera False