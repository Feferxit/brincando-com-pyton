import random

def mastermind():
    palavras = ["casa", "bola", "cama", "vida", "luz"]
    palavra_secreta = random.choice(palavras)
    tentativas = 5

    print("Bem-vindo ao jogo de Mastermind! Tente adivinhar a palavra de 4 letras.")
    while tentativas > 0:
        palpite = input("Seu palpite: ").lower()
        if palpite == palavra_secreta:
            print("Parabéns! Você acertou!")
            return
        else:
            feedback = ["_" if palpite[i] != palavra_secreta[i] else palpite[i] for i in range(4)]
            print(f"Feedback: {' '.join(feedback)}")
            tentativas -= 1
            print(f"Tentativas restantes: {tentativas}")

    print(f"Você perdeu! A palavra era: {palavra_secreta}")

mastermind()
