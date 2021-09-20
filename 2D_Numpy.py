"""
import numpy as np

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
a = np.array(a)
print(a)

print(a.dtype)
print(a.ndim)
print(a.shape)
print(a.size)

A = np.array([[11, 12], [21, 22]])
B = np.array([[1, 0], [0, 1]])
C = A * B
print(C)

Z = np.dot(A, B)
print(Z)
"""

# Importando as bibliotecas

import numpy as np
import matplotlib.pyplot as plt

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
print(a)

# Fazendo um cast com o nampy array

A = np.array(a)
print(A)

# Obtendo o numero de dimensões

print(A.ndim)

# Obtendo o numero de shapes

print(A.shape)

# Obtendo o tamanho do array

print(A.size)

# Acessar o elemento da segunda linha e terceira coluna
print(A[1, 2])

# Acessando um intervalo dentro do array

print(A[0][0:2])
print(A[0:2, 2])

# Operações básicas

X = np.array([[1, 0], [0, 1]])
Y = np.array([[2, 1], [1, 2]])
Z = X + Y
print(Z)

Z = 2 * Y
print(Z)

Z = X * Y
print(Z)

# Multiplicar os arrays juntos

Z = np.dot(X, Y)
print(Z)

k = np.array([1, 1, 1, 1, 1])
j = k + 10
print(j)
