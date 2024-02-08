import pygame
import random
import sys
import os
from math import inf


pygame.init()
WIDTH, HEIGHT = size = 990, 645
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Змейка')
pygame.mixer.music.load('data/start_music.mp3')
pygame.mixer.music.play(-1)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Apple(pygame.sprite.Sprite):
    image = load_image('apple_for_snake.png')
    image_gold = load_image('golden_apple.png')

    def __init__(self, *group):
        super().__init__(*group)
        choice = random.choice([Apple.image, Apple.image_gold, Apple.image, Apple.image, Apple.image])
        if choice == Apple.image_gold:
            self.score_diff = 250
        else:
            self.score_diff = 100
        self.image = choice
        self.pos = [random.randrange(1, 65) * 15, random.randrange(1, 42) * 15]
        self.rect = self.image.get_rect(topleft=(self.pos[0], self.pos[1]))

    def make_apple(self):
        return self.pos

    def del_apples(self):
        all_sprites.remove(all_sprites)

    def get_score(self):
        return self.score_diff


class Snake:
    def __init__(self):
        self.head = [495, 285]
        self.body = [[495, 285], [480, 285], [465, 285]]
        self.flag = True
        self.apple_cords = 0, 0
        self.speed = Speed()

    def run_right(self):
        if self.flag:
            self.apple = Apple(all_sprites)
            self.apple_cords = self.apple.make_apple()
            self.flag = False
        self.head[0] += 15
        for el in self.body[1:]:
            if self.head[0] == el[0] and self.head[1] == el[1]:
                self.head = [495, 285]
                self.body = [[495, 285], [480, 285], [465, 285]]
                self.flag = True
                self.apple.del_apples()
                end_game(self.speed.ret_speed()[1])
                self.speed.del_speed()
                return True
        if self.head[0] == self.apple_cords[0] and self.head[1] == self.apple_cords[1]:
            self.apple.del_apples()
            self.speed.speed_up()
            self.apple = Apple(all_sprites)
            self.apple_cords = self.apple.make_apple()
            self.flag = False
            self.body.append([self.head[0], self.head[1]])
        if self.head[0] > 990:
            self.head = [495, 285]
            self.body = [[495, 285], [480, 285], [465, 285]]
            self.flag = True
            self.apple.del_apples()
            end_game(self.speed.ret_speed()[1])
            self.speed.del_speed()
            return True
        else:
            self.body.insert(0, list(self.head))
            for el in self.body:
                pygame.draw.rect(screen, (235, 0, 0), (el[0], el[1], 15, 15))
            del self.body[-1]
            return False

    def run_left(self):
        if self.flag:
            self.apple = Apple(all_sprites)
            self.apple_cords = self.apple.make_apple()
            self.flag = False
        self.head[0] -= 15
        for el in self.body[1:]:
            if self.head[0] == el[0] and self.head[1] == el[1]:
                self.head = [495, 285]
                self.body = [[495, 285], [480, 285], [465, 285]]
                self.flag = True
                self.apple.del_apples()
                end_game(self.speed.ret_speed()[1])
                self.speed.del_speed()
                return True
        if self.head[0] == self.apple_cords[0] and self.head[1] == self.apple_cords[1]:
            self.apple.del_apples()
            self.speed.speed_up()
            self.apple = Apple(all_sprites)
            self.apple_cords = self.apple.make_apple()
            self.flag = False
            self.body.append([self.head[0], self.head[1]])
        if self.head[0] < 0:
            self.head = [495, 285]
            self.body = [[495, 285], [480, 285], [465, 285]]
            self.flag = True
            self.apple.del_apples()
            end_game(self.speed.ret_speed()[1])
            self.speed.del_speed()
            return True
        else:
            self.body.insert(0, list(self.head))
            for el in self.body:
                pygame.draw.rect(screen, (235, 0, 0), (el[0], el[1], 15, 15))
            del self.body[-1]
            return False

    def run_down(self):
        if self.flag:
            self.apple = Apple(all_sprites)
            self.apple_cords = self.apple.make_apple()
            self.flag = False
        self.head[1] += 15
        for el in self.body[1:]:
            if self.head[0] == el[0] and self.head[1] == el[1]:
                self.head = [495, 285]
                self.body = [[495, 285], [480, 285], [465, 285]]
                self.flag = True
                self.apple.del_apples()
                end_game(self.speed.ret_speed()[1])
                self.speed.del_speed()
                return True
        if self.head[0] == self.apple_cords[0] and self.head[1] == self.apple_cords[1]:
            self.apple.del_apples()
            self.speed.speed_up()
            self.apple = Apple(all_sprites)
            self.apple_cords = self.apple.make_apple()
            self.flag = False
            self.body.append([self.head[0], self.head[1]])
        if self.head[1] > 645:
            self.head = [495, 285]
            self.body = [[495, 285], [480, 285], [465, 285]]
            self.flag = True
            self.apple.del_apples()
            end_game(self.speed.ret_speed()[1])
            self.speed.del_speed()
            return True
        else:
            self.body.insert(0, list(self.head))
            for el in self.body:
                pygame.draw.rect(screen, (235, 0, 0), (el[0], el[1], 15, 15))
            del self.body[-1]
            return False

    def run_up(self):
        if self.flag:
            self.apple = Apple(all_sprites)
            self.apple_cords = self.apple.make_apple()
            self.flag = False
        self.head[1] -= 15
        for el in self.body[1:]:
            if self.head[0] == el[0] and self.head[1] == el[1]:
                self.head = [495, 285]
                self.body = [[495, 285], [480, 285], [465, 285]]
                self.flag = True
                self.apple.del_apples()
                end_game(self.speed.ret_speed()[1])
                self.speed.del_speed()
                return True
        if self.head[1] < 0:
            self.head = [495, 285]
            self.body = [[495, 285], [480, 285], [465, 285]]
            self.flag = True
            self.apple.del_apples()
            end_game(self.speed.ret_speed()[1])
            self.speed.del_speed()
            return True
        else:
            self.body.insert(0, list(self.head))
            for el in self.body:
                pygame.draw.rect(screen, (235, 0, 0), (el[0], el[1], 15, 15))
            if self.head[0] == self.apple_cords[0] and self.head[1] == self.apple_cords[1]:
                self.apple.del_apples()
                self.speed.speed_up()
                self.apple = Apple(all_sprites)
                self.apple_cords = self.apple.make_apple()
                self.flag = False
                self.body.append([self.head[0], self.head[1]])
            else:
                del self.body[-1]
            return False

    def reject_game(self):
        self.head = [495, 285]
        self.body = [[495, 285], [480, 285], [465, 285]]
        self.flag = True
        self.speed.del_speed()
        self.apple.del_apples()
        won_game()

    def update_speed(self):
        return self.speed.ret_speed()

    def g_score(self):
        return self.apple.get_score()


def won_game():
    pygame.mixer.music.unload()
    pygame.mixer.music.load('data/win_sound.mp3')
    pygame.mixer.music.play(1)
    fon = pygame.transform.scale(load_image('snake_win.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    fon2 = pygame.transform.scale(load_image('won_text.png'), (600, 150))
    screen.blit(fon2, (200, 10))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    # for line in intro_text:
    #     string_rendered = font.render(line, 1, pygame.Color('black'))
    #     intro_rect = string_rendered.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    #     text_coord += 10
    #     intro_rect.top = text_coord
    #     text_coord += intro_rect.height
    #     screen.blit(string_rendered, intro_rect)

    while True:
        for e in pygame.event.get():
            keys = pygame.key.get_pressed()
            if e.type == pygame.QUIT:
                terminate()
            elif keys[pygame.K_SPACE]:
                pygame.draw.rect(screen, (225, 0, 0), (495, 285, 15, 15))
                start_screen()
                return
        pygame.display.flip()
        clock.tick(100)


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    pygame.mixer.music.unload()
    pygame.mixer.music.load('data/start_music.mp3')
    pygame.mixer.music.play(-1)
    fon = pygame.transform.scale(load_image('snake_fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    fon2 = pygame.transform.scale(load_image('fon2.gif'), (550, 150))
    screen.blit(fon2, (WIDTH // 4 - 20, HEIGHT // 2 - 70))
    fon3 = pygame.transform.scale(load_image('fon3.gif'), (450, 120))
    screen.blit(fon3, (280, -20))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    # for line in intro_text:
    #     string_rendered = font.render(line, 1, pygame.Color('black'))
    #     intro_rect = string_rendered.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    #     text_coord += 10
    #     intro_rect.top = text_coord
    #     text_coord += intro_rect.height
    #     screen.blit(string_rendered, intro_rect)

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                terminate()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                return True  # начинаем игру
        pygame.display.flip()
        clock.tick(100)


class Speed:
    def __init__(self):
        self.speed = 20
        self.score = 0

    def speed_up(self):
        self.speed += 1
        self.score += snake.g_score()

    def del_speed(self):
        self.speed = 20
        self.score = 0

    def ret_speed(self):
        return self.speed, self.score


def end_game(score):
    pygame.mixer.music.unload()
    pygame.mixer.music.load('data/death_sound.mp3')
    pygame.mixer.music.play(1)
    fon = pygame.transform.scale(load_image('dead_fon.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    fon2 = pygame.transform.scale(load_image('dead_text.png'), (600, 150))
    screen.blit(fon2, (220, 250))
    font = pygame.font.Font('data/шрифт.ttf', 30)
    intro_text = [f"Your score: {score}"]
    text_coord = 550
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        text_coord += 10
        intro_rect.top = text_coord
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for e in pygame.event.get():
            keys = pygame.key.get_pressed()
            if e.type == pygame.QUIT:
                terminate()
            elif keys[pygame.K_SPACE]:
                pygame.draw.rect(screen, (235, 0, 0), (495, 285, 15, 15))
                start_screen()
                return
        pygame.display.flip()
        clock.tick(100)


all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
start_screen()
running = True
right = False
left = False
down = False
up = False
do = True
END = False
# TIMEREVENT = pygame.USEREVENT + 1
# pygame.time.set_timer(TIMEREVENT, 5000)
font2 = pygame.font.Font('data/шрифт.ttf', 30)
score = font2.render('Score: ', 1, pygame.Color('white'))
snake = Snake()
grass = load_image('grass2.png')
while running:
    screen.blit(grass, (0, 0))
    speed = snake.update_speed()[0]
    if snake.update_speed()[1] >= 2000:
        do = True
        up = False
        down = False
        left = False
        right = False
        snake.reject_game()
    score = font2.render(f'Score: {snake.update_speed()[1]}', 1, pygame.Color('white'))
    if not (down or up or right or left):
        apples_cords = []
        pygame.draw.rect(screen, (235, 0, 0), (495, 285, 45, 15))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        # if event.type == TIMEREVENT and not do:
        #     cds = Apple().make_apple()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and (down or up or do):
            do = False
            up = False
            down = False
            left = False
            right = True
        if keys[pygame.K_LEFT] and (down or up):
            do = False
            up = False
            down = False
            left = True
            right = False
        if keys[pygame.K_DOWN] and (right or left or do):
            do = False
            up = False
            down = True
            left = False
            right = False
        if keys[pygame.K_UP] and (right or left or do):
            do = False
            up = True
            down = False
            left = False
            right = False
    if right:
        if snake.run_right():
            right = False
            do = True
    if left:
        if snake.run_left():
            left = False
            do = True
    if up:
        if snake.run_up():
            up = False
            do = True
    if down:
        if snake.run_down():
            down = False
            do = True
    screen.blit(score, (0, 0))
    all_sprites.draw(screen)
    clock.tick(speed)
    pygame.display.flip()
pygame.quit()
