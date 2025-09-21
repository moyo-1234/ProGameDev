import pygame
import time

pygame.init()
run = True
WIDTH = 500
HEIGHT = 500
Screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Happpy Birthday Mayokun")
images = pygame.image.load("C:/Users/femia/Desktop/python_game_dev/Pro Game dev/blimg.jpeg")
images = pygame.transform.scale(images,(500,500))
while run:
    font = pygame.font.SysFont("Caveat",30)
    text = font.render("Happy Birthday",1,"Blue")
    text1 = font.render("Mayokun",1,"Orange")
    Screen.blit(images,(0,0))
    Screen.blit(text,(40,40))
    Screen.blit(text1,(400,460))
    pygame.display.update()
    time.sleep(3)
    