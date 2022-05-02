
def nome1 (argumento_posicional, *pacote_de_argumentos):
    print(argumento_posicional, pacote_de_argumentos)

nome1('pessoas', 'joaquim', 'antonho', 'Genival')

def nome2 (argumento_nomeado='se nao definir aparece isso', **pacote_nomeado):
    print(argumento_nomeado, pacote_nomeado)

nome2('x', palavras='paz, amor, união e sei lá')