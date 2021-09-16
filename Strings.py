# \n = pula linha
# \t = tab
# \\ = uma barra invertida (\)


name = "Michael Jackson"

print(name[0:4])  # imprime da variável 0 até a 4 da string
print(name[8:12])
print(name[::2])  # selecionamos cada segunda variável da string, tambem chamado de stride

# retornar o tamanho da string
print(len(name))

statement = name + " is the best"
print(statement)
print(3 * name)
name = name + " is the best"
print(name)

# imprimir em uppercase / lowercase
A = "Thriller is the sixth studio album"
B = A.upper()
print(B)
B = A.lower()
print(B)

# substituir uma palavra da string
A = "Michael Jackson is the best"
print(A)
B = A.replace("Michael", "Janet")
print(B)

nome = "Michael Jackson"
print(nome.find("el"))
print(nome.find("& * D"))
