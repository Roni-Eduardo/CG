import sys
import pygame

pygame.init()

#confuiguração da tela 
largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pygame")

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

tamanho_fonte = 50
fonte = pygame.font.SysFont(None, tamanho_fonte)

texto = fonte.render("Roni", True, BRANCO)
#texto_rect = texto.get_rect(center=(largura/2, altura/2))#centro
texto_rect = texto.get_rect(center=(50, 550))
#texto_rect = texto.get_rect(center=(largura/80, 25))
#texto_rect = texto.get_rect(right=(largura/4, altura/4))

#loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill(PRETO)
    tela.blit(texto, texto_rect)
    pygame.display.flip()

    











