import pygame
import sys
from MecMovimento import MovendoTexto

class Game:
    def __init__(self):
        pygame.init()
        self.largura = 800
        self.altura = 600
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Bate-Bate")
        self.clock = pygame.time.Clock()
        self.MovendoTexto = MovendoTexto("Roni", 50, self.largura, self.altura)

    def run(self):
        rodando = True
        while rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False

            self.MovendoTexto.move()
            self.tela.fill((0, 0, 0))
            self.tela.blit(self.MovendoTexto.texto_surf, self.MovendoTexto.rect)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()