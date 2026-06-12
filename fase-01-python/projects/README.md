# Projeto de Consulta CEP

## API utilizada:
ViaCEP. Site: https://viacep.com.br/

## Como foi implementado:
Primeiro foi retirados possiveis espaços no final e do começo que seriam inúteis. Após isso, verifiquei se o numero de caracteres da string é 8. Se for maior ou menor, não é um CEP.

Depois defini variaveis com as chaves do json da API, para colocar no print de forma mais legível.
Verifiquei se só continha números no CEP. Se sim, ele fazia a requisição para a API.
Utilizei o modulo request e json utilizando o from, pois só iria utilizar uma função, e isso economiza memória. 
Após isso, exibi o bairro, a UF, o CEP e o estado.