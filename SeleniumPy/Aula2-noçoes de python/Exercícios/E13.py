# Faça um programa que dada uma lista e um número inteiro, imprima a tabuada desse número

n = input('Qual número vc deseja saber a tabuada ?  ')
lista = [1,2,3,4,5,6,7,8,9,10]

n = float(n)

for valor in lista:
    x = valor * n
    x = str(x)
    x = x.split('.')
    inteiro, decimal = x
    
    if decimal != '0':
        print(f'{valor} X {n} = {inteiro}.{decimal}')
    else:
        print(f'{valor} X {n} = {inteiro}')

