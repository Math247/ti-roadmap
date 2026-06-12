# Manipulando texto
frase -> cadeia de caracteres -> string

dentro de cada mini espaço de memória tera uma letra, começando do 0. 

## Fatiamento
Pegar pedaços dela.
frase[9] -> [] -> identificador de lista -> ele pega o caracter 9. 
frase[9:13] -> pega 9, 10, 11 e 12 da cadeia. eh sempre um a menos no final. ele para de pegar no 13, mas não pega o 13. o ultimo valor n entra na contagem.

frase[9:21:2] -> começa no 9, para no 21 e pula 2 casas.

frase[:5] -> se n tem nada onde começa, ele começa do inicio.
frase[15:] -> se n tem nada no final, vai ate o final.
frase[9::3] -> vai começar no 9 e vai ate o final, e pula de 3 em 3

## Analise
len(frase) -> comprimento. qual o tamanho da frase.
frase.count('o') -> contar qtas vezes aparece o 'o' minusculo.
frase.coutr('o',0,13) -> entre o caracter 0 ao 12, ele ve qtas letras 'o' tem
frase.find('deo') -> Ele retorna em q momento começa o 'deo'. -> se n tiver 'deo' ele retorna -1.
'Curso' in frase -> Retorna True ou False.

## Transformação
frase.replace('Python', 'Android') -> Onde tiver 'Python', ele substitui por 'Android'.
frase.upper() -> Colocar tudo em letra maiúscula.
frase.lower() -> Colocar tudo em letra minúscula.
frase.capitalize() -> Joga tudo pra minúsculo, e so o primeiro carctere vai ficar maiúsculo
frase.title() -> Vai ver onde tem espaço, e o caractere seguinte fica em maiúsculo.
frase.strip() -> Remove os espaços do inicio e do fim da string. Os do meio ficam.
frase.rstrip() -> Só remove os da direita (ultimos espaços).
frase.lstrip() -> Só remove os da esquerda (os do inicio).

## Divisão
frase.split() -> divide a string considerando os espaços. cada uma das palavras fica numa lista. 

## Junção
'-'.join(frase) -> Gera uma string unica, e em vez de espaço, coloca um '-'.