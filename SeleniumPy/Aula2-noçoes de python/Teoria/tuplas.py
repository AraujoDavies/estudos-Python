minha_tupla = ('Davies', 23, 0, 'tristeza', 'b.o')
#tuplas são imutáveis mas não são inuteis, pois são mais leves que listas e podemos empacotar/desempacotar

#empacotando... só da pra usar um * por vez
nome, idade, *coisas_que_nao_quero = minha_tupla #empacotei e coisas_q_nao_quero vira uma lista
nome , *numeros, sentimento, problema = minha_tupla
*tudo, bo = minha_tupla

print(nome, idade)
print(type(coisas_que_nao_quero))#list

# cruzando variaveis
nome, idade = idade, nome
print (nome) #23

def funcreturn():
    return 1, 2, 3 # tupla - mtas coisas no python retorna tupla :D e é bem facinho de usar :D