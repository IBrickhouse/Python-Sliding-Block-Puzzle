import pygame
import sys
import os
import random

# Initializing window
width = 800
height = 600
FPS  = 12

pygame.init()
pygame.display.set_caption('sliding tiles')
gameDisplay = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Define colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
brown = (100,40,0)

background = pygame.image.load('white.jpg')
background = pygame.transform.scale(background, (800,600))

font = pygame.font.Font(os.path.join(os.getcwd(), 'comic.ttf'), 70)