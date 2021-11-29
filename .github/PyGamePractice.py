# Pygame Practice, William Case, 11/19/2021 8:38am, v0.2

import pygame, sys 
from pygame.locals import *

# start Pygame
pygame.init()

# Create game window
windowsurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Hello, world!")

# Set Color Values 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)