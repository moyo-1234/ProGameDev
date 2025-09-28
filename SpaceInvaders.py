import pygame

HEIGHT = 600
WIDTH = 1000
run = True
Screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Space  Invaders")
bg = pygame.image.load("bg.png")
Red = pygame.image.load("RSS.png")
Yellow = pygame.image.load("YSS.png")
bg = pygame.transform.scale(bg,(1000,600))
Red = pygame.transform.scale(Red,(50,40))
Red = pygame.transform.rotate(Red,90)
Yellow = pygame.transform.scale(Yellow,(50,40))
Yellow = pygame.transform.rotate(Yellow,270)
def draw():
    Screen.blit(bg,(0,0))
    Screen.blit(Red,(200,300))
    Screen.blit(Yellow,(700,300))
    pygame.display.update()




while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    draw()
