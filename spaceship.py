import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite().__init__(self)
        self.image = pygame.Surface([20, 20])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()

        self.rect.center = pos

class Spaceship(Block):
    GRAVITY = 1
    BOUNCE_LOSS = 1.5
    ROLLING_FRICTION = 1.0625
    
    def __init__(self, x, y):
        # set coordinates
        self.x = x
        self.y = y
        # set rate of change of coordinates (i.e. speed)
        self.speed_x = 0
        # set y speed equal to gravity
        self.speed_y = 0
        # set size of spaceship
        self.radius = 50

    def update(self, width, height):
        self.speed_y += Spaceship.GRAVITY
        # bounce off of bounds of window
        # if too far left or right
        if self.x + self.radius > width:
            self.x = width - self.radius
            self.speed_x = -self.speed_x / Spaceship.BOUNCE_LOSS
        if self.x - self.radius < 0:
            self.x = self.radius
            self.speed_x = -self.speed_x / Spaceship.BOUNCE_LOSS
        # if too high or low
        if self.y - self.radius < 0:
            self.y = self.radius
            self.speed_y = -self.speed_y
        if self.y + self.radius > height:
            self.y = height - self.radius
            self.speed_x = self.speed_x / Spaceship.ROLLING_FRICTION
            self.speed_y = -self.speed_y / Spaceship.BOUNCE_LOSS
            if self.speed_y <= 4 and self.speed_y >= -4:
                self.speed_y = 0
            print('speed %d' % self.speed_y)
        self.x += self.speed_x
        self.y += self.speed_y


    def render(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), self.radius)
