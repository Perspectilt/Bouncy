import pygame
import res
import physics

# Basic stuff
pygame.init()
screen = pygame.display.set_mode((1024, 768))
screen.fill((255, 255, 255))
pygame.display.set_caption('Bouncy')

# Create a ball and a container
ball_1 = res.Ball(screen, pos_x=500, pos_y=100, radius=50, mass=1)
container_1 = res.Container(screen, pos_x=0, pos_y=0, width=1024, height=768)

# Add the object and the boundaries to their respective global lists
objects = [ball_1]
boundaries = [container_1]

# Applying gravity to all objects
physics.apply_gravity(objects, 50)

running = True      # variable to store state of the loop

# Main loop
while running:
    # Handles the quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    # Runs the game physics
    physics.physics(objects, boundaries)            # Use log=True for debug output   |   Use limit=<no. of seconds> to limit the program to a certain amount of time
    
# Try to use the limit argument every time if you intend to use the debug_extract.py
