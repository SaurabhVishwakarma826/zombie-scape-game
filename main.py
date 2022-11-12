import pygame
import random

screen_size = [600, 600]
screen = pygame.display.set_mode(screen_size)
score = 0
green = (0, 255, 0)
pygame.font.init()

def load(name):
    return pygame.image.load(name)


def display_score(score):
    font = pygame.font.SysFont('Comic Sans MS', 30)
    score_text = 'Score: ' + str(score)
    text = font.render(score_text, True, green)
    screen.blit(text, [20, 10])
    if score < -3000:
        display()


def display():
    font = pygame.font.SysFont('Comic Sans MS', 50)
    text = font.render("Game Over", True, green)
    screen.blit(text, [180, 300])


def get_rand_offset():
    return 100*random.randint(5, 15)


def set_s_position(idx, pos):
    global keep_alive
    global score
    if c_positions[idx] > 600:
        c_positions[idx] = 0 - get_rand_offset()
        score = score + 100
    else:
        c_positions[idx] += 5
    if score < -3400:
        keep_alive=False


background = load("backgound1.png")
chicken = load('chicken.png')
user = load('user.png')
zombis_1 = load("z_1.png")
zombis_2 = load("z_2.png")
zombis_3 = load("z_3.png")
zombis_4 = load("z_4.png")
zombis_5 = load("z_5.png")
zombis_6 = load("z_6.png")
user_x = 160
c_positions = [0-get_rand_offset(), 0-get_rand_offset(), 0-get_rand_offset(),0-get_rand_offset(),0-get_rand_offset(),0]

clock = pygame.time.Clock()
keep_alive=True

while keep_alive:
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and user_x < 520:
        user_x = user_x + 10
    elif keys[pygame.K_LEFT] and user_x > 0:
        user_x = user_x - 10

    set_s_position(0, 0)
    set_s_position(1, 100)
    set_s_position(2, 200)
    set_s_position(3, 300)
    set_s_position(4, 400)
    set_s_position(5, 500)

    screen.blit(background, [0, 0])
    screen.blit(zombis_1, [0, c_positions[0]])
    screen.blit(zombis_2, [100, c_positions[1]])
    screen.blit(zombis_3, [200, c_positions[2]])
    screen.blit(zombis_4, [300, c_positions[3]])
    screen.blit(zombis_5, [400, c_positions[4]])
    screen.blit(zombis_6, [500, c_positions[5]])

    display_score(score)
    screen.blit(user, [user_x, 500])

    if c_positions[0] > 500 and user_x < 85:
        print('crash 1', user_x)
        score = score - 50
    if c_positions[5] > 500 and user_x > 410:
        print('crash 6', user_x)
        score = score - 50
    if c_positions[1] > 500 and user_x > 10 and user_x < 180:
        print('crash 2', user_x)
        score = score - 50
    if c_positions[2] > 500 and user_x > 110 and user_x < 280:
        print('crash 3', user_x)
        score = score - 50
    if c_positions[3] > 500 and user_x > 210 and user_x < 380:
        print('crash 4', user_x)
        score = score - 50
    if c_positions[4] > 500 and user_x > 310 and user_x < 485:
        print('crash 5', user_x)
        score = score - 50
    pygame.display.update()
    clock.tick(60)
