# faça um programa que leia 5 numeros e informe o Maior

n1 = int(input('Digite o primeiro valor: \n'))
n2 = int(input('Digite o segundo valor: \n'))
n3 = int(input('Digite o terceiro valor: \n'))
n4 = int(input('Digite o quarto valor: \n'))
n5 = int(input('Digite o quinto valor: \n'))

numeros = [n1, n2, n3, n4, n5]

print(f"O maior número digitado foi o {max(numeros)}")
