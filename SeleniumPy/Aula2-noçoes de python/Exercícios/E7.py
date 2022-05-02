# Faça um programa que responde se uma frase tem vogais, se sim quais são ?

msg = "slc em!"
msg = msg.lower()
vogais = ["a", "e", "i", "o", "u"]

for el in msg:
    for vogal in vogais:
        if vogal == el:
            print(vogal.upper())