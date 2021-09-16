# Sets são um tipo de collection, isso significa que você pode adicionar diferentes tipos (int, string, float)
# Diferente de listas e tuplas, eles são desordenados, isso significa que seus elementos não possuem índice
# Sets podem ter apenas elementos unicos, isso significa que há apenas um elemento específico em um conjunto
# Resumindo: sets não repetem valores

# Criando um set

Set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(Set1)

# Converter uma lista em um set usando o type casting set()

album_list = ["Michael Jackson", "Thriller", "Thriller", 1982]
print(album_list)
album_set = set(album_list)
print(album_set)

# Operações
# Para adicionar um elemento no conjunto set, utilize o método add()

A = {"Thriller", "Back in Black", "AC/DC"}
A.add("NSYNC")
print(A)

# Para remover um elemento no conjunto set, utilize o metodo remove()

A.remove("NSYNC")
print(A)

# Para verificar se um elemento está no conjunto, utilize o comando in

print("AC/DC" in A)
print("NSYNC" in A)

# Operações matemáticas com conjuntos
# Intersecção de dois conjuntos usando & ou o método intersection()
# Todos os elementos que não estiverem nos dois conjuntos será excluído

album_set_1 = {"AC/DC", "Back in Black"}
album_set_2 = {"AC/DC", "Back in Black", "The dark side of the Moon"}
album_set_3 = album_set_1 & album_set_2
print(album_set_3)

# A união de dois conjuntos é o novo conjunto de elementos que contém todos os itens em ambos
# os conjuntos. Podemos encontrar a união dos conjuntos de albuns usando o método .union()
# excluindo apenas os elementos que se repetem

print(album_set_1.union(album_set_2))

# Para verificar se um conjunto é um subconjunto, utilize o método issubset()

print(album_set_3.issubset(album_set_1))
