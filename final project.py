import pygame
pygame.font.init()
font = pygame.font.SysFont("Arial",30)
RHealth = 10
Bhealth = 10
HEIGHT = 550
WIDTH = 900
BulSpeed = 8
run = True
MaxBul = 5
winner = ""

Screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Ping Pong")
bg = pygame.image.load("C:/Users/femia/Desktop/python_game_dev/Pro Game dev/tennistable.png")
Red = pygame.image.load("C:/Users/femia/Desktop/python_game_dev/Pro Game dev/pingpong.png")
Blue = pygame.image.load("C:/Users/femia/Desktop/python_game_dev/Pro Game dev/Bpingpong.jpeg")
bg = pygame.transform.scale(bg,(1000,600))
Red = pygame.transform.scale(Red,(50,40))
Red = pygame.transform.rotate(Red,90)
Blue = pygame.transform.scale(Blue,(50,40))
Blue = pygame.transform.rotate(Blue,270)
Rrect = pygame.Rect(200,300,50,40)
Brect = pygame.Rect(700,300,50,40)
def draw(Rrect,Brect,RBul,BBul):
    Screen.blit(bg,(0,0))
    Screen.blit(Red,(Rrect.x,Rrect.y))
    Screen.blit(Blue,(Brect.x,Brect.y))
    pygame.draw.rect(Screen,"black",(450,0,17,900))
    RHealthText = font.render("Health:"+str(RHealth),1,"red")
    Screen.blit(RHealthText,(50,20))
    BHealthText = font.render("Health:"+str(Bhealth),1,"blue")
    Screen.blit(BHealthText,(800,20))
    for i in RBul:
        pygame.draw.rect(Screen,"red",(i))
    for i in BBul:
        pygame.draw.rect(Screen,"blue",(i))
    pygame.display.update()

def BShipMove(keys,Brect):
    if keys [pygame.K_LEFT]and Brect.x > 517:
        Brect.x =Brect.x - 1
    if keys [pygame.K_RIGHT]and Brect.x < 950:
        Brect.x = Brect.x + 1
    if keys [pygame.K_UP]and Brect.y > 0:
        Brect.y = Brect.y - 1
    if keys [pygame.K_DOWN]and Brect.y < 550:
        Brect.y = Brect.y + 1

def RShipMove(keys,Rrect):
    if keys [pygame.K_a]and Rrect.x > 0:
        Rrect.x = Rrect.x - 1
    if keys [pygame.K_d]and Rrect.x < 467:
        Rrect.x = Rrect.x + 1
    if keys [pygame.K_w]and Rrect.y > 0:
        Rrect.y = Rrect.y - 1
    if keys [pygame.K_s]and Rrect.y < 550:
        Rrect.y = Rrect.y + 1

RBul = []
BBul = []
BlueHit = pygame.USEREVENT + 1
RedHit = pygame.USEREVENT + 2

def bullet(RBul,BBul,Rrect,Brect):
    for i in RBul:
        i.x = i.x + BulSpeed
        if i.colliderect(Brect):
            pygame.event.post(pygame.event.Event(RedHit))
            RBul.remove(i)
        elif i.x > 1000:
            RBul.remove(i)
    for i in BBul:
        i.x = i.x - BulSpeed
        if i.colliderect(Rrect):
            pygame.event.post(pygame.event.Event(BlueHit))
            BBul.remove(i)
        elif i.x < 0:
            BBul.remove(i)











while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_q and len(RBul) < MaxBul:
                RbulRect = pygame.Rect(Rrect.x + Rrect.width,Rrect.y + Rrect.height // 2,10 ,5 )
                RBul.append(RbulRect)
            if i.key == pygame.K_SPACE and len(BBul) < MaxBul:
                BBulRect = pygame.Rect(Brect.x,Brect.y + Brect.height // 2,10,5)
                BBul.append(BBulRect)
        if i.type == RedHit:
            Bhealth = Bhealth - 1
        if i.type == BlueHit:
            RHealth = RHealth - 1

    if RHealth <= 0:
        winner = "Blue Spaceship wins"
        winnertext = font.render(winner,1,"orange")
        Screen.blit(winnertext,(500,300))
        pygame.display.update()
        pygame.time.delay(5000)
        break

    if Bhealth <= 0:
        winner = "Red Spaceship wins"
        winnertext = font.render(winner,1,"orange")
        Screen.blit(winnertext,(500,300))
        pygame.display.update()
        pygame.time.delay(5000)
        break
    keys = pygame.key.get_pressed()
    draw(Rrect,Brect,RBul,BBul)
    BShipMove(keys,Brect)
    RShipMove(keys,Rrect)
    bullet(RBul,BBul,Rrect,Brect)
    pygame.display.update()