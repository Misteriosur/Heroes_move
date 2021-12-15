import sys
import pygame
import os

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('К щелчку')
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    x, y = 0, 0

    running = True
    speed = 1
    test = False
    FPS = 60
    clock = pygame.time.Clock()
    screen.fill((255, 255, 255))


    def load_image(name, colorkey=None):
        fullname = os.path.join('data', name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        return image

    image = load_image("creature.png")

    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        k = pygame.key.get_pressed()
        if k[pygame.K_UP]:
            y -= 10
        if k[pygame.K_DOWN]:
            y += 10
        if k[pygame.K_LEFT]:
            x -= 10
        if k[pygame.K_RIGHT]:
            x += 10
        screen.blit(image, (x, y))
        clock.tick(FPS)

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()