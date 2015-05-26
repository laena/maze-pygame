import player
from player import *

class Monster(Player):
	def __init__(self, theme, x, y):
		Player.__init__(self, theme)
		self.X = x
		self.Y = y
		self.frame = theme.monster