import pygame

class Rect:

    x = 0
    y = 0
    w = 0
    h = 0

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def get_pygame_rect(self):
        return pygame.Rect([self.x, self.y], [self.w, self.h])
