import pygame
import sys

pygame.init()

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

largura = 800
altura = 600

screen = pygame.display.set_mode((largura, altura))#tupla são listas não alteráveis (( ))
pygame.display.set_caption("Pong")

#Definição da Raquete
raquete_largura = 10
raquete_altura = 60
tamanho_bola = 15

#Posição da raquete
pc_x = 10 #- raquete_largura
pc_y = altura // 2 - raquete_altura // 2

#Posição da raquete de player
player_1_x = largura - 10 - raquete_largura
player_1_y = altura // 2 - raquete_altura // 2

#Posição da bola
bola_x = largura // 2
bola_y = altura // 2 - tamanho_bola // 2

raquete_player_1_dy = 5
raquete_player_dy = 5

clock = pygame.time.Clock()

rodando = True
while rodando:
    for event in pygame.event.get(): # Loop de eventos
        if event.type == pygame.QUIT:# quando o botão de fechar for pressionado
            rodando = False

    screen.fill(PRETO)

    pygame.draw.rect(screen, BRANCO, (pc_x, pc_y, raquete_largura, raquete_altura)) #desenha a raquete
    pygame.draw.ellipse(screen, BRANCO, (bola_x, bola_y, tamanho_bola, tamanho_bola)) #desenha a bola
    pygame.draw.rect(screen, BRANCO, (player_1_x, player_1_y, raquete_largura, raquete_altura))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and player_1_y > 0:
        player_1_y -= raquete_player_1_dy
    if keys[pygame.K_DOWN] and player_1_y < altura - raquete_altura:
        player_1_y += raquete_player_1_dy

    pygame.display.flip()# atualiza a tela

    clock.tick(120)

pygame.quit() # encerra o pygame
sys.exit() # encerra o sistema