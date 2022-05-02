conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

print(conjunto1)
#########################

nome_iguais = {'Davies', 'Davies'} # conjuntos nao aceita iguais

print(nome_iguais)

# Transformar uma lista em conjuntos é legal!!!
numeros = [1,1,1,1,1,1,1,2,3,3,4,4,4,4,45,5,5,5]

change = set(numeros)

print(change)
newList = list(change)
print(newList)


#funções
conjunto1.union({conjunto2}) # 1,2,3,4,5
conjunto1.difference(conjunto2) # 1, 2
conjunto1.intersection(conjunto2) # 3
conjunto1.update(conjunto2) #1,2,3,4,5
conjunto1.pop() #tira valores aleatorios pq a estrutura do conjunto é diferente
conjunto1.discard(1) # 2, 3
conjunto2.discard(1) # 4, 5