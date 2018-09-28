import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 20])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()

        self.rect.center = pos

class Spaceship(Block):
    def __init__(self, x, y):
        # set coordinates
        self.x = x
        self.y = y
        # set rate of change of coordinates (i.e. speed)
        self.speed_x = 5
        self.speed_y = 5
        # set size of spaceship
        self.radius = 50

    def update(self, width, height):
        self.x += self.speed_x
        self.y += self.speed_y
        # bounce off of bounds of window
        if self.x + self.radius > width:
            self.speed_x = -self.speed_x
        if self.y + self.radius > height:
            self.speed_y = -self.speed_y
        if self.x - self.radius < 0:
            self.speed_x = -self.speed_x
        if self.y - self.radius < 0:
            self.speed_y = -self.speed_y


    def render(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)
