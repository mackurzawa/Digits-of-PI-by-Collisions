import pygame
import Constants


class Block:
    def __init__(self, x, y, m, v, l):
        self.x = x
        self.y = y
        self.m = m
        self.v = v
        self.l = l

    def draw(self, screen):
        pygame.draw.rect(screen, Constants.square_c, pygame.Rect(self.x, self.y, self.l, self.l))

    def update(self):
        self.x += self.v

    def collide(self, block2):
        if block2.x < self.x + self.l:
            import main
            main.COLLISIONS += 1
            return True
        return False

    def wall(self):
        if self.x < 0:
            import main
            main.COLLISIONS += 1
            self.v *= -1
