import pygame
from pygame.locals import *

import eztext

class Question():
	def __init__(self, theme, text, answer, x, y):
		self.GRIDSIZE = theme.gridsize
		self.X = x * self.GRIDSIZE
		self.Y = y * self.GRIDSIZE

		self.answer = answer.lower()
		self.font 	= theme.font

		self.frame 		= theme.questionUnanswered
		self.frameOld 	= theme.questionAnswered
		self.background = theme.questionBackground
		self.label 		= self.font.render(text, 1, (0,0,0))
		self.textBox 	= eztext.Input(maxlength=45, color=(0,0,0), font=self.font, x=150, y=250, prompt='type here: ')

	def draw(self, surface, alreadyAnswered):
		if alreadyAnswered:
			surface.blit(self.frameOld, pygame.Rect(self.X, self.Y, self.GRIDSIZE, self.GRIDSIZE))
		else:
			surface.blit(self.frame, pygame.Rect(self.X, self.Y, self.GRIDSIZE, self.GRIDSIZE))
		return surface

	def show(self, surface):
		surface.blit(self.background, (50, 50))
		self.textBox.draw(surface)
		surface.blit(self.label, (150, 150))

	def keyboardInput(self, events, surface):
		text = self.textBox.update(events)
		self.show(surface)
		if text is not None:
			return text.strip().lower() == self.answer
		return None