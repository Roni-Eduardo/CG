import pygame
from pygame import mixer
import sys
import random

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

# Paddle definition
paddle_width = 10
paddle_height = 60
ball_size = 14

# Paddle speed
player_paddle_dy = 5
computer_paddle_dy = 5

# Initial ball speed
ball_speed_x = 3
ball_speed_y = 3

# Winner definition
winner = ""

# Control definition
control = False
running = True

# Font configuration
font_file = "font/PressStart2P-Regular.ttf"
font = pygame.font.Font(font_file, 36)

# Define sounds
mixer.music.load("audios/game.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.5)
sound = mixer.Sound("audios/Sound_A.wav")

clock = pygame.time.Clock()

def main_menu():
    global running, control
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    control = True
                    return
        # Render menu text
        screen.fill(BLACK)
        menu_text = font.render("Pong", True, WHITE)
        menu_text_rect = menu_text.get_rect(center=(width // 2, height // 2))
        screen.blit(menu_text, menu_text_rect)

        time = pygame.time.get_ticks()
        # Press Space to play
        if time % 2000 < 1000:
            start_text = font.render("Press Space", True, WHITE)
            start_text_rect = start_text.get_rect(center=(width // 2, 450))
            screen.blit(start_text, start_text_rect)

        clock.tick(1)
        pygame.display.flip()

def initial_position():
    global computer_x, computer_y, player_x, player_y, ball_x, ball_y, ball2_x, ball2_y, score_computer, score_player

    # Computer paddle position
    computer_x = 10
    computer_y = height // 2 - paddle_height // 2

    # Player paddle position
    player_x = width - 20
    player_y = height // 2 - paddle_height // 2

    # Ball position
    ball_x = width // 2 - ball_size // 2
    ball_y = height // 2 - ball_size // 2

    # Second ball position
    ball2_x = width // 2 + ball_size // 2
    ball2_y = height // 2 + ball_size // 2

    # Define score
    score_player = 0
    score_computer = 0

def game_over():
    global running, winner, control
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    control = True
                    initial_position()
                    return
        # Render game over text
        screen.fill(BLACK)
        game_over_text = font.render(f"Winner: {winner}", True, WHITE)
        game_over_text_rect = game_over_text.get_rect(center=(width // 2, height // 2))
        screen.blit(game_over_text, game_over_text_rect)

        pygame.display.flip()

main_menu()
initial_position()

# Counter to adjust ball speed
speed_counter = 0

while running:
    if not control:
        game_over()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        # Moving the ball
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        ball2_x += ball_speed_x * 1.5
        ball2_y -= ball_speed_y * 1.5

        # Collision rectangles
        ball_rect = pygame.Rect(ball_x, ball_y, ball_size, ball_size)
        ball2_rect = pygame.Rect(ball2_x, ball2_y, ball_size, ball_size)
        computer_paddle_rect = pygame.Rect(computer_x, computer_y, paddle_width, paddle_height)
        player_paddle_rect = pygame.Rect(player_x, player_y, paddle_width, paddle_height)

        # Ball colors
        ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Ball collision with computer and player paddles
        if ball_rect.colliderect(computer_paddle_rect) or ball_rect.colliderect(
            player_paddle_rect
        ) or ball2_rect.colliderect(computer_paddle_rect) or ball2_rect.colliderect(player_paddle_rect):
            sound.play()
            ball_speed_x = -ball_speed_x
            ball_speed_y += random.choice([-1, 1]) * random.uniform(0.5, 1.5)

        # Ball collision with screen borders
        if ball_y <= 0 or ball_y >= height - ball_size:
            ball_speed_y = -ball_speed_y
            ball_speed_x += random.choice([-1, 1]) * random.uniform(0.5, 1.5)

        # Reset ball position at the start of the game
        if ball_x <= 0:
            ball_x = width // 2 - ball_size // 2
            ball_y = height // 2 - ball_size // 2
            ball_speed_x = -ball_speed_x
            score_player += 1
            if score_player == 5:
                winner = "Player 1"
                game_over()

        if ball2_x <= 0:
            ball2_x = width // 2 - ball_size // 2
            ball2_y = height // 2 - ball_size // 2
            ball_speed_x = -ball_speed_x
            score_player += 1
            if score_player == 5:
                winner = "Player 1"
                game_over()

        # Moving the second ball back inside the screen if it exits to the left
        if ball2_x <= 0:
            ball2_x = width // 2 - ball_size // 2
            ball2_y = height // 2 - ball_size // 2
            ball_speed_x = -ball_speed_x

        # Rendering the balls
        pygame.draw.ellipse(screen, ball_color, (ball_x, ball_y, ball_size, ball_size))
        pygame.draw.ellipse(screen, ball_color, (ball2_x, ball2_y, ball_size, ball_size))

        # Rendering the paddles
        pygame.draw.rect(screen, WHITE, (computer_x, computer_y, paddle_width, paddle_height))
        pygame.draw.rect(screen, WHITE, (player_x, player_y, paddle_width, paddle_height))

        # Moving the computer paddle to follow the ball
        if computer_y + paddle_height // 2 < ball_y:
            computer_y += computer_paddle_dy
        elif computer_y + paddle_height // 2 > ball_y:
            computer_y -= computer_paddle_dy

        # Prevent computer paddle from leaving the area
        if computer_y < 0:
            computer_y = 0
        elif computer_y > height - paddle_height:
            computer_y = height - paddle_height

        # Displaying the score
        score_font = pygame.font.Font(font_file, 16)
        score_text = score_font.render(
            f"Score Computer: {score_computer}       Score Player: {score_player}", True, WHITE
        )
        score_rect = score_text.get_rect(center=(width // 2, 30))
        screen.blit(score_text, score_rect)

        # Player paddle keyboard control
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_paddle_dy
        if keys[pygame.K_DOWN] and player_y < height - paddle_height:
            player_y += player_paddle_dy

        pygame.display.flip()
        clock.tick(60)

pygame.quit()
sys.exit()