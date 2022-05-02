# faça um programa que com uma Função calcule a média de uma lista
#sum() and len() podem ajudar

#pegando 4 valores:
def pegando_valores ():
    i = 1
    lista = []
    
    while i < 5:
        valor = int(input(f'digite o valor {i}:  '))
        lista.append(valor)
        i += 1

    media(lista)

def media (valores):    
    media = sum(valores) / len(valores)
    print(f'A média é {media}')

pegando_valores()