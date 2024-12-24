import pygame
import time
import random

pygame.init()

# Configuração da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game')

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Função principal
def jogo_da_cobrinha():
    x = largura / 2
    y = altura / 2
    velocidade = 10
    x_mudar = 0
    y_mudar = 0
    comprimento = 1
    corpo = []

    comida_x = round(random.randrange(0, largura - 10) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura - 10) / 10.0) * 10.0

    clock = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_mudar = -velocidade
                    y_mudar = 0
                elif evento.key == pygame.K_RIGHT:
                    x_mudar = velocidade
                    y_mudar = 0
                elif evento.key == pygame.K_UP:
                    y_mudar = -velocidade
                    x_mudar = 0
                elif evento.key == pygame.K_DOWN:
                    y_mudar = velocidade
                    x_mudar = 0

        x += x_mudar
        y += y_mudar

        tela.fill(preto)
        pygame.draw.rect(tela, verde, [comida_x, comida_y, 10, 10])

        corpo.append([x, y])
        if len(corpo) > comprimento:
            del corpo[0]

        for parte in corpo[:-1]:
            if parte == [x, y]:
                pygame.quit()
                quit()

        for parte in corpo:
            pygame.draw.rect(tela, branco, [parte[0], parte[1], 10, 10])

        pygame.display.update()

        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, largura - 10) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura - 10) / 10.0) * 10.0
            comprimento += 1

        clock.tick(15)

jogo_da_cobrinha()
