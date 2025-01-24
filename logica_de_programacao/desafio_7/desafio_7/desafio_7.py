"""Soma todos os números inteiros entre 1 e 100"""

accumulator = 0

for iterator in range(100):
    accumulator += (iterator+1)

print('A soma dos números de 1 a 100 é ', accumulator)
