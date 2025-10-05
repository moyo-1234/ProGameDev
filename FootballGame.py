import pygame

HEIGHT = 700
WIDTH = 700
run = True
Screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Goal Defenders")
bg = pygame.image.load("fballbg.jpg")
Rgoal = pygame.image.load("GoalR.png")
Lgoal = pygame.image.load("goalL.png")
bg = pygame.transform.scale(bg,(800,800))
Rgoal = pygame.transform.scale(Rgoal,(50,60))
Lgoal = pygame.transform.scale(Lgoal,(50,60))

def draw():
    Screen.blit(bg,(0,0))
    Screen.blit(Rgoal,(200,300))
    Screen.blit(Lgoal,(500,300))
    pygame.display.update()




while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    draw()
