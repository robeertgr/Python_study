"""
Códigos de status
1xx = Informational
2xx = Success
200 = OK
3xx = Redirection
300 = Multiple Choices
4xx = Client Error
401 = Unauthorized
403 = Forbidden
404 = Not Found
"""
import os

import requests


url = 'https://www.ibm.com'
r = requests.get(url)
print(r.status_code)  # Retorna o status code
print(r.request.headers)  # Verifica os request headers
print("Request body: ", r.request.body)  # Verifica o request body

# Você pode ver a resposta do header do HTTP usando o atributo headers. Retorna um dicionario em Python
header = r.headers
print(r.headers)

# Obtendo a data de quando a requisição foi enviada usando a chave date
print(header['date'])

# Indicando o tipo de dado
print(header['Content-Type'])

# Para checar a codificação
print(r.encoding)

# Para verificar os 100 primeiros caracteres do texto mostrado no HTML
print(r.text[0:100])

# Pode carregar outros tipos de dados que não seja texto, por exemplo imagens
url = 'https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png'
r = requests.get(url)
print(r.headers)

path = os.path.join(os.getcwd(), 'image.png')
path

# Baixando uma nova imagem
with open(path, 'wb') as f:
    f.write(r.content)
