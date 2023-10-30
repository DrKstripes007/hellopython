import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BALL_SPEED = 5
PADDLE_SPEED = 10
FPS = 60

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Game variables
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = BALL_SPEED
ball_dy = BALL_SPEED

paddle1_x = 50
paddle1_y = HEIGHT // 2 - 50
paddle1_dy = 0

paddle2_x = WIDTH - 50
paddle2_y = HEIGHT // 2 - 50
paddle2_dy = 0

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1_dy = -PADDLE_SPEED
    elif keys[pygame.K_s]:
        paddle1_dy = PADDLE_SPEED
    else:
        paddle1_dy = 0

    if keys[pygame.K_UP]:
        paddle2_dy = -PADDLE_SPEED
    elif keys[pygame.K_DOWN]:
        paddle2_dy = PADDLE_SPEED
    else:
        paddle2_dy = 0

    # Update game logic here
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collisions with walls
    if ball_y <= 0 or ball_y >= HEIGHT:
        ball_dy *= -1

    # Ball collisions with paddles
    if (
        ball_x <= paddle1_x + 10
        and paddle1_y < ball_y < paddle1_y + 100
    ) or (
        ball_x >= paddle2_x - 10
        and paddle2_y < ball_y < paddle2_y + 100
    ):
        ball_dx *= -1

    # Ball out of bounds
    if ball_x <= 0 or ball_x >= WIDTH:
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_dx *= -1

    # Move paddles
    paddle1_y += paddle1_dy
    paddle2_y += paddle2_dy

    # Ensure paddles stay in bounds
    paddle1_y = max(0, min(paddle1_y, HEIGHT - 100))
    paddle2_y = max(0, min(paddle2_y, HEIGHT - 100))

    # Clear the screen
    screen.fill(WHITE)

    # Draw paddles and ball
    pygame.draw.rect(screen, (0, 0, 255), (paddle1_x, paddle1_y, 10, 100))
    pygame.draw.rect(screen, (255, 0, 0), (paddle2_x - 10, paddle2_y, 10, 100))
    pygame.draw.ellipse(screen, (0, 255, 0), (ball_x - 10, ball_y - 10, 20, 20))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
