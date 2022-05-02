# Faça um programa que pegue a lista de entrada e retorne as combinações possiveis
# ex de entrada: [1, 2, 3, 4]
# ex de saida: [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]

lista1 = []
lista2 = []
c = 0

resposta = ''

while resposta != 'ok':
    resposta = input('digite um numero para lista: (ao finalizar[ok])   ')
    if resposta == 'ok':
        break
    else:
        lista1.append(int(resposta))

for i in lista1:
    for i2 in lista1:
        if i != i2:
            tmpList = [i, i2]
            if tmpList not in lista2:
                if tmpList[::-1] not in lista2:
                    lista2.append(tmpList)
    c += 1

if len(lista2) > 1:
    print(f"Ao todo temos {len(lista2)} combinações possíveis, sendo elas: \n{lista2}")
elif len(lista2) == 1:
    print(f"Uma combinação possível: \n{lista2}")
else:
    print('0 Combinações D:')