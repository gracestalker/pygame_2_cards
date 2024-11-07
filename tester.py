import pygame
import sys


# Initialize pygame
pygame.init()

# Screen dimensions and settings
screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Green Square")

# Define the square properties
square_color = (0, 255, 0)  # Green color
square_size = 10
square_x, square_y = screen_width // 2, screen_height // 2
speed = 5  # Speed of movement

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()




    # Keep the square inside the screen boundaries
    square_x = max(0, min(screen_width - square_size, square_x))
    square_y = max(0, min(screen_height - square_size, square_y))

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the green square
    pygame.draw.rect(screen, square_color, (square_x, square_y, square_size, square_size))

    # Update the display
    pygame.display.flip()

    # Control frame rate
    pygame.time.Clock().tick(30)
