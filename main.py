import pygame
import spaceship

# screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
blue_color = (97, 159, 182)

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
# set game_over boolean and start loop
game_over = False
while not game_over:
    for event in pygame.event.get():
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
