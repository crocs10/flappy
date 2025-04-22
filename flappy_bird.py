import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Flappy Bird")

# Set up colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Set up game clock
clock = pygame.time.Clock()

# Set up bird
bird_x = 50
bird_y = 250
bird_velocity = 0
gravity = 0.5
bird_jump = -10

# Set up pipe
pipe_width = 50
pipe_height = random.randint(150, 300)
pipe_x = 400
pipe_gap = 150

# Function to draw bird
def draw_bird(y):
    pygame.draw.circle(screen, BLACK, (bird_x, y), 20)

# Function to draw pipe
def draw_pipe(x, height):
    pygame.draw.rect(screen, GREEN, (x, 0, pipe_width, height))  # Top pipe
    pygame.draw.rect(screen, GREEN, (x, height + pipe_gap, pipe_width, 600))  # Bottom pipe

# Game loop
running = True
while running:
    screen.fill(WHITE)  # Fill screen with white background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = bird_jump  # Make bird jump

    # Bird movement
    bird_velocity += gravity
    bird_y += bird_velocity

    # Pipe movement
    pipe_x -= 5
    if pipe_x < -pipe_width:
        pipe_x = 400
        pipe_height = random.randint(150, 300)

    # Collision detection (bird hits the ground or the pipes)
    if bird_y > 580 or bird_y < 0:
        running = False  # End the game if bird hits the ground or sky

    # Draw bird and pipe
    draw_bird(bird_y)
    draw_pipe(pipe_x, pipe_height)

    pygame.display.update()  # Update display
    clock.tick(60)  # Set frame rate to 60 FPS

pygame.quit()
