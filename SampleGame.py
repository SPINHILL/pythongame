# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit change note 
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((0, 225, 0))
    for x in range(4):
        # Draw a solid blue circle in the center
        if (x == 0 ):
            #draw a red circle 
            pygame.draw.circle(screen, (255,0,0 ), (200+(x * 60), 200+(x * 75)), 75)
        elif (x == 1):
            #draw green circle
            pygame.draw.circle(screen, (0,255,0 ), (200+(x * 60), 200+(x * 75)), 75)
        elif (x == 2 ) :
            #draw blue circle
            pygame.draw.circle(screen, (0,0,255 ), (200+(x * 60), 200+(x * 75)), 75)
        else :
            #draw white circle
            pygame.draw.circle(screen, (255,255,255 ), (200+(x * 60), 200+(x * 75)), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
