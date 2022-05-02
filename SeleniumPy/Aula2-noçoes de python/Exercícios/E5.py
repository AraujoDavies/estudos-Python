# Fazer media para verificar aluno aprovado ou reprovado

p1 = float(input("Nota na prova 1: "))
p2 = float(input("Nota na prova 2: "))
p3 = float(input("Nota na prova 3: "))

media = (p1 + p2 + p3) / 3

if media > 10 or media < 0:
    print('Notas atribuidas não correspondem ao valor de 1 a 10')
elif media == 10:
    print(f'UAUUUU Parabéns!!! - Sua média foi {media}')
elif media > 6:
    print(f'Aprovado - Sua média foi {media}')
else:
    print(f'reprovado - Sua média foi {media}')
