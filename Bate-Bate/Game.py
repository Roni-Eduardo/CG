import pygame
import sys
from MecMovimento import MovendoTexto # Importa o arquivo MecMovimento

class Game: # Controla a logica do jogo
    def __init__(self):
        pygame.init()
        self.largura = 800 # Tamanho da tela
        self.altura = 600 # Tamanho da tela
        self.tela = pygame.display.set_mode((self.largura, self.altura))# Tela 
        pygame.display.set_caption("Bate-Bate")
        self.clock = pygame.time.Clock() 
        self.MovendoTexto = MovendoTexto("Roni", 50, self.largura, self.altura)

    def run(self): # Chama a posição do texto e atualiza a tela se movimentando até realizar o exit
        rodando = True #
        while rodando: # Loop infinito
            for evento in pygame.event.get(): # Loop de eventos
                if evento.type == pygame.QUIT:
                    rodando = False

            self.MovendoTexto.move() # Move os objetos
            self.tela.fill((0, 0, 0))
            self.tela.blit(self.MovendoTexto.texto_surf, self.MovendoTexto.rect)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()