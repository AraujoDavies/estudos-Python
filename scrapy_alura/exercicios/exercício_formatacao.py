string = 'O\ns@po\nn#o\tl@v@\to\npé'
#resultado que quero:
resultado = 'O sapo não lava o pé'

# o split() já entende que o \n e o \t são espaços :D
string = " ".join(string.split()).replace("@", "a").replace("#", "ã")

print(string)
if string == resultado:
    print('ok')
else:
    print('nao ok')

