# Operadores lógicos
# OR

album_year = 1991

if album_year < 1980 or album_year > 1989:
    print("The Album was made in the 70's or 90's")
else:
    print("The Album was made in the 1980's")

# AND

if 1979 < album_year < 1990:  # ou album_year > 1979 and album_year < 1990:
    print("This Album was made in the 80's")
