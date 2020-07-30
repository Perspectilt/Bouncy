"""Module containing all materials"""
import pygame


class Ball:


    # Initial definition
    def __init__(self, surface, **kwargs):
        self.surface = surface
        self.radius = kwargs.get('radius')
        self.pos_x = kwargs.get('pos_x')
        self.pos_y = kwargs.get('pos_y')
        self.colour = kwargs.get('colour', (255, 0, 0))
        self.mass = kwargs.get('mass')
        self.type = 'object'

        self.create()

    # Creates the ball
    def create(self):
        self.ball = pygame.draw.circle(self.surface, self.colour, (self.pos_x, self.pos_y), self.radius)

    # Moves the ball
    def move(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.surface.fill((255, 255, 255))
        self.create()
        pygame.display.update()

    # Returns the ball's coordinates
    def pos(self):
        return self.pos_x, self.pos_y, self.pos_x + self.radius * 2, self.pos_y + self.radius * 2

    forces = []         # List storing all the forces


class Container:
    # Initial definition
    def __init__(self, surface, **kwargs):
        self.surface = surface
        self.width = kwargs.get('width')
        self.height = kwargs.get('height')
        self.pos_x = kwargs.get('pos_x')
        self.pos_y = kwargs.get('pos_y')
        self.type = 'boundary'

    # Returns the position of the ball
    def pos(self):
        x1 = self.pos_x
        x2 = self.pos_x + self.width
        y1 = self.pos_y
        y2 = self.pos_y + self.height

        return x1, y1, x2, y2

objects, boundaries = [], []
