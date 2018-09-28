import pygame
import spaceship

print(pygame.__path__)
# screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
blue_color = (97, 159, 182)

# controls
KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

# setup pygame window and timer
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()

# setup game components
#start spaceship on bottom in middle of window
spaceship = spaceship.Spaceship(0, 0)
spaceship.x = int(SCREEN_WIDTH / 2)
spaceship.y = SCREEN_HEIGHT - spaceship.radius

ball = spaceship.Spaceship(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2))
ball_group = pygame.sprite.Group()
ball_group.add(ball)

player_group = pygame.sprite.Group()
player_group.add(spaceship)
# set game_over boolean and start loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                if event.key == KEY_UP:
                    spaceship.speed_y -= 5
                elif event.key == KEY_DOWN:
                    spaceship.speed_y += 5
                elif event.key == KEY_LEFT:
                    spaceship.speed_x -= 5
                elif event.key == KEY_RIGHT:
                    spaceship.speed_x += 5
        if event.type == pygame.KEYUP:
                print('key down %r' % event.key)
        if event.type == pygame.QUIT:
            game_over = True

    spaceship.update(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Draw background
    screen.fill(blue_color)

    # Game display
    spaceship.render(screen)

    # update canvas in window
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
