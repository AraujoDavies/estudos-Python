# faça um programa que dada a entrada de uma lista ele faça o cálculo acumulativo da mesma
# exemplo de entrada: [1, 2, 3, 4]
# exemplo de saída: [1, 3, 6, 10]

lista1= []
lista2 = []
ns = 1

while ns != 0:
    ns = int(input('Insira um valor na lista: '))
    lista1.append(ns)
    
    if len(lista2) > 0:
        x = ns + lista2[-1] 
        lista2.append(x)
    else:
        x = ns 
        lista2.append(x)

lista1.pop()
lista2.pop()

print(lista1)
print(lista2)