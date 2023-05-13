"""
    sets.py
    Autor: Iago Magalhães
    Descrição:
        - Mostrar exemplos de como declarar sets em Python
"""
 # Declaração de um set
nome_do_set1 = {1, 2, 3, 4}
print(nome_do_set1)
print(type(nome_do_set1))

nome_do_set2 = set([1, 2, 3, 4])
print(nome_do_set2)
print(type(nome_do_set2))

# Adicionando, atualizando e removendo elementos dos Sets
meu_set = {1, 2, 3, 4, 1}

# Adicionando elementos
meu_set.add(2)
print("Adição", meu_set)

# Atualizando set
meu_set.update([3, 4, 5, 6])
print("Atualição", meu_set)

# Removendo elemento
meu_set.discard(2)
print("Remoção", meu_set)

# Operações matemáticas com Sets
meu_set = {1, 2, 3, 4, 1}
meu_set_2 = set([1, 2, 8, 9, 10])

# União
print("União")
print(meu_set | meu_set_2)
print(meu_set.union(meu_set_2))

# Interseção
print("Interseção")
print(meu_set & meu_set_2)
print(meu_set.intersection(meu_set_2))

# Diferença
print("Diferença")
print(meu_set - meu_set_2)
print(meu_set.difference(meu_set_2))

# Diferença Simétrica
print("Diferença Simétrica")
print(meu_set ^ meu_set_2)
print(meu_set.symmetric_difference(meu_set_2))