import pygame


FPS = 60 # частота кадров в секунду

pygame.init()
pygame.mixer.init()  # для звука
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Brodilka")
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(FPS)
    screen.fill((0, 0, 0))
    pygame.display.flip()

    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False