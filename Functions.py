# Funções recebem alguma entrada e em seguida produzem alguma saída ou alteração
# É um pedaço de código que você pode reutilizar
# Você pode implementar sua própria função, mas em muitos casos você usa as funções de outras pessoas

# Função Len - Retorna o tamanho de uma lista, set ou tupla.

album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5]
print(album_ratings)
L = len(album_ratings)
print(L)

# Função Sum - Soma todos os elementos

S = sum(album_ratings)
print(S)

# Função Sorted - Usado para classificar uma lista
# Retorna uma nova lista ou tupla classificada.

sorted_album_rating = sorted(album_ratings)
print(sorted_album_rating)

# Função Sort - Usado para classificar uma lista
# As classificações do album da lista serão alteradas e nenhuma nova lista será criada.

print(album_ratings)
album_ratings.sort()
print(album_ratings)


# Criando a propria função

def add1(a):
    b = a + 1
    return b


c = add1(10)
print(c)
d = add1(8)
print(d)


# ---------------------------------------------------------------
# Multiplos parâmetros


def Mult(a, b):
    x = a * b
    return x


print(Mult(2, 3))
print(Mult(2, "Michael Jackson "))


def MJ():
    print('Michael Jackson')


MJ()


# ---------------------------------------------------------------
# Usando loop na função


def printStuff(Stuff):
    for i, s in enumerate(Stuff):
        print("Album", i, "Rating is", s)


album_ratings = [10.9, 8.5, 9.5]
printStuff(album_ratings)

# ---------------------------------------------------------------


def Thriller():
    date = 1982
    return date


date = 2017
print(Thriller())
print(date)


# ---------------------------------------------------------------


def PinkFloyd():
    global ClaimedSales
    ClaimedSales = '45 million'
    return ClaimedSales


PinkFloyd()
print(ClaimedSales)
