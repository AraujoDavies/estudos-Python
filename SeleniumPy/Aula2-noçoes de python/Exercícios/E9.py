# Faça um Programa q só vai parar se valor entre 1 - 10

resposta = -1

while int(resposta) > 10 or int(resposta) < 0:
    print ('insira uma nota entre 0~10 \n')
    resposta = input("Digite uma nota: ")

print('nota registrada!')