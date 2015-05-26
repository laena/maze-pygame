import pygame
from pygame.locals import *

class Sound:
	def __init__(self):
		pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
		pygame.mixer.music.set_volume(1.0)

	def playBackground(self):
		pygame.mixer.music.stop()
		pygame.mixer.music.load('sound/background.ogg')
		pygame.mixer.music.play(-1)

	def playIntro(self):
		pygame.mixer.music.stop()
		pygame.mixer.music.load('sound/intro.ogg')
		pygame.mixer.music.play(-1)

	def playWon(self):
		pygame.mixer.music.stop()
		sound = pygame.mixer.Sound('sound/win.ogg')
		sound.play()

	def playLost(self):
		pygame.mixer.music.stop()
		sound = pygame.mixer.Sound('sound/lose.ogg')
		sound.play()