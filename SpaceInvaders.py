import pygame
pygame.font.init()
font = pygame.font.SysFont("Comfortaa",30)
RHealth = 10
Yhealth = 10
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
Rrect = pygame.Rect(200,300,50,40)
Yrect = pygame.Rect(700,300,50,40)
def draw(Rrect,Yrect):
    Screen.blit(bg,(0,0))
    Screen.blit(Red,(Rrect.x,Rrect.y))
    Screen.blit(Yellow,(Yrect.x,Yrect.y))
    pygame.draw.rect(Screen,"black",(500,0,17,600))
    RHealthText = font.render("Health:"+str(RHealth),1,"red")
    Screen.blit(RHealthText,(50,20))
    YHealthText = font.render("Health:"+str(Yhealth),1,"yellow")
    Screen.blit(YHealthText,(850,20))
    pygame.display.update()



while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    draw(Rrect,Yrect)
