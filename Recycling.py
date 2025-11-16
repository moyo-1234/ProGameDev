import pygame
import random
import time
pygame.init()
WIDTH = 500
HEIGHT = 500
font = pygame.font.SysFont("Comfortaa",30)
run = True
StartTime = time.time()
bg = pygame.image.load("C:/Users/femia/Desktop/python_game_dev/Pro Game dev/recbg.png")
bg = pygame.transform.scale(bg,(500,500))
Screen = pygame.display.set_mode((WIDTH,HEIGHT))
Score = 0
class bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/femia/Desktop/python_game_dev/Pro Game dev/bin.png")
        self.image = pygame.transform.scale(self.image,(50,70))
        self.rect = self.image.get_rect()

bin1 = bin()
allsprites = pygame.sprite.Group()
allsprites.add(bin1)
class plastic(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/femia/Desktop/python_game_dev/Pro Game dev/plastic.png")
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()

nonrecyc = pygame.sprite.Group()
for i in range(20):
    plastic1 = plastic()
    plastic1.rect.x = random.randint(0,460)
    plastic1.rect.y = random.randint(0,440)
    allsprites.add(plastic1)
    nonrecyc.add(plastic1)

class recyclable(pygame.sprite.Sprite):
    def __init__(self,img):       
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()

recycl = ["C:/Users/femia/Desktop/python_game_dev/Pro Game dev/box.png","C:/Users/femia/Desktop/python_game_dev/Pro Game dev/paper.png"]
recyc = pygame.sprite.Group()
for i in range(50):
    recyclable1 = recyclable(random.choice(recycl))
    recyclable1.rect.x = random.randint(0,460)
    recyclable1.rect.y = random.randint(0,440)
    allsprites.add(recyclable1)
    recyc.add(recyclable1)



clock = pygame.time.Clock()

while run:
    for i in pygame.event.get():
        if i .type == pygame.QUIT:
            run = False
    Screen.blit(bg,(0,0))
    allsprites.draw(Screen)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if bin1.rect.y > 0:
            bin1.rect.y = bin1.rect.y - 2
    if keys[pygame.K_DOWN]:
        if bin1.rect.y < 440:
            bin1.rect.y = bin1.rect.y + 2
    if keys[pygame.K_LEFT]:
        if bin1.rect.x > 0:
            bin1.rect.x = bin1.rect.x - 2
    if keys[pygame.K_RIGHT]:
        if bin1.rect.x < 460:
            bin1.rect.x = bin1.rect.x + 2
    collideR = pygame.sprite.spritecollide(bin1,recyc,True)
    collideN = pygame.sprite.spritecollide(bin1,nonrecyc,True)
    for i in collideR:
        Score = Score + 1
    for i in collideN:
        Score = Score - 2
    ScoreText = font.render("Score:"+str(Score),1,"red")
    Screen.blit(ScoreText,(420,30))
    clock.tick(30)
    TimeElapsed = time.time() - StartTime
    if TimeElapsed >= 60:
        if Score > 20:
            Win = font.render("You Won",1,"gold")
            Screen.blit(Win,(230,230))
        else:
            Lose = font.render("You Lost",1,"red")
            Screen.blit(Lose,(230,230))
    else:
        Time = font.render("Time Left:"+str(60- int(TimeElapsed)),1,"light blue")
        Screen.blit(Time,(350,50))
    pygame.display.update()

        
    
    


