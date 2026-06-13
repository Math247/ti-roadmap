# Validador de Acesso

Projeto simples em Python para praticar condições e tomada de decisão usando `if`, `elif` e `else`.

## Objetivo

O objetivo deste projeto é validar se um usuário pode acessar um sistema com base em duas informações:

- idade;
- autorização de acesso.

Este projeto faz parte do Estágio 2 da Fase 01 - Python.

## Conceitos Praticados

- entrada de dados com `input()`;
- conversão de tipos com `int()`;
- tratamento básico de strings com `strip()` e `upper()`;
- operadores relacionais;
- condições com `if`;
- condições compostas com `if`, `elif` e `else`;
- blocos indentados;
- validação simples de entrada.

## Regras do Programa

O programa solicita:

1. nome do usuário;
2. idade;
3. informação se o usuário tem autorização.

O acesso é liberado apenas quando:

- o usuário tem autorização;
- a idade é maior ou igual a 18 anos.

Caso contrário, o programa informa o motivo da recusa.

## Como Executar

Execute o arquivo com Python:

```bash
python validador-acesso.py
```

## Exemplo de Uso

Entrada:

```txt
Digite seu nome: Matheus
Digite a idade: 25
O usuario tem autorização? S
```

Saída:

```txt
Tem autorização!
Liberado!
```

## Exemplo de Acesso Negado

Entrada:

```txt
Digite seu nome: Matheus
Digite a idade: 16
O usuario tem autorização? S
```

Saída:

```txt
Tem autorização!
Você tem menos de 18, não está liberado.
```

## Melhorias Futuras

- tratar erro caso o usuário digite texto no campo de idade;
- aceitar apenas `S` ou `N` como resposta válida;
- melhorar as mensagens exibidas ao usuário;
- separar a lógica em funções;
- criar testes automatizados.
