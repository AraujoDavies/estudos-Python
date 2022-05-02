string = 'jeito um'
string = " jeito dois"

multilinhas = """
Outro 
Jeito 
de
string
"""

# print(multilinhas)

# Concatenando:
apresentacao = "Eu me chamo Davies, Prazer em conhecê-lo"
pergunta = 'Qual é o seu nome?'

#print(apresentacao + '. ' + pergunta)

print('Corrida de cavalos:')
print ('#' + ' '*20 + '🐎')
print ('#' + ' '*18 + '🐎')
print ('#' + ' '*30 + '🐎')
print ('#' + ' '*22 + '🐎')
print ('#' + ' '*25 + '🐎')
print ('#' + ' '*11 + '🐎')

#alguns métodos:
a = 'abracadabra'
a.count('a') # return 5
a.index('c') # return 4
a.partition('c') # return Tupla ('abra', 'c', 'adabra')
a.replace('a', 'c') # return cbrcccdcbrc
a.upper() # ABRACADABRA lower | capitalize
a.split('b') # return List ['a', 'racada', 'ra']

#dir('') retorna todas funções de strings