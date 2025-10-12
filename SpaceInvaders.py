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

def YShipMove(keys,Yrect):
    if keys [pygame.K_LEFT]and Yrect.x > 517:
        Yrect.x =Yrect.x - 1
    if keys [pygame.K_RIGHT]and Yrect.x < 950:
        Yrect.x = Yrect.x + 1
    if keys [pygame.K_UP]and Yrect.y > 0:
        Yrect.y = Yrect.y - 1
    if keys [pygame.K_DOWN]and Yrect.y < 550:
        Yrect.y = Yrect.y + 1

def RShipMove(keys,Rrect):
    if keys [pygame.K_a]and Rrect.x > 0:
        Rrect.x = Rrect.x - 1
    if keys [pygame.K_d]and Rrect.x < 467:
        Rrect.x = Rrect.x + 1
    if keys [pygame.K_w]and Rrect.y > 0:
        Rrect.y = Rrect.y - 1
    if keys [pygame.K_s]and Rrect.y < 550:
        Rrect.y = Rrect.y + 1

    

while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.KEYDOWN:
            pass
    keys = pygame.key.get_pressed()
    draw(Rrect,Yrect)
    YShipMove(keys,Yrect)
    RShipMove(keys,Rrect)
    pygame.display.update()
