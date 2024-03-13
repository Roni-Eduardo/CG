import sys
import pygame
import random

pygame.init()

#confuiguração da tela 
largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pygame")

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
COR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AMARELO = (255, 255, 0)

tamanho_fonte = 50
fonte = pygame.font.SysFont(None, tamanho_fonte)

texto = fonte.render("Roni", True, BRANCO)

texto_rect = texto.get_rect(center=(largura/2, altura/2))#centro
clock = pygame.time.Clock()

#texto_rect = texto.get_rect() #canto-superior-esquerdo
#texto_rect.left = 450
#texto_rect.right = 800
#texto_rect.top = 0
#texto_rect.bottom = 150

#velocidade_x = 1
#velocidade_y = 1

velocidade_x = random.randint(-1, 1)
velocidade_y = random.randint(-1, 1)

while velocidade_x == 0:
    velocidade_x = random.randint(-1, 1)

while velocidade_y == 0:
    velocidade_y = random.randint(-1, 1)

velo_x = 0
velo_y = 0

red = 0
blue = 0
green = 0

#loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    texto_rect.x += velocidade_x      
    texto_rect.y += velocidade_y   

    if texto_rect.right >= largura:
        velocidade_x = random.randint(-1, 0)
        velocidade_y = random.randint(-1, 1)

        velo_x = velocidade_x
        velo_y = velocidade_y

        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue =  random.randint(0, 255)

        COR = (red, green, blue)
        texto = fonte.render("Roni", True, COR)

    if texto_rect.left <= 0: 
        velocidade_x = random.randint( 0, 1)
        velocidade_y = random.randint(-1, 1)

        velo_x = velocidade_x
        velo_y = velocidade_y

        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue =  random.randint(0, 255)

        COR = (red, green, blue)
        texto = fonte.render("Roni", True, COR)

    if texto_rect.bottom >= altura:
        velocidade_x = random.randint(-1, 1)
        velocidade_y = random.randint(-1, 0)

        velo_x = velocidade_x
        velo_y = velocidade_y

        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue =  random.randint(0, 255)

        COR = (red, green, blue)
        texto = fonte.render("Roni", True, COR)
    
    if texto_rect.top <= 0:
        velocidade_x = random.randint(-1, 1)
        velocidade_y = random.randint( 0, 1)

        velo_x = velocidade_x
        velo_y = velocidade_y

        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue =  random.randint(0, 255)

        COR = (red, green, blue)
        texto = fonte.render("Roni", True, COR)


    clock.tick(200)
    tela.fill(PRETO)
    tela.blit(texto, texto_rect)
    pygame.display.flip()