"""
É uma biblioteca usada para computação científica e possuí muitas funções úteis
Também é a base para pandas
"""

# Verificar o tipo do array

import numpy as np

a = np.array([0, 1, 2, 3, 4])
b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
c = np.array([20, 1, 2, 3, 4])
c[0] = 100
c[4] = 0

# Verificar o tipo do array

print(type(b))

# Verificar o tamanho do array

print(np.size)

# Numero de dimensões do array (ou classificação do array)

print(np.ndim)

# Indicando o tamanho do array em cada dimensão

print(np.shape)

# Selecionando um intervalo do array

print(c[1:4])

c[3:5] = 300, 400
print(c)

# Operações matemáticas com vetores

"""
u = np.array([1, 0])
v = np.array([0, 1])
z = u + v
print(z)
"""

u = np.array([1, 0])
v = np.array([0, 1])
z = []
for n, m in zip(u, v):
    z.append(n + m)
print(z)

for n, m in zip(u, v):
    z.append(n - m)
print(z)

"""
y = np.array([1, 2])
z = 2 * y
print(z)
"""

y = [1, 2]
z = []
for n in y:
    z.append(2 * n)
print(z)

"""
u = np.array([1, 2])
v = np.array([3, 2])
z = u * v
print(z)
"""

u = np.array([1, 2])
v = np.array([3, 2])
z = []
for n, m in zip(u, v):
    z.append(n * m)
print(z)

# Multiplica um vetor pelo outro e depois soma os dois

u = np.array([1, 2])
v = np.array([3, 1])
result = np.dot(u, v)
print(result)

# Adicionando constante em um array numpy

u = np.array([1, 2, 3, -1])
z = u + 1
print(z)
