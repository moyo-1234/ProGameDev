import pygame
pygame.init()
WIDTH = 500
HEIGHT = 500
run = True
Screen = pygame.display.set_mode((WIDTH,HEIGHT))
class bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/femia\Desktop/python_game_dev/Pro Game dev/bin.png")
        self.image = pygame.transform.scale(self.image,(50,70))
        self.rect = self.image.get_rect()

bin1 = bin()
allsprites = pygame.sprite.Group()
allsprites.add(bin1)








while run:
    for i in pygame.event.get():
        if i .type == pygame.QUIT:
            run = False
    allsprites.draw(Screen)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if bin1.rect.y > 0:
            bin1.rect.y = bin1.rect.y - 4
    pygame.display.update()

        
    
    


