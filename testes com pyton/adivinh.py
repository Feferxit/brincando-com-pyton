import random

def adivinhe_o_numero():
    numero = random.randint(1, 100)
    while True:
        palpite = int(input("Adivinhe o número (1-100): "))
        if palpite == numero:
            print("Parabéns! Você acertou!")
            break
        elif palpite < numero:
            print("Muito baixo!")
        else:
            print("Muito alto!")

adivinhe_o_numero()
