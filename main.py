import pygame
import spaceship
import camera

print(pygame.__path__)
# screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# controls
KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275
KEY_ROTATE_RIGHT = pygame.K_d
KEY_ROTATE_LEFT = pygame.K_a

# setup pygame window and timer
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()
black_color = (0, 0, 0)
blue_color = (97, 159, 182)
green_color = (0, 255, 25)
camera = camera.Camera(None, SCREEN_WIDTH, SCREEN_HEIGHT)
pygame.mixer.init()
sound = pygame.mixer.Sound('sounds/win.wav')

# setup game components
#start spaceship on bottom in middle of window
hero_image_base = pygame.image.load('images/hero.png').convert_alpha()
my_spaceship = spaceship.Spaceship(0, 0)
my_spaceship.x = int(SCREEN_WIDTH / 2)
my_spaceship.y = SCREEN_HEIGHT * .9

# ball = spaceship.Spaceship(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2))
# ball_group = pygame.sprite.Group()
# ball_group.add(ball)

# player_group = pygame.sprite.Group()
# player_group.add(my_spaceship)
# set game_over boolean and start loop
game_over = False
key_pressed, pressed_up, pressed_down, pressed_right, pressed_left, pressed_rotate_left, pressed_rotate_right = False, False, False, False, False, False, False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == KEY_UP:
                pressed_up = True
            if event.key == KEY_DOWN:
                pressed_down = True
            if event.key == KEY_LEFT:
                pressed_left = True
            if event.key == KEY_RIGHT:
                pressed_right = True
            if event.key == KEY_ROTATE_RIGHT:
                pressed_rotate_right = True
            if event.key == KEY_ROTATE_LEFT:
                pressed_rotate_left = True
        if event.type == pygame.KEYUP:
            if event.key == KEY_UP:
                pressed_up = False
            if event.key == KEY_DOWN:
                pressed_down = False
            if event.key == KEY_LEFT:
                pressed_left = False
            if event.key == KEY_RIGHT:
                pressed_right = False
            if event.key == KEY_ROTATE_RIGHT:
                pressed_rotate_right = False
            if event.key == KEY_ROTATE_LEFT:
                pressed_rotate_left = False
        if event.type == pygame.QUIT:
            game_over = True
    # keep increasing speed as long as key is held
    if pressed_up:
        my_spaceship.move_forward()
    if pressed_down:
        my_spaceship.move_back()
    if pressed_right:
        my_spaceship.move_right()
    if pressed_left:
        my_spaceship.move_left()
    if pressed_rotate_right:
        my_spaceship.rotate(True)
    if pressed_rotate_left:
        my_spaceship.rotate(False)



    # Draw background
    screen.fill(blue_color)
    ground = pygame.Rect(0, SCREEN_HEIGHT * .9, SCREEN_WIDTH, SCREEN_HEIGHT * .1)
    pygame.draw.rect(screen, green_color, ground)
    # Draw spaceship
    hero_image_active = pygame.transform.rotate(hero_image_base, (my_spaceship.orientation))
    my_spaceship.update(SCREEN_WIDTH, SCREEN_HEIGHT * .9)
    camera.update(my_spaceship.rect)
    # Game display
    my_spaceship.render(screen)
    screen.blit(hero_image_active, (my_spaceship.x, my_spaceship.y))


    # update canvas in window
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
