# Diferente das tuplas, as listas são mutáveis, ou seja, pode-se alterar seu conteúdo

L = ["Michael Jackson", 10.1, 1982]
print(L[0])

L1 = L + ["pop", 10]
print(L1)

# Para alterar uma lista, usamos o método extends

L.extend(["pop", 10])
print(L)

# Para adicionar um elemento à lista, usamos o método append

L.append("A")
print(L)

# Para alterar um elemento da lista, basta adicionar o numero do seu índice e digitar o novo conteúdo

L[3] = "Rock"
print(L)

# Para remover um elemento da lista, usamos o método del e o índice do elemento

del(L[0])
print(L)

# Para converter uma string em uma lista, usamos o método split()
# O split converte cada grupo de caracteres separados por um espaço em um elemento de uma lista
# Podemos usar a função de divisão para separar strings em um caractere específico, conhecido como delimitador
# O resultado é uma lista, cada elemento corresponde a um conjunto de caracteres separados por vírgula

print("A,B,C,D".split(","))

# Para clonar uma lista, usamos a sintaxe [:]

A = ["hard rock", 10, 1.2]
B = A[:]
A[0] = "Banana"
print(A, B)

# Para mais dúvidas, use o comando help() passando como argumento a lista, tupla ou qualquer outro objeto

B = ["a", "b", "c"]
B[0] = "A"
print(B)
print(B[1:])
