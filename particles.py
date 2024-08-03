import pygame

class Particle:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.hue_value = color

    def show_sand(self, surface):
        color = pygame.Color(0)
        color.hsva = (self.hue_value, 100, 100)
        pygame.draw.rect(surface, color, (self.x * self.size, self.y * self.size, self.size, self.size))
