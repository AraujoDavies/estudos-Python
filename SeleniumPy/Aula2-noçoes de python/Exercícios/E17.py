# Faça um programa que calcule a Mediana de uma lista
#sorted() -> pode ajudar

i = 1
lista = []
while i < 5:
    valor = int(input(f'digite o valor {i}:  '))
    lista.append(valor)
    i += 1

ordenada = sorted(lista) # ordena a lista do menor para o maior

def mediana(lista_de_valores):
    par_ou_impar = len(lista_de_valores) % 2
    if par_ou_impar == 0:
        #code to executed if par
        i = (len(lista_de_valores) // 2)
        mediana = (lista_de_valores[i] + lista_de_valores[i-1]) / 2
        print(mediana)
    else: 
        #code to execute if impar
        mediana = (len(lista_de_valores) // 2)
        print(lista_de_valores[mediana])

mediana(ordenada)