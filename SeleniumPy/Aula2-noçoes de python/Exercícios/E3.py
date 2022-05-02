"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é
de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a
serem compradas e o preço total.
"""

import math

area = float(input('Heyyy, vc pinta como eu pinto ?? KKKK \n\n\n Falaaa pintor, qual é o tamanho da area(M²) q vamos pintar ?'))

lata_litros = 18 #uma lata tem 18 litros
lata_valor = float(80) # valor da lata

total_litros = area / 3 # valor total de litros utilizados

qt_latas = total_litros / lata_litros
qt_latas = math.ceil(qt_latas) 
valor = qt_latas * lata_valor

print(f'Você vai precisar de {qt_latas} lata que da R${valor}')