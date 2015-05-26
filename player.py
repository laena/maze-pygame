import pygame
from pygame.locals import *

class Player():
	def __init__(self, theme):
		self.GRIDSIZE = theme.gridsize
	
		self.X = 0
		self.Y = 0
		
		self.moveDown = False
		self.moveUp = False
		self.moveLeft = False
		self.moveRight = False

		self.frame = theme.player

		self.time_since_last_update = 0

	def updatePosition(self, maze):
		if self.moveDown:
			newY = self.Y + self.GRIDSIZE
			if not maze.collides(self.X, newY) and newY <= 552:
				self.Y = newY
			self.moveDown = False
		if self.moveUp:
			newY = self.Y - self.GRIDSIZE
			if not maze.collides(self.X, newY) and newY >= 0:
				self.Y = newY
			self.moveUp = False
		if self.moveRight:
			newX = self.X + self.GRIDSIZE
			if not maze.collides(newX, self.Y) and newX <= 752:
				self.X = newX
			self.moveRight = False
		if self.moveLeft:
			newX = self.X - self.GRIDSIZE
			if not maze.collides(newX, self.Y) and newX >= 0:
				self.X = newX
			self.moveLeft = False

	def draw(self, surface, maze, checkQuestion):
		surface.blit(self.frame, pygame.Rect(self.X, self.Y, self.GRIDSIZE, self.GRIDSIZE))
		if checkQuestion: maze.checkQuestion(self.X, self.Y, surface)
		return surface