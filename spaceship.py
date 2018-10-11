import pygame
from math import sin, pi, sqrt

class Block(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite().__init__(self)
        self.image = pygame.Surface([20, 20])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()

        self.rect.center = pos

class Spaceship(Block):
    BOUNCE_LOSS = 1.5
    AIR_FRICTION = 1.125
    
    def __init__(self, x, y):
        # set coordinates
        self.x = x
        self.y = y
        # set rate of change of coordinates (i.e. speed)
        self.speed_x = 0
        # set y speed equal to gravity
        self.speed_y = 0
        # set size of spaceship
        self.radius = 10
        self.orientation = 0
        self.gravity = 1

    def update(self, width, height):
        self.gravity = abs(self.y) / height
        self.speed_y += self.gravity
        # bounce off of bounds of window
        # if too far left or right
        if self.x + self.radius > width:
            self.x = width - self.radius
            self.speed_x = -self.speed_x / Spaceship.BOUNCE_LOSS
        if self.x - self.radius < 0:
            self.x = self.radius
            self.speed_x = -self.speed_x / Spaceship.BOUNCE_LOSS
        # if too high or low
        if self.y - self.radius < height * .1:
            self.y = self.radius + (height * .1)
            # self.speed_y = 0
        if self.y + self.radius > height:
            self.y = height - self.radius
            self.speed_y = -self.speed_y / Spaceship.BOUNCE_LOSS
            if self.speed_y <= 4 and self.speed_y >= -4:
                self.speed_y = 0
        self.speed_x = self.speed_x / Spaceship.AIR_FRICTION
        self.speed_y = self.speed_y / Spaceship.AIR_FRICTION
        self.x += self.speed_x
        self.y += self.speed_y

    def rotate(self, right):
        if right: #clockwise
            self.orientation -= 1
        else: # left, counterclockwise
            self.orientation += 1
        if self.orientation < -360:
            self.orientation += 360
        elif self.orientation > 0:
            self.orientation -= 360
        print("orientation %f" % self.orientation)

    def move(self, direction):
        orientation = abs(self.orientation) - 90 + direction
        if orientation % 90 == 0:
            orientation += 1
        if orientation > 360:
            orientation -= 360
        elif orientation < 0:
            orientation += 360
        print("orientation %f" % orientation)
        # convert to radians
        angle_b = 90
        angle_c = (180 - angle_b - orientation)
        orientation_radians = (orientation * pi) / 180
        angle_b_radians = (angle_b * pi) / 180
        angle_c_radians = (angle_c * pi) / 180
        # calculate +x and -y speed
        right_speed = sin(angle_c_radians) / sin(angle_b_radians)
        up_speed = sin(orientation_radians) / sin(angle_b_radians)
        print("up speed %f" % up_speed)
        print("right speed %f" % right_speed)
        self.speed_y += up_speed
        self.speed_x += right_speed

    def move_forward(self):
        self.move(0)

    def move_back(self):
        self.move(180)

    def move_right(self):
        self.move(90)

    def move_left(self):
        self.move(270)

    def render(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), self.radius)
