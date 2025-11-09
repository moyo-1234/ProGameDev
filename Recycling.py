import pygame
import random
pygame.init()
WIDTH = 500
HEIGHT = 500
run = True
bg = pygame.image.load("C:/Users/femia/Desktop/python_game_dev/Pro Game dev/recbg.png")
bg = pygame.transform.scale(bg,(500,500))
Screen = pygame.display.set_mode((WIDTH,HEIGHT))
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





while run:
    for i in pygame.event.get():
        if i .type == pygame.QUIT:
            run = False
    Screen.blit(bg,(0,0))
    allsprites.draw(Screen)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if bin1.rect.y > 0:
            bin1.rect.y = bin1.rect.y - 1
    if keys[pygame.K_DOWN]:
        if bin1.rect.y < 440:
            bin1.rect.y = bin1.rect.y + 1
    if keys[pygame.K_LEFT]:
        if bin1.rect.x > 0:
            bin1.rect.x = bin1.rect.x - 1
    if keys[pygame.K_RIGHT]:
        if bin1.rect.x < 460:
            bin1.rect.x = bin1.rect.x + 1
    pygame.display.update()

        
    
    


