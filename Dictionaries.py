# Um dicionario é um tipo de coleção
# Possuem chaves e valores

# Criando um dicionario
# Para criar um dicionario, usamos chaves {}, as chaves são os primeiros elementos.
# As chaves devem ser imutáveis e únicos
# Cada chave é seguida por um valor separado por dois pontos
# exemplo: {"key1":1, "key2":"2", "key3":[3, 3, 3], "key4": (4, 4, 4), ('key5'):5}
# Cada par de chave e valor é separado por uma virgula

# Atribuindo uma variável ao dicionario

DICT = {"Thriller": 1982, "Back in Black": 1980, "The Dark Side of the Moon": 1973, "The Bodyguard": 1992,
        "Bat Out of Hell": 1977, "The Greatest...": 1976, "Saturday Night Fever": 1977,
        "Rumours": 1977}
print(DICT)

# A Chave é usada para pesquisar o valor. Usamos colchetes; o argumento é a chave, isso gera o valor
print(DICT["Thriller"])

# Para adicionar uma nova entrada ao dicionario, fazemos da seguinte forma:
# Isto irá adicionar a nova entrada no final do dicionário

DICT["Graduation"] = "2007"
print(DICT)

# Para deletar uma entrada, usamos o método del() chamando pela chave

del(DICT['Thriller'])
print(DICT)

# Para verificar se um elemento está no dicionário, usamos o comando in
# Se o elemento existir, retornará True, caso contrário retornará False

print("The Bodyguard" in DICT)

# Para imprimir todas as chaves de um dicionário, usamos o método keys()

print(DICT.keys())

# Para imprimir todos os valores do dicionário, usamos o método values()

print(DICT.values())
