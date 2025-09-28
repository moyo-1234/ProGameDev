import pygame
import time

pygame.init()
run = True
WIDTH = 600
HEIGHT = 600
Screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Happy Mothers Day Mum")
image = pygame.image.load("C:/Users/femia/Desktop/python_game_dev/Pro Game dev/mday1.png")
image1 = pygame.image.load("C:/Users/femia/Desktop/python_game_dev/Pro Game dev/mday2.png")
images = pygame.transform.scale(image1,(600,600))
imagess = pygame.transform.scale(image,(600,600))
while run:
    font = pygame.font.SysFont("Comfortaa",30)
    text = font.render("Happy Mothers Day",1,"pink")
    text1 = font.render("Mum",1,"purple")
    Screen.blit(imagess,(0,0))
    Screen.blit(text,(40,40))
    Screen.blit(text1,(450,480))
    pygame.display.update()
    time.sleep(3)
    Screen.blit(images,(0,0))
    pygame.display.update()
    time.sleep(3)