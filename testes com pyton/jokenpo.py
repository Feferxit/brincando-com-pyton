import random

def pedra_papel_tesoura():
    opcoes = ["pedra", "papel", "tesoura"]
    computador = random.choice(opcoes)

    print("Escolha: pedra, papel ou tesoura")
    jogador = input("Sua escolha: ").lower()

    print(f"Computador escolheu: {computador}")
    if jogador == computador:
        print("Empate!")
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "tesoura" and computador == "papel") or \
         (jogador == "papel" and computador == "pedra"):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

pedra_papel_tesoura()
