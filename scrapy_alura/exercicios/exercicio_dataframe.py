import pandas as pd

card = {'value': 'R$ 1000',
'name': 'Fusca',
'motor': 'Motor 1.6',
'description': 'Ano 1963 - 455.286 km',
'location': 'Belo Horizonte - MG',
'items': ['Rádio', 'Buzina']}


#como criar um dataframe do card ? espera-se uma tabela com uma linha e 6 colunas

dataset = pd.DataFrame.from_dict(card, orient='index').T
dataset