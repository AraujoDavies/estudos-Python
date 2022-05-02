# user input 3 preços e o software retorna o mais barato na tela

p1 = float(input('Preço do primeiro produto: '))
p2 = float(input('Preço do segundo produto: '))
p3 = float(input('Preço do terceiro produto: '))

if p1 <= p2 and p1 <= p3:
    print(f'O produto mais barato custa R${p1}')
elif p2 <= p3 and p2 <= p1:
    print(f'O produto mais barato custa R${p2}')
elif p3 <= p2 and p3 <= p1:
    print(f'O produto mais barato custa R${p3}')
else:
    print('Error!')