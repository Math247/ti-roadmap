# Consulta CEP

Projeto simples em Python para consultar informações de endereço usando a API pública ViaCEP.

## Objetivo

Praticar os fundamentos estudados no Estágio 1 da Fase 01 - Python:

- variáveis;
- tipos primitivos;
- entrada de dados com `input()`;
- validação simples de strings;
- importação de módulos;
- consumo de API;
- leitura de resposta em JSON;
- saída de dados com `print()`.

## API Utilizada

Este projeto utiliza a API pública ViaCEP:

https://viacep.com.br/

Exemplo de endpoint:

```txt
https://viacep.com.br/ws/01001000/json/
```

## Como Executar

Instale a dependência:

```bash
pip install requests
```

Execute o arquivo:

```bash
python consulta-cep.py
```

## Como Funciona
O programa solicita um CEP ao usuário e realiza algumas validações antes de chamar a API:
1. Remove espaços no início e no final com strip().
2. Verifica se o CEP possui exatamente 8 caracteres.
3. Verifica se o CEP contém apenas números.
4. Faz uma requisição para a API ViaCEP.
5. Verifica se a API retornou erro.
6. Exibe CEP, UF, estado e bairro.

## Exemplo de uso

Entrada:

```txt
Insira o CEP: 01001000
```

Saída esperada:

```txt
- O CEP é: 01001-000, a UF é SP, o estado é São Paulo, e o bairro é Sé.
```

## Conceitos Praticados

- input()
- str
- len()
- strip()
- isnumeric()
- if/else
- from requests import get
- from json import loads
- leitura de dados JSON
- validação de entrada

## Melhorias Futuras

- Tratar erro de conexão com a internet.
- Permitir CEP com hífen, como 01001-000.
- Separar o código em funções.
- Criar testes automatizados.
- Salvar o resultado em arquivo.