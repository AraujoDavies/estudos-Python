dicionario = {
    'chave': 'valor',
    'chave2': ['valor1', 'valor2']
}

pessoa = {
    'nome': 'Davies',
    'idade': 23,
    'atividades': {
        'natação': 'quarta',
        'futsal': 'quinta',
        'Trading': 'Todos os dias',
        'Estudos': 'Todos os dias'
    }
}

#nome
print(
    pessoa['nome']
)

#dia do futsal
print(
    pessoa['atividades']['futsal']
)