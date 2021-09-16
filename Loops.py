# range(3) = 0, 1, 2
# range(10, 15) = 10, 11, 12, 13, 14

# FOR

squares = ["red", "yellow", "green", 'purple', "blue"]
print(squares)

for i in range(0, 5):
    squares[i] = "white"
print(squares)

squares_2 = ["red", "yellow", "green"]
for squares_2 in squares_2:
    print(squares_2)

# Para enumerar, utilize o método enumerate()

squares_3 = ['red', 'yellow', 'green']
for i, squares_3 in enumerate(squares_3):
    print(squares_3)
    print(i)

# While
# Só é executado se uma condição for atendida

squares_4 = ['orange', 'orange', 'purple', 'blue']
newsquares = []
i = 0

print(squares_4)
while squares_4[i] == 'orange':
    newsquares.append(squares_4[i])
    i += 1
    print(newsquares)

# Quiz

#1
Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'Soul', 'Pop']
for Genre in Genres:
    print(Genre)

Squares = ['red', 'yellow', 'green', 'purple', 'blue']
for Square in Squares:
    print(Square)

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
Rating = PlayListRatings[0]
while i < len(PlayListRatings) and Rating >= 6:
    print(Rating)
    i += 1
