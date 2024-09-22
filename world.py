import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pico's Block Adventure")

# Define Pico's character
pico_color = (255, 0, 0)
pico_x = 100
pico_y = 500
pico_width = 50
pico_height = 50
pico_speed = 5
pico_jump = False
pico_y_velocity = 0
gravity = 0.5

# Define wall
wall_color = (0, 0, 255)
wall_x = 400
wall_y = 500
wall_width = 50
wall_height = 50

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys to move Pico
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pico_x -= pico_speed
    if keys[pygame.K_RIGHT]:
        pico_x += pico_speed

    # Pico jumps if not already jumping
    if not pico_jump:
        if keys[pygame.K_SPACE]:
            pico_jump = True
            pico_y_velocity = -10  # Jump speed

    if pico_jump:
        pico_y_velocity += gravity  # Apply gravity
        pico_y += pico_y_velocity

        # Stop Pico when he lands
        if pico_y >= 500:
            pico_y = 500
            pico_jump = False

    # Check if Pico hits the wall
    if (pico_x + pico_width > wall_x) and (pico_x < wall_x + wall_width):
        pico_x = wall_x - pico_width if pico_x < wall_x else wall_x + wall_width

    # Fill screen, draw Pico and the wall
    screen.fill((173, 216, 230))
    pygame.draw.rect(screen, pico_color, (pico_x, pico_y, pico_width, pico_height))
    pygame.draw.rect(screen, wall_color, (wall_x, wall_y, wall_width, wall_height))
    pygame.display.flip()

pygame.quit()
