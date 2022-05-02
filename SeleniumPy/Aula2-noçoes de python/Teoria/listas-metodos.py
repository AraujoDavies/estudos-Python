lista_mercado = [] # digitar a variavel. ctrl+espaço mostra todos os métodos, brinque!
resposta = ''

while resposta != 'acabou':
    resposta = input("O que vamos comprar ?\n")
    lista_mercado.append(resposta) #adiciona item

lista_mercado.pop() # remove ultimo item, que no caso é 'acabou' 

print(lista_mercado)