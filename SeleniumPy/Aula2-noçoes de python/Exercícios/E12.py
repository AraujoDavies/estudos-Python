# Receba um Float e imprima a parte decimal dele na tela

while 1 > 0 :
    nmr = input('digite um número quebrado: ')

    if '.' in nmr:
        nmr = nmr.replace('.', ',')

    if ',' in nmr:
        print(nmr)
        break
    else:
        print('por favor né amigão... digite um numero separado por ponto ou vírgula')    
    
inteiro, decimal = nmr.split(',')

print(f"A parte decimal é {decimal}")