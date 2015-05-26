import pygame

DIRECTORY = "/themes/dungeon/"

class Theme:
	def __init__(self):
		self.Background = pygame.image.load(DIRECTORY + "Background.png")
		self.obstacle 	= pygame.image.load(DIRECTORY + "Obstacle.png")
		self.goal 		= pygame.image.load(DIRECTORY + "Lena.png")
		self.start		= pygame.image.load(DIRECTORY + "Start.png")