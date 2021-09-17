"""
O método utilizado para ler dados de um arquivo é .read()
Exemplo: File1 = open("/resources/data/Example2.txt", "w")
Parâmetros utilizados: "w" = write "r" = read "a" append
File1.name = retorna uma string com o diretório do arquivo
File1.mode = visualiza o modo que o objeto está usando, o modo de atributo de dados
File1.close = Fecha o objeto de arquivo
File1.read = armazena os valores do arquivo em uma variável qualquer como uma string
File1.readlines() = produz cada linha como um elemento
File1.readline() = Lê a primeira linha do arquivo
Cada vez que você chamar o readline(), ele irá armazenar uma linha diferente na variável atribuída
Você pode imprimir o conteúdo do arquivo usando o print()
Usar a instrução With para abrir o arquivo é uma prática melhor porque fecha o arquivo automaticamente
Esta instrução fechará o arquivo no fim da identação

Loop para imprimir cada linha individualmente

with open("Example1.txt", "r") as File1:
    for line in File1:
        print(line)

Imprimindo os caracteres de uma string do texto
No exemplo, irá imprimir os 4 primeiros caracteres da primeira linha

with open("Example1.txt", "r") as File1:
    file_stuff = File1.readlines(4)
    print(file_stuff)
"""

import urllib.request

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN' \
      '-SkillsNetwork/labs/Module%204/data/example1.txt '
filename = 'Example1.txt'
urllib.request.urlretrieve(url, filename)

Example1 = "Example1.txt"
file1 = open(Example1, "r")
print(file1.name)
print(file1.mode)
print(file1.read())
file1.close()

with open(Example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)
file1.closed  # verifica se o arquivo está fechado

with open(Example1, "r") as file1:
    print(file1.read(4))  # imprime os 4 primeiros caracteres da string
file1.closed

with open(Example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))
file1.closed

with open(Example1, "r") as file1:
    print(file1.read(16))
    print(file1.read(5))
    print(file1.read(9))
file1.closed

with open(Example1, "r") as file1:
    print("First line: " + file1.readline())  # Concatenando um print com a primeira linha do arquivo
file1.closed

with open(Example1, "r") as file1:
    print(file1.readline(20))  # Se você definir uma quantidade de caracteres e ele exceder a quantidade da linha,
    # ele não passa para a próxima
    print(file1.read(20))  # Retorna os próximos 20 caracteres
file1.closed

# Usando o loop para imprimir as linhas

with open(Example1, "r") as file1:
    i = 0
    for line in file1:
        print("Iteration", str(i), ": ", line)
        i += 1

# Ler os arquivos e atribuir como uma lista
# Cada [i] representa uma linha diferente

with open(Example1, "r") as file1:
    FileasList = file1.readlines()
    print(FileasList[0])
    print(FileasList[1])
    print(FileasList[2])
