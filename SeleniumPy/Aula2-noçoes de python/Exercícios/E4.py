"""
Faça um programa que peça 2 números inteiros e um número float. Calcule e
mostre:

> O produto do dobro do primeiro com metade do segundo .
> A soma do triplo do primeiro com o terceiro.
> O terceiro elevado ao cubo.
"""

i1 = int(input('Digite um valor Int:'))
i2 = int(input('Digite um valor Int:'))
i3 = float(input('Digite um valor Float:'))

# O produto do dobro do primeiro com metade do segundo.
r1 = (2 * i1) * (i2 / 2)

# A soma do triplo do primeiro com o terceiro.
r2 = (i1 * 3) + i3

# O terceiro elevado ao cubo.
r3 = i3 ** 3

print(f'{r1} \n {r2} \n {r3.fixed(2)}')