import pygame
from pygame.locals import *

DIRECTORY = "themes/dungeon/"

class Theme:
	def __init__(self):
		self.dimX, self.dimY = 768, 576  #16x12
		self.gameName 	= 'Maze Game' 
		self.background = pygame.image.load(DIRECTORY + "Background.png")
		self.obstacle 	= pygame.image.load(DIRECTORY + "Obstacle.png")
		self.goal 		= pygame.image.load(DIRECTORY + "princess.png")
		self.player		= pygame.image.load(DIRECTORY + "hero.png")
		self.monster	= pygame.image.load(DIRECTORY + "Monster.png")
		self.start		= pygame.image.load(DIRECTORY + "Start.png")
		self.life		= pygame.image.load(DIRECTORY + "life.png")

		self.questionUnanswered = pygame.image.load(DIRECTORY + "Question_new.png")
		self.questionAnswered 	= pygame.image.load(DIRECTORY + "Question_old.png")
		self.questionBackground = pygame.image.load(DIRECTORY + "QuestionBackground.png")

		self.gridsize 	= 48
		self.font		= pygame.font.SysFont("monospace", 20)