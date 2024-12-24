def forca():
    palavra_secreta = "python"
    letras_descobertas = ["_"] * len(palavra_secreta)
    tentativas = 6

    print("Bem-vindo ao jogo da Forca!")
    while tentativas > 0 and "_" in letras_descobertas:
        print(" ".join(letras_descobertas))
        letra = input("Digite uma letra: ").lower()

        if letra in palavra_secreta:
            for i, l in enumerate(palavra_secreta):
                if l == letra:
                    letras_descobertas[i] = letra
        else:
            tentativas -= 1
            print(f"Errado! Você tem {tentativas} tentativas restantes.")

    if "_" not in letras_descobertas:
        print(f"Parabéns! Você adivinhou a palavra: {palavra_secreta}")
    else:
        print(f"Você perdeu! A palavra era: {palavra_secreta}")

forca()
