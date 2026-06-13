# Cores no terminal

codigo ANSI - escape sequence.

começa com contra barra

sempre q quer representar cor-> \033[<style;text;backgroud>m

## Codigos para estilo:
0 -> sem estilo
1 -> negrito
4 -> underline
7 -> negative

## Codigos para texto:
30 -> branco
31 -> vermelho
32 -> verde
33 -> amarelo
34 -> azul
35 -> roxo
36 -> ciano
37 -> cinza -> cor padrao

## Back
mesmas cores, mas de 40 ate 47

ex:

print('\033[7;33;44mOlá, Mundo!\033[m')