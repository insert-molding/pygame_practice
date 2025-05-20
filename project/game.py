import pygame
import random

pygame.init()

# 해상도 설정

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("pygame test")

# 색상 설정

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# 움직이는 개체

red_width = red_height = 50
red_x, red_y = random.randint(0, 800-red_width), random.randint(0, 600-red_height)
red_box = pygame.Rect(red_x, red_y, red_width, red_height)

# 장애물

obs_width = obs_height = 50
obs_x, obs_y = random.randint(0, 800-obs_width), random.randint(0, 600-obs_height)
obstacle = pygame.Rect(obs_x, obs_y, obs_width, obs_height)

# 아이템

item_width = item_height = 25
item_x, item_y = random.randint(0, 800-item_width), random.randint(0, 600-item_height)
item = pygame.Rect(item_x, item_y, item_width, item_height)

# fps를 제어할 객체 생성

clock = pygame.time.Clock()
fps = 60
speed = 100

# 게임 실행 반복문

running = True
while running:
    # fps에 따라 속도 조절
    dt_time = speed * (clock.tick(fps) / 1000)
    
    # 게임 종료
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 키보드 조작
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        red_box.y -= dt_time
    if keys[pygame.K_DOWN]:
        red_box.y += dt_time
    if keys[pygame.K_LEFT]:
        red_box.x -= dt_time
    if keys[pygame.K_RIGHT]:
        red_box.x += dt_time

# 화면 업데이트
    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, red_box)
    pygame.draw.rect(screen, BLUE, obstacle)
    pygame.draw.rect(screen, YELLOW, item)

    pygame.display.flip()

pygame.quit()