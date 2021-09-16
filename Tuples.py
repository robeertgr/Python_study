# Uma tupla é imutável, ou seja, não se pode alterar o seu conteúdo
# Uma tupla pode conter outras tuplas, bem como outros tipos de dados complexos
# isto é chamado de aninhamento (nesting)
Ratings = (10, 9, 6, 5, 10, 8, 9, 6, 2)
print(len(Ratings))
print(Ratings)

print(Ratings[0])

Tuple1 = ("disco", 10, 1.2)
Tuple2 = Tuple1 + ("hard rock", 10)
print(Tuple2)
print(Tuple2[0:3])

# RatingsSorted = sorted(Ratings)

C_tuple = (-5, 1, -3)
C_list = sorted(C_tuple)
print(C_list)

# Nesting (aninhamento)
# Uma tupla pode ser enxergada como uma árvore

NT = (1, 2, ("pop", 'rock'), (3, 4), ("disco", (1, 2)))
print(NT[2])
print(NT[2][1])
print(NT[2][1][0])




