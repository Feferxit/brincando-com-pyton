def exibir_tabuleiro(tabuleiro):
    print("\n")
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---+---+---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---+---+---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print("\n")

def verificar_vitoria(tabuleiro, jogador):
    # Verifica linhas, colunas e diagonais
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]              # Diagonais
    ]
    for combinacao in combinacoes:
        if tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]] == jogador:
            return True
    return False

def jogo_da_velha():
    tabuleiro = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]  # Tabuleiro inicial
    jogador_atual = "X"  # O jogador X começa
    jogadas_restantes = 9

    print("Bem-vindo ao Jogo da Velha!")
    exibir_tabuleiro(tabuleiro)

    while jogadas_restantes > 0:
        try:
            # Solicitar jogada
            jogada = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")) - 1
            if tabuleiro[jogada] == "X" or tabuleiro[jogada] == "O":
                print("Essa posição já foi escolhida. Tente novamente.")
                continue

            # Realizar a jogada
            tabuleiro[jogada] = jogador_atual
            exibir_tabuleiro(tabuleiro)

            # Verificar se houve vitória
            if verificar_vitoria(tabuleiro, jogador_atual):
                print(f"Parabéns, jogador {jogador_atual}! Você venceu!")
                break

            # Trocar jogador
            jogador_atual = "O" if jogador_atual == "X" else "X"
            jogadas_restantes -= 1
        except (ValueError, IndexError):
            print("Entrada inválida. Por favor, escolha um número entre 1 e 9.")

    if jogadas_restantes == 0:
        print("Velha! O jogo terminou sem vencedores.")

jogo_da_velha()
