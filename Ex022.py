#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
from time import sleep
pygame.init()
pygame.mixer.music.load('Ex022.mp3')
pygame.mixer.music.play()

sleep(40)
pygame.mixer.music.stop()
