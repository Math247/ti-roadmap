from requests import get
from json import loads
cep = str(input('Insira o CEP: ')).strip()
if len(cep) < 8 or len(cep) > 8:
    print('O cep precisa ter 8 digitos. Ex: 22222222')
else:
    strcep = 'cep'
    strcidade = 'uf'
    strestado = 'estado'
    strbairro = 'bairro'
    if cep.isnumeric():
        request = get('https://viacep.com.br/ws/'+cep+'/json/')
        response = loads(request.content)
        if 'erro' in response:
            print('CEP com erro.')
        else:
            print('O CEP é: {}, a UF é {}, o estado é {}, e o bairro é {}.'.format(response[strcep], response[strcidade], response[strestado], response[strbairro]))
    else:
        print('O CEP precisa conter apenas numeros. Ex: 22222222')