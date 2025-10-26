import pygame
pygame.font.init()
font = pygame.font.SysFont("Comfortaa",30)

HEIGHT = 700
WIDTH = 800
LHealth = 10
RHealth = 10
run = True
MaxBal = 5
Screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Goal Defenders")
bg = pygame.image.load("fballbg.jpg")
Rgoal = pygame.image.load("GoalR.png")
Lgoal = pygame.image.load("goalL.png")
bg = pygame.transform.scale(bg,(800,800))
Rgoal = pygame.transform.scale(Rgoal,(50,60))
Lgoal = pygame.transform.scale(Lgoal,(50,60))
Rrect = pygame.Rect(700,300,50,40)
Lrect = pygame.Rect(200,300,50,40)

def draw(Rrect,Lrect,LBul,RBul):
    Screen.blit(bg,(0,0))
    Screen.blit(Rgoal,(Rrect.x,Rrect.y))
    Screen.blit(Lgoal,(Lrect.x,Lrect.y))
    pygame.draw.rect(Screen,"black",(390,0,17,700))
    RHealthText = font.render("Health:"+str(RHealth),1,"red")
    Screen.blit(RHealthText,(50,20))
    LHealthText = font.render("Health:"+str(LHealth),1,"blue")
    Screen.blit(LHealthText,(700,20))
    for i in RBul:
        pygame.draw.rect(Screen,"blue",(i))
    for i in LBul:
        pygame.draw.rect(Screen,"red",(i))
    pygame.display.update()


def RGoalMove(keys,Rrect):
    if keys [pygame.K_LEFT]and Rrect.x > 407:
        Rrect.x = Rrect.x - 0.53
    if keys [pygame.K_RIGHT]and Rrect.x < 750:
        Rrect.x = Rrect.x + 0.53
    if keys [pygame.K_UP]and Rrect.y > 0:
        Rrect.y = Rrect.y - 0.53
    if keys [pygame.K_DOWN]and Rrect.y < 650:
        Rrect.y = Rrect.y + 0.53

def LGoalMove(keys,Lrect):
    if keys [pygame.K_a]and Lrect.x > 0:
        Lrect.x = Lrect.x - 0.53   
    if keys [pygame.K_d]and Lrect.x < 340:
        Lrect.x = Lrect.x + 0.53
    if keys [pygame.K_w]and Lrect.y > 0:
        Lrect.y = Lrect.y - 0.53
    if keys [pygame.K_s]and Lrect.y < 650:
        Lrect.y = Lrect.y + 0.53

RBul = []
LBul = []


while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_q and len(LBul) < MaxBal:
                LbulRect = pygame.Rect(Lrect.x + Lrect.width,Lrect.y + Lrect.height // 2,10 ,5 )
                LBul.append(LbulRect)
            if i.key == pygame.K_SPACE and len(RBul) < MaxBal:
                RBulRect = pygame.Rect(Rrect.x,Rrect.y + Rrect.height // 2,10,5)
                RBul.append(RBulRect)
    keys = pygame.key.get_pressed()
    draw(Rrect,Lrect,LBul,RBul)
    LGoalMove(keys,Lrect)
    RGoalMove(keys,Rrect)
    pygame.display.update
