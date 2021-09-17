"""
importa a biblioteca pandas > import pandas as anyname
guarda o valor de file1.csv na variável > csv_path = 'file1.csv'
o método head() exibe as 5 primeiras linhas do arquivo > df.head()

df = pd.DataFrame({'a': [11, 21, 31], 'b': [21, 22, 23]})
print(df.head(3))

xlsx_path = 'file1.xlsx'
df = pd.read_excel(xlsx_path)
print(df.head())

songs = {'Album': ['Thriller', 'Back in Black', 'The Dark Side of the Moon',\
                   'The Bodyguard', 'Bat out of Hell'],
         'Released': [1982, 1980, 1973, 1992, 1977],
         'Length': ['00:42:19', '00:42:11', '00:42:49', '00:57:44', '00:46:33']}
songs_frame = pd.DataFrame(songs)
print(songs_frame)

df = pd.DataFrame({'a': [1, 2, 1], 'b': [1, 1, 1]})
print(df)
print(df['a'].unique())  # Imprime os valores únicos de uma tabela
print(df[df['a'] < 2])  # Imprime os valores das linhas onde a coluna A é menor que dois
"""

# Importando a biblioteca
import pandas as pd

# Lendo o dado de um arquivo CSV
csv_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204' \
           '/Datasets/TopSellingAlbums.csv '
df = pd.read_csv(csv_path)
print(df.head())

# Lendo os dados de um arquivo excel
xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204' \
           '/Datasets/TopSellingAlbums.xlsx'
df = pd.read_excel(xlsx_path)
print(df.head())  # Imprimindo as primeiras 5 linhas do dataframe

# Acessando a coluna Length e atribuindo em um dataframe X
x = df[['Length']]
print(x)

# Visualizando os dados e acessando-os

x = df['Length']
print(x)

# Pegando as colunas como um dataframe

x = type(df[['Artist']])
print(x)

# Acessando multiplas colunas

y = df[['Artist', 'Length', 'Genre']]
print(y)

# Acessando o valor da primeira linha e da primeira coluna

print(df.iloc[0, 0])

# Acessando o valor da secunda linha e da primeira coluna

print(df.iloc[1, 0])

# Acessando o valor da primeira linha e da terceira coluna

print(df.iloc[0, 2])

"""
Pode-se também acessar os valores das colunas usando os nomes
df.loc[0, 'Artist']
df.loc[1, 'Artist']
df.loc[0, 'Released']
df.loc[1, 'Released']

Pode-se também cortar a tabela pelo index e nome da coluna

df.iloc[0:2, 0:3]
df.iloc[0:2, 'Artist': 'Released']
"""