# Faça um programa que receba uma data de nascimento em dias e imprima uma msg:
# voce Nasceu dia <dia> de <Mês> de <ano>
meses = ['Janeiro', 'Fevereiro', 'Março', "Abril", "Maio", "Junho", "Julho", "Agosto", 'Setembro', "Outubro", 'Novembro', "Dezembro"]

data = input('digite a data do seu nascimento separada por barras, ex (30/12/2001): \n')

dia, mes, ano = data.split('/')
 
if int(mes) > 0 and int(mes) < 13 and int(dia) > 0 and int(dia) < 32:
    mestxt = meses[int(mes) - 1]
    print(f"O cidadão nasceu dia {dia} de {mestxt} de {ano}.")