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

# Racket definition
racket_width = 10
racket_height = 60
ball_size = 14

# Racket speed
racket_player_1_dy = 5
racket_pc_dy = 5

# Initial ball speed
ball_speed_x = 3
ball_speed_y = 3

# Define winner
winner = ""

# Define control
control = False
running = True

# Font settings
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
    global pc_x, pc_y, player_1_x, player_1_y, ball_x, ball_y, pc_score, player_1_score

    # PC racket position
    pc_x = 10
    pc_y = height // 2 - racket_height // 2

    # Player racket position
    player_1_x = width - 20
    player_1_y = height // 2 - racket_height // 2

    # Ball position
    ball_x = width // 2 - ball_size // 2
    ball_y = height // 2 - ball_size // 2

    # Define the score
    player_1_score = 0
    pc_score = 0

def end_game():
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
        # Render end text
        screen.fill(BLACK)
        end_text = font.render(f"Winner: {winner}", True, WHITE)
        end_text_rect = end_text.get_rect(center=(width // 2, height // 2))
        screen.blit(end_text, end_text_rect)

        pygame.display.flip()

main_menu()
initial_position()

# Counter to adjust ball speed
speed_counter = 0

while running:
    if not control:
        end_game()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        # Moving the ball
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Collision rectangles
        ball_rect = pygame.Rect(ball_x, ball_y, ball_size, ball_size)
        racket_pc_rect = pygame.Rect(pc_x, pc_y, racket_width, racket_height)
        racket_player_1_rect = pygame.Rect(player_1_x, player_1_y, racket_width, racket_height)

        # Ball color
        ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Ball collision with PC and player racket
        if ball_rect.colliderect(racket_pc_rect) or ball_rect.colliderect(racket_player_1_rect):
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
            player_1_score += 1
            if player_1_score == 5:
                winner = "Player 1"
                end_game()

        if ball_x >= width - ball_size:
            ball_x = width // 2 - ball_size // 2
            ball_y = height // 2 - ball_size // 2
            ball_speed_x = -ball_speed_x
            pc_score += 1
            if pc_score == 5:
                winner = "PC"
                end_game()

        # Moving PC racket to follow the ball
        if pc_y + racket_height // 2 < ball_y:
            pc_y += racket_pc_dy
        elif pc_y + racket_height // 2 > ball_y:
            pc_y -= racket_pc_dy

        # Prevent PC racket from leaving the area
        if pc_y < 0:
            pc_y = 0
        elif pc_y > height - racket_height:
            pc_y = height - racket_height

        # Adjust ball speed over time
        speed_counter += 1
        if speed_counter == 300:  # Adjust the number of frames as needed
            ball_speed_x *= 1.2  # Increase speed by 20%
            ball_speed_y *= 1.2
            speed_counter = 0  # Reset the counter

        # Display score in the game
        score_font = pygame.font.Font(font_file, 16)
        score_text = score_font.render(f"Score PC: {pc_score}       Score Player_1: {player_1_score}", True, WHITE)
        score_rect = score_text.get_rect(center=(width // 2, 30))

        screen.blit(score_text, score_rect)

        # Assets (objects)
        pygame.draw.rect(screen, WHITE, (pc_x, pc_y, racket_width, racket_height))
        pygame.draw.rect(screen, WHITE, (player_1_x, player_1_y, racket_width, racket_height))
        pygame.draw.ellipse(screen, ball_color, (ball_x, ball_y, ball_size, ball_size))  # Ball color
        pygame.draw.aaline(screen, WHITE, (width // 2, 0), (width // 2, height))

        # Player 1 keyboard control
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_1_y > 0:
            player_1_y -= racket_player_1_dy
        if keys[pygame.K_DOWN] and player_1_y < height - racket_height:
            player_1_y += racket_player_1_dy

        pygame.display.flip()

        clock.tick(60)

pygame.quit()
sys.exit()
