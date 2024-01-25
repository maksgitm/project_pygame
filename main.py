import pygame
import random
import sys
import os


pygame.init()
WIDTH, HEIGHT = size = 1000, 650
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Змейка')


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

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Apple.image
        self.pos = [random.randrange(1, 99) * 10, random.randrange(1, 64) * 10]
        self.rect = self.image.get_rect(topleft=(self.pos[0], self.pos[1]))

    def make_apple(self):
        return self.pos

    def del_apples(self):
        all_sprites.remove(all_sprites)


class Snake:
    def __init__(self):
        self.head = [500, 280]
        self.body = [[500, 280], [490, 280], [480, 280]]
        self.flag = True
        self.apple_cords = 0, 0
        self.speed = Speed()

    def run_right(self):
        if self.flag:
            self.apple_cords = Apple(all_sprites).make_apple()
            self.flag = False
        self.head[0] += 10
        for el in self.body[1:]:
            if self.head[0] == el[0] and self.head[1] == el[1]:
                self.head = [500, 280]
                self.body = [[500, 280], [490, 280], [480, 280]]
                self.flag = True
                self.speed.del_speed()
                Apple().del_apples()
                end_game()
                return True
        if self.head[0] == self.apple_cords[0] and self.head[1] == self.apple_cords[1]:
            print('TRUE')
            Apple().del_apples()
            self.apple_cords = Apple(all_sprites).make_apple()
            self.flag = False
            self.speed.speed_up()
            self.body.append([self.head[0], self.head[1]])
        if self.head[0] > 1000:
            self.head = [500, 280]
            self.body = [[500, 280], [490, 280], [480, 280]]
            self.flag = True
            self.speed.del_speed()
            Apple().del_apples()
            end_game()
            return True
        else:
            self.body.insert(0, list(self.head))
            for el in self.body:
                pygame.draw.rect(screen, pygame.Color('red'), (el[0], el[1], 10, 10))
            del self.body[-1]
            return False

    def run_left(self):
        if self.flag:
            self.apple_cords = Apple(all_sprites).make_apple()
            self.flag = False
        self.head[0] -= 10
        for el in self.body[1:]:
            if self.head[0] == el[0] and self.head[1] == el[1]:
                self.head = [500, 280]
                self.body = [[500, 280], [490, 280], [480, 280]]
                self.flag = True
                self.speed.del_speed()
                Apple().del_apples()
                end_game()
                return True
        if self.head[0] == self.apple_cords[0] and self.head[1] == self.apple_cords[1]:
            print('TRUE')
            Apple().del_apples()
            self.apple_cords = Apple(all_sprites).make_apple()
            self.body.append([self.head[0], self.head[1]])
            self.flag = False
            self.speed.speed_up()
        if self.head[0] < 0:
            self.head = [500, 280]
            self.body = [[500, 280], [490, 280], [480, 280]]
            self.flag = True
            self.speed.del_speed()
            Apple().del_apples()
            end_game()
            return True
        else:
            self.body.insert(0, list(self.head))
            for el in self.body:
                pygame.draw.rect(screen, pygame.Color('red'), (el[0], el[1], 10, 10))
            del self.body[-1]
            return False

    def run_down(self):
        if self.flag:
            self.apple_cords = Apple(all_sprites).make_apple()
            self.flag = False
        self.head[1] += 10
        for el in self.body[1:]:
            if self.head[0] == el[0] and self.head[1] == el[1]:
                self.head = [500, 280]
                self.body = [[500, 280], [490, 280], [480, 280]]
                self.flag = True
                self.speed.del_speed()
                Apple().del_apples()
                end_game()
                return True
        if self.head[0] == self.apple_cords[0] and self.head[1] == self.apple_cords[1]:
            print('TRUE')
            Apple().del_apples()
            self.apple_cords = Apple(all_sprites).make_apple()
            self.body.append([self.head[0], self.head[1]])
            self.speed.speed_up()
            print(self.speed.ret_speed())
            self.flag = False
            self.speed.speed_up()
        if self.head[1] > 650:
            self.head = [500, 280]
            self.body = [[500, 280], [490, 280], [480, 280]]
            self.flag = True
            self.speed.del_speed()
            Apple().del_apples()
            end_game()
            return True
        else:
            self.body.insert(0, list(self.head))
            for el in self.body:
                pygame.draw.rect(screen, pygame.Color('red'), (el[0], el[1], 10, 10))
            del self.body[-1]
            return False

    def run_up(self):
        if self.flag:
            self.apple_cords = Apple(all_sprites).make_apple()
            self.flag = False
        self.head[1] -= 10
        for el in self.body[1:]:
            if self.head[0] == el[0] and self.head[1] == el[1]:
                self.head = [500, 280]
                self.body = [[500, 280], [490, 280], [480, 280]]
                self.flag = True
                self.speed.del_speed()
                Apple().del_apples()
                end_game()
                return True
        print(self.apple_cords)
        if self.head[1] < 0:
            self.head = [500, 280]
            self.body = [[500, 280], [490, 280], [480, 280]]
            self.flag = True
            self.speed.del_speed()
            Apple().del_apples()
            end_game()
            return True
        else:
            self.body.insert(0, list(self.head))
            for el in self.body:
                pygame.draw.rect(screen, pygame.Color('red'), (el[0], el[1], 10, 10))
            if self.head[0] == self.apple_cords[0] and self.head[1] == self.apple_cords[1]:
                print('TRUE')
                Apple().del_apples()
                # Apple(all_sprites)
                self.apple_cords = Apple(all_sprites).make_apple()
                self.body.append([self.head[0], self.head[1]])
                self.flag = False
                self.speed.speed_up()
            else:
                del self.body[-1]
            return False

    def update_speed(self):
        return self.speed.ret_speed()


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["ЗМЕЙКА", "",
                  "Правила игры",
                  "Наберите как можно больше очков,",
                  "поглощая яблоки. Управляйте змейкой",
                  "с помощью клавиш перемещения (стрелочек)",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "НАЖМИТЕ НА ПРОБЕЛ, ЧТОБЫ ПРОДОЛЖИТЬ"]

    fon = pygame.transform.scale(load_image('snake_fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        text_coord += 10
        intro_rect.top = text_coord
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

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

    def speed_up(self):
        self.speed += 1

    def del_speed(self):
        self.speed = 20

    def ret_speed(self):
        return self.speed


def end_game():
    intro_text = ["Вы проиграли!", "",
                  "Нажмите на пробел, чтобы начать заново"]
    fon = pygame.transform.scale(load_image('snake_end_game.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
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
                pygame.draw.rect(screen, pygame.Color('red'), (500, 275, 10, 10))
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
snake = Snake()
while running:
    screen.fill(pygame.Color('black'))
    speed = snake.update_speed()
    if not (down or up or right or left):
        apples_cords = []
        pygame.draw.rect(screen, pygame.Color('red'), (500, 280, 30, 10))
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
    all_sprites.draw(screen)
    clock.tick(speed)
    pygame.display.flip()
pygame.quit()
