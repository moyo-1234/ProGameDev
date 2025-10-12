import pygame
pygame.font.init()
font = pygame.font.SysFont("Comfortaa",30)

HEIGHT = 700
WIDTH = 800
LHealth = 10
RHealth = 10
run = True
Screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Goal Defenders")
bg = pygame.image.load("fballbg.jpg")
Rgoal = pygame.image.load("GoalR.png")
Lgoal = pygame.image.load("goalL.png")
bg = pygame.transform.scale(bg,(800,800))
Rgoal = pygame.transform.scale(Rgoal,(50,60))
Lgoal = pygame.transform.scale(Lgoal,(50,60))
Rrect = pygame.Rect(200,300,50,40)
Lrect = pygame.Rect(700,300,50,40)

def draw(Rrect,Lrect):
    Screen.blit(bg,(0,0))
    Screen.blit(Rgoal,(200,300))
    Screen.blit(Lgoal,(500,300))
    pygame.draw.rect(Screen,"black",(390,0,17,700))
    RHealthText = font.render("Health:"+str(RHealth),1,"red")
    Screen.blit(RHealthText,(50,20))
    LHealthText = font.render("Health:"+str(LHealth),1,"blue")
    Screen.blit(LHealthText,(700,20))
    pygame.display.update()




while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    draw(Rrect,Lrect)
