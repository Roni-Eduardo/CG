import pygame
from pygame import mixer
import sys

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

largura = 800
altura = 600

screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pong")

# Definição da Raquete
wide_racket = 10 #raquete_largura
racket_height = 60 #raquete_altura
ball_size = 10 #tamanho_bola

# Velocidade da raquete
raquete_player_1_dy = 5
raquete_pc_dy = 5

# velocidade da bola
velocidade_bola_x = 3
velocidade_bola_y = 3

# Definir Vencedor
vencedor = ""

# Definir controle
controle = False
rodando = True

# Configuração da fonte
font_file = "font/PressStart2P-Regular.ttf"
font = pygame.font.Font(font_file, 36)

#Definir sons
mixer.music.load("audios/music_game.mp3")

#denifir sons
mixer.music.load("audios/music_game.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.5)
som = mixer.Sound("audios/Sound_A.wav")

clock = pygame.time.Clock()


def menu_principal():
    global rodando, controle
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    controle = True
                    return
        # Renderiza o texto do menu
        screen.fill(BLACK)
        texto_menu = font.render("Pong", True, WHITE)
        text_menu_rect = texto_menu.get_rect(center=(largura // 2, altura // 2))
        screen.blit(texto_menu, text_menu_rect)

        tempo = pygame.time.get_ticks()
        print(tempo)
        # Pressione Space para jogar
        if tempo % 2000 < 1000:
            texto_iniciar = font.render("Pressione Espaço", True, WHITE)
            texto_iniciar_rect = texto_iniciar.get_rect(center=(largura // 2, 450))
            screen.blit(texto_iniciar, texto_iniciar_rect)

        clock.tick(1)
        pygame.display.flip()


def posicao_inicial():
    global pc_x, pc_y, player_1_x, player_1_y, bola_x, bola_y, score_pc, score_player_1

    # Posição da Raquete do pc
    pc_x = 10
    pc_y = altura // 2 - racket_height // 2

    # Posição da Raquete do player
    player_1_x = largura - 20
    player_1_y = altura // 2 - racket_height // 2

    # Posição da bola
    bola_x = largura // 2 - ball_size // 2
    bola_y = altura // 2 - ball_size // 2

    # Define o Score
    score_player_1 = 0
    score_pc = 0


def fim_jogo():
    global rodando, vencedor, controle
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    controle = True
                    posicao_inicial()

                    return
        # Renderiza o texto do menu
        screen.fill(BLACK)
        texto_fim = font.render(f"Vencedor: {vencedor}", True, WHITE)
        text_fim_rect = texto_fim.get_rect(center=(largura // 2, altura // 2))
        screen.blit(texto_fim, text_fim_rect)

        pygame.display.flip()


menu_principal()
posicao_inicial()

while rodando:
    if not controle:
        fim_jogo()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        screen.fill(BLACK)

        # Movendo a bola
        bola_x += velocidade_bola_x
        bola_y += velocidade_bola_y

        # Retângulos de Colisão
        bola_rect = pygame.Rect(bola_x, bola_y, ball_size, ball_size)
        raquete_pc_rect = pygame.Rect(pc_x, pc_y, wide_racket, racket_height)
        raquete_player_1_rect = pygame.Rect(
            player_1_x, player_1_y, wide_racket, racket_height
        )

        # Colisão da bola com a raquete do pc e a raquete do player
        if bola_rect.colliderect(raquete_pc_rect) or bola_rect.colliderect(
            raquete_player_1_rect
        ):
            som.play()
            velocidade_bola_x = -velocidade_bola_x

        # Colisão da bola com as bordas da tela
        if bola_y <= 0 or bola_y >= altura - ball_size:
            velocidade_bola_y = -velocidade_bola_y

        # Posicionar a bola no inicio do jogo
        if bola_x <= 0:
            bola_x = largura // 2 - ball_size // 2
            bola_y = altura // 2 - ball_size // 2
            velocidade_bola_x = -velocidade_bola_x
            score_player_1 += 1
            print(f"Score Player_1: {score_player_1}")
            if score_player_1 == 5:
                print("Player_1 ganhou!")
                vencedor = "Player 1"
                fim_jogo()

        if bola_x >= largura - ball_size:
            bola_x = largura // 2 - ball_size // 2
            bola_y = altura // 2 - ball_size // 2
            velocidade_bola_x = -velocidade_bola_x
            score_pc += 1
            print(f"Score PC: {score_pc}")
            if score_pc == 5:
                print("PC ganhou!")
                vencedor = "PC"
                fim_jogo()

        # Movendo a raquete do pc pra seguir a bola
        if pc_y + racket_height // 2 < bola_y:
            pc_y += raquete_pc_dy
        elif pc_y + racket_height // 2 > bola_y:
            pc_y -= raquete_pc_dy

        # Evitar que a raquete do pc saia da área
        if pc_y < 0:
            pc_y = 0
        elif pc_y > altura - racket_height:
            pc_y = altura - racket_height

        # Mostrando Score no jogo
        fonte_score = pygame.font.Font(font_file, 16)
        score_texto = fonte_score.render(
            f"Score PC: {score_pc}       Score Player_1: {score_player_1}", True, WHITE
        )
        score_rect = score_texto.get_rect(center=(largura // 2, 30))

        screen.blit(score_texto, score_rect)

        # assets (objetos)
        pygame.draw.rect(screen, WHITE, (pc_x, pc_y, wide_racket, racket_height))
        pygame.draw.rect(
            screen, WHITE, (player_1_x, player_1_y, wide_racket, racket_height)
        )
        pygame.draw.ellipse(
            screen, WHITE, (bola_x, bola_y, ball_size, ball_size)
        )
        pygame.draw.aaline(screen, WHITE, (largura // 2, 0), (largura // 2, altura))

        # Controle Teclado do Player_1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_1_y > 0:
            player_1_y -= raquete_player_1_dy
        if keys[pygame.K_DOWN] and player_1_y < altura - racket_height:
            player_1_y += raquete_player_1_dy

        pygame.display.flip()

        clock.tick(60)

# fim_jogo()
pygame.quit()
sys.exit()
