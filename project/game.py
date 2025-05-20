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
obstacles = []
for _ in range(5):
    obs = pygame.Rect(random.randint(0, 800-obs_width), random.randint(0, 600-50), obs_width, obs_height)
    obstacles.append(obs)

# 아이템

item_width = item_height = 25
item_x, item_y = random.randint(0, 800-item_width), random.randint(0, 600-item_height)
items = []
for _ in range(5):
    item = pygame.Rect(random.randint(0, 800-item_width), random.randint(0, 600-item_height), item_width, item_height)
    items.append(item)

# fps를 제어할 객체 생성

clock = pygame.time.Clock()
fps = 60
speed = 300

# 게임 실행 반복문

running = True
while running:
# fps에 따라 속도 조절
    dt_time = speed * (clock.tick(fps) / 1000)

# 충돌 시 이전 위치 복귀 좌표
    previous_position = red_box.copy()
    # print(previous_position)

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

# 충돌 감지
    for obs in obstacles:
        if red_box.colliderect(obs):
            if previous_position.right <= obs.left:
                red_box.right = obs.left
            elif previous_position.left >= obs.right:
                red_box.left = obs.right
            elif previous_position.top >= obs.bottom:
                red_box.top = obs.bottom
            elif previous_position.bottom >= obs.top:
                red_box.bottom = obs.top

    for item in items:
        if red_box.colliderect(item):
            items.remove(item)
    # 화면 업데이트, 배경, 개체 출력
    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, red_box)
    for obs in obstacles:
        pygame.draw.rect(screen, BLUE, obs)
    for item in items:
        pygame.draw.rect(screen, YELLOW, item)
    
    pygame.display.flip()

pygame.quit()