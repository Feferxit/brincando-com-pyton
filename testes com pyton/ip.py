import random

def par_ou_impar():
    print("Bem-vindo ao Jogo de Par ou Ímpar!")
    escolha = input("Você quer Par ou Ímpar? (P/I): ").strip().upper()
    while escolha not in ["P", "I"]:
        escolha = input("Opção inválida. Escolha Par (P) ou Ímpar (I): ").strip().upper()

    jogador_numero = int(input("Digite um número entre 0 e 10: "))
    computador_numero = random.randint(0, 10)
    soma = jogador_numero + computador_numero

    print(f"Você escolheu {jogador_numero}, o computador escolheu {computador_numero}. Soma: {soma}")
    if soma % 2 == 0:
        resultado = "P"
        print("A soma é Par!")
    else:
        resultado = "I"
        print("A soma é Ímpar!")

    if resultado == escolha:
        print("Parabéns! Você venceu!")
    else:
        print("Você perdeu! Tente novamente.")

par_ou_impar()
