import pygame
import random
pygame.init()
WIDTH = 500
HEIGHT = 500
run = True
bg = pygame.image.load("C:/Users/femia/Desktop/python_game_dev/Pro Game dev/PirateShip.jpg")
bg = pygame.transform.scale(bg,(500,500))
Screen = pygame.display.set_mode((WIDTH,HEIGHT))

class pira(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/femia/Desktop/python_game_dev/Pro Game dev/Pirate.png")
        self.image = pygame.transform.scale(self.image,(50,70))
        self.rect = self.image.get_rect()

pira1 = pira()
allsprites = pygame.sprite.Group()
allsprites.add(pira1)
class cannonball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/femia/Desktop/python_game_dev/Pro Game dev/cannonball.png")
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()

notmoney = pygame.sprite.Group()
for i in range(10):
    cannon1 = cannonball()
    cannon1.rect.x = random.randint(0,460)
    cannon1.rect.y = random.randint(0,440)
    allsprites.add(cannon1)
    cannonball.add(cannon1)

class money(pygame.sprite.Sprite):
    def __init__(self,img):       
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()

mone = ["C:/Users/femia/Desktop/python_game_dev/Pro Game dev/ring.png","C:/Users/femia/Desktop/python_game_dev/Pro Game dev/coin.png"]
mon = pygame.sprite.Group()

for i in range(10):
    money1 = money(random.choice(mone))
    money1.rect.x = random.randint(0,460)
    money1.rect.y = random.randint(0,440)
    allsprites.add(money1)
    mon.add(money1)









while run:
    for i in pygame.event.get():
        if i .type == pygame.QUIT:
            run = False
    Screen.blit(bg,(0,0))
    allsprites.draw(Screen)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if pira1.rect.y > 0:
            pira1.rect.y = pira1.rect.y - 1            
    if keys[pygame.K_LEFT]:
        if pira1.rect.x > 0:
            pira1.rect.x = pira1.rect.x - 1
    if keys[pygame.K_DOWN]:
        if pira1.rect.y < 440:
            pira1.rect.y = pira1.rect.y + 1
    if keys[pygame.K_RIGHT]:
        if pira1.rect.x < 455:
            pira1.rect.x = pira1.rect.x + 1
    pygame.display.update()
