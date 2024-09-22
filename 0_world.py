# Step 0: Setting Up Pygame and the Game Window

# Q. What is pygame? 
# A. Pygame is existing code to control the computer screen and keyboard.
# E. Comment out import line to see error message.
import pygame

# Q. Why do we initialize Pygame? 
# A. To ask the computer to set aside memory and display from other programs.
# E. Comment out pygame.init() to see error message.
pygame.init()

# Q. What is the different between display and terminal output?
# A. Display is a graphics window on the screen, terminal is text on the screen.
# Q. Why set up the game window?
# A. To create a window where the game will be displayed.
# E. Change dipslay width and height to half (400, 300)
screen = pygame.display.set_mode((800, 600))  # Width: 800, Height: 600

# Q. How to display a title on the program window?
# A. Use pygame fnction display.set_caption("Title")
# E. Change the window title
pygame.display.set_caption("Pico's Block Adventure")

# Q. What is the main game loop?
# A. A loop that runs the game until the player quits.
# E1. change running to True to see effect
# E2. change running to False to quit faster
# E3. change print message to see text in terminal
# E4. comment out flip to see effect on display window
while 1:
    print("Hello")
    pygame.display.flip()
    # Q. Why do we need to flip the display? 
    # A. To update the display with the new game state.

pygame.quit()
