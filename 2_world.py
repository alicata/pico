import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pico's Block Adventure")

# Define Pico's character
pico_color = (255, 0, 0)  # Red color for Pico
pico_x = 100
pico_y = 500
pico_width = 50
pico_height = 50
pico_speed = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys to move Pico left or right
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pico_x -= pico_speed
    if keys[pygame.K_RIGHT]:
        pico_x += pico_speed

    # Fill screen and draw Pico
    screen.fill((173, 216, 230))
    pygame.draw.rect(screen, pico_color, (pico_x, pico_y, pico_width, pico_height))  # Draw Pico as a red block
    pygame.display.flip()

pygame.quit()
