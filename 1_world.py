# Step 1: Setting Up Pygame and the Game Window


import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))  # Width: 800, Height: 600
pygame.display.set_caption("Pico's Block Adventure")

# Main game loop: runs until player quits
running = True
while running:
    # Check for events from the gamer (keyboard, mouse, etc.)
    for event in pygame.event.get():
        # If player clicks the X in the top corner, quit the game
        if event.type == pygame.QUIT:
            running = False

    screen.fill((173, 216, 230))  # Fill screen with light blue color
    pygame.display.flip()  # Update the display

pygame.quit()
