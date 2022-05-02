minha_lista_aleatoria = ['lasanha', 'churrasco', 'Japa', 150, [1,2,3], 'Violão' ]

#slice

# de onde : até onde : quanto em quanto

print(minha_lista_aleatoria[::2]) # lasanha, japa e lista[1,2,3]
print(minha_lista_aleatoria[3::]) # 150, [1,2,3], violao
print(minha_lista_aleatoria[:-3:]) # Lasanha, churrasco e japa

print(minha_lista_aleatoria[::-1]) # vem do ultimo até o primeiro
""" o -1 pode ser usado para fazer um nome ser escrito de trás para frente"""
dtpf = 'de trás pra frente'
print(dtpf[::-1]) # etnerf arp sárt ed