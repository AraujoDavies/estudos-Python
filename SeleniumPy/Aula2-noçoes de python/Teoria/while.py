# While and Break

resposta = input("Bora tomar uma ?[s/n]  ")
i = 1

while resposta != "s":
    resposta = input("Bora vai ?[s/n]  ")
    i += 1
    if "chato" in resposta or "chata" in resposta:
        print ("Sorry!!")
        break
else:
    print (f"A{'e' * i}! Bora logo intaum!")
