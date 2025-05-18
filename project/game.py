import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("pygame test")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

x_pos = screen.get_size()[0]//2
y_pos = screen.get_size()[1]//2

speed = 100

clock = pygame.time.Clock()
fps = 60

running = True
while running:
    dt_time = speed * (clock.tick(fps) / 1000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y_pos -= dt_time
    if keys[pygame.K_DOWN]:
        y_pos += dt_time
    if keys[pygame.K_LEFT]:
        x_pos -= dt_time
    if keys[pygame.K_RIGHT]:
        x_pos += dt_time
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (x_pos, y_pos, 50, 50))
    
    pygame.display.flip()

pygame.quit()