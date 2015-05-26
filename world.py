import pygame
from pygame.locals import *
import question
import random

class World():
	def __init__(self, theme):
		self.frame 		= theme.background
		self.obstacle 	= theme.obstacle
		self.life		= theme.life
		self.goal 		= theme.goal
		self.GRIDSIZE 	= theme.gridsize
		self.dimX		= theme.dimX
		self.dimY		= theme.dimY

		import levelloader
		self.obstacles, self.questions, self.goalpos, self.monsters = levelloader.loadAuto(theme)
		#levelloader.load(theme, "levels/1.lvl", "levels/questions.csv")
		
		self.remainingLives = 5
		self.hitQuestion = False
		self.currentQuestion = None

	def draw(self, surface):
		surface.blit(self.frame, pygame.Rect(0, 0, self.dimX, self.dimY))
		for o in self.obstacles:
			surface.blit(self.obstacle, pygame.Rect(o[0] * self.GRIDSIZE, o[1] * self.GRIDSIZE, self.GRIDSIZE, self.GRIDSIZE))
		for q, a in self.questions.iteritems():
			q.draw(surface, a)
		if self.goalpos is not None:
			surface.blit(self.goal, pygame.Rect(self.goalpos[0]*self.GRIDSIZE, self.goalpos[1]*self.GRIDSIZE, self.GRIDSIZE, self.GRIDSIZE))
		for m in self.monsters:
			m.draw(surface, self, False)
		for i in range(0, self.remainingLives):
			surface.blit(self.life, pygame.Rect(self.dimX-i*self.GRIDSIZE, 0, self.GRIDSIZE, self.GRIDSIZE))
		return surface

	def collides(self, x, y):
		for o in self.obstacles:
			ox = o[0] * self.GRIDSIZE
			oy = o[1] * self.GRIDSIZE
			if abs(ox - x) < self.GRIDSIZE and abs(oy - y) < self.GRIDSIZE:
				return True
		return False

	def checkQuestion(self, x, y, surface):
		for q in self.questions:
			if abs(q.X - x) < self.GRIDSIZE and abs(q.Y - y) < self.GRIDSIZE:
				alreadyAnswered = self.questions[q]
				if not alreadyAnswered:
					q.show(surface)
					self.hitQuestion = True
					self.currentQuestion = q
				break

	def checkInput(self, events, surface):
		if self.currentQuestion:
			res = self.currentQuestion.keyboardInput(events, surface)
			if res is None: return None
			elif res is True:
				self.questions[self.currentQuestion] = True
			else:
				self.remainingLives -= 1
			self.currentQuestion = None
			self.hitQuestion = False
			return res

	def allQuestionsAnswered(self):
		for key, value in self.questions.iteritems():
			if value == False: return False
		return True

	def moveMonsters(self):
		m = random.choice(self.monsters)
		i = random.randint(1,4)
		if i == 1: 		m.moveUp = True
		elif i == 2: 	m.moveDown = True
		elif i == 3: 	m.moveRight = True
		elif i == 4: 	m.moveLeft = True
		m.updatePosition(self)

	def hitMonster(self, x, y):
		for m in self.monsters:
			if abs(m.X - x) < self.GRIDSIZE and abs(m.Y - y) < self.GRIDSIZE:
				return True
		return False

	def gameStatus(self, x, y):
		if self.goalpos[0]*self.GRIDSIZE == x and self.goalpos[1]*self.GRIDSIZE == y and self.allQuestionsAnswered():
			return "WIN"
		elif self.remainingLives <= 0 or self.hitMonster(x, y):
			return "LOSE"
		else: return "RUNNING"