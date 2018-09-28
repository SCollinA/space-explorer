import pygame

class Spaceship:
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
            self.speed_x = -5
        if self.y + self.radius > height:
            self.speed_y = -5
        if self.x - self.radius < 0:
            self.speed_x = 5
        if self.y - self.radius < 0:
            self.speed_y = 5


    def render(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)
