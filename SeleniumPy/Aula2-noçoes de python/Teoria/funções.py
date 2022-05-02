lista1 = [1, 2, 4, 3]

def media_da_lista (lista_numeros):
    # sum = soma os valores da lista
    return print(sum(lista_numeros) / len(lista_numeros))

media_da_lista(lista1)

def termo_ferias (nome, cpf, rg):
    return print(f"""
    Termo de Férias

    Devido as circunstâncias o/a colaborador(a) {nome}, portador(a) do CPF: {cpf} e do RG: {rg}.
    
    Está apto a tirar 2 anos de Férias.

    ass. Diretora Geral
    """)

termo_ferias('Davies de Araujo', 123456789, 9876543210)