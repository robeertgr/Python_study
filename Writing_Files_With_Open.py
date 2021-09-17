# Utilizamos o método write() para escrever em um arquivo

# Escrever uma nova linha em um arquivo
exmp2 = 'Example2.txt'
with open(exmp2, "w") as writefile:
    writefile.write("This is line A")

with open(exmp2, "r") as testwritefile:
    print(testwritefile.read())

with open(exmp2, "w") as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")

with open(exmp2, "r") as testwritefile:
    print(testwritefile.read())

"""
Escrevendo uma lista no texto:
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
print(Lines)
"""

# Escrevendo uma string na lista do texto

Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
with open('Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)

with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

with open('Example2.txt', 'w') as writefile:
    writefile.write("Overwrite\n")
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

# Appending files - Podemos escrever em arquivos sem perder os dados já existentes usando o argumento 'a'

with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

"""
Há outros meios de manipular um arquivo
r+ = lê e escreve, não pode truncar o arquivo
w+ = escreve e lê, pode truncar os arquivos
a+ = appending e lê, criando novos arquivos se já não existir
"""

with open('Example2.txt', 'a+') as testwritefile:
    testwritefile.write("This is line E\n")
    print(testwritefile.read())

"""
.tell() = retorna a posição atual em bytes
.seek(offset, from) = muda a posição de bytes 'offset' respeitando o 'from'
"""
with open('Example2.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))

    data = testwritefile.read()
    if not data:  # retorna uma string vazia falsa
        print('Read nothing')
    else:
        print(testwritefile.read())

    testwritefile.seek(0, 0)  # move 0 bits do começo

    print("\nNew Location: {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if not data:
        print('Read nothing')
    else:
        print(data)

    print("Location after read: {}".format(testwritefile.tell()))

# Testando o r+

with open('Example2.txt', 'r+') as testwritefile:
    data = testwritefile.readlines()
    testwritefile.seek(0, 0)  # Escreve no começo do arquivo

    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Finished\n")
    testwritefile.truncate()
    testwritefile.seek(0, 0)
    print(testwritefile.read())

# Copiando um arquivo para outro

with open('Example2.txt', 'r') as readfile:
    with open('Example3.txt', 'w') as writefile:
        for line in readfile:
            writefile.write(line)

with open('Example3.txt', 'r') as testwritefile:
    print(testwritefile.read())
