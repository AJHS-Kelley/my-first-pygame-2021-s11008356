# Pygame Practice, William Case, 11/19/2021 8:47am, v1.0

import pygame, sys 
from pygame.locals import *

# start Pygame
pygame.init()

# Create game window
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Hello, world!")

# Set Color Values 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 252, 99)

# Setup Fonts
basicFont = pygame.font.SysFont(None, 48)

# Setup Text 
text = basicFont.render('Hello, world', True, YELLOW, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# Draw background onto window surface.
windowSurface.fill(YELLOW)

# draw a green polygon onto surface.
pygame.draw.polygon(windowSurface, GREEN, ((146, 0),(291, 106), (236, 277), (56, 277), (0,106)))

# Draw blue lines on the surface
pygame.draw.line(windowSurface, BLUE, (60, 60), (120,60), 4)
pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)

# Draw a circle
pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

# Draw an ellipse 
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

# Draw text background rectangle onto surface.
pygame.draw.rect(windowSurface, BLACK, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# Get a pixel array of the surface.
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = BLACK
del pixArray

# Draw the text onto the surface.
windowSurface.blit(text, textRect)

# Draw window onto the screen.
pygame.display.update()

# Run the game loop.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()