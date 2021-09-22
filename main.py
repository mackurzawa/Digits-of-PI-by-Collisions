import pygame
import sys

import Block
import Constants

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode((Constants.screen_width, Constants.screen_height))

block1 = Block.Block(Constants.screen_width / 3, Constants.screen_height * 2/3 - Constants.square, Constants.m1, 0, Constants.square)
block2 = Block.Block(Constants.screen_width * 2/3, Constants.screen_height * 2/3 - 3*Constants.square, Constants.m2, -1/Constants.iterations, 3*Constants.square)

COLLISIONS = 0

while True:
    screen.fill((100, 100, 100))
    pygame.draw.aaline(screen, (0, 0, 0), (0, 2/3 * Constants.screen_height), (Constants.screen_width, 2/3 * Constants.screen_height))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    for i in range(Constants.iterations):
        if block1.collide(block2):
            m1 = block1.m
            m2 = block2.m
            block1.v, block2.v = (m1 - m2)/(m1 + m2)*block1.v + 2*m2/(m1 + m2)*block2.v, (m2 - m1)/(m1 + m2)*block2.v + 2*m1/(m1 + m2)*block1.v
        block1.wall()
        block1.update()
        block2.update()
    textsurface = myfont.render(str(COLLISIONS), False, (0, 0, 0))
    screen.blit(textsurface, (0, 0))
    block1.draw(screen)
    block2.draw(screen)

    pygame.display.flip()
