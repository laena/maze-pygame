#!/usr/bin/env python

import player, world
import pygame
from pygame.locals import *
import sys

pygame.init()

import theme
theme = theme.Theme()
screen = pygame.display.set_mode([theme.dimX, theme.dimY])

pygame.display.set_caption(theme.gameName)
pygame.mouse.set_visible(0)

import sound
sound = sound.Sound()
sound.playIntro()

maze 	= world.World(theme)
frank 	= player.Player(theme)

gameOver 			= False
waitingForAnswer 	= False
started 			= False
waitingForExit		= False

screen.blit(theme.start, pygame.Rect(0, 0, theme.dimX, theme.dimY))
pygame.display.update()

clock = pygame.time.Clock()

while True: # MAIN GAME LOOP
	clock.tick(30)
	checkQuestion = True
	events = pygame.event.get()
	# Getting the pressed keys and save them in a list []

	startSound = False
	for event in events:
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE) or (waitingForExit and event.type == KEYDOWN):
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if not started:
				started = True
				startSound = True
			if waitingForAnswer:
				if maze.checkInput(events, screen) is not None:
					waitingForAnswer = False
					checkQuestion = False
				else:
					pygame.display.update()
					continue
			keys_pressed = pygame.key.get_pressed()
			if not keys_pressed: continue
			elif (keys_pressed[K_LEFT]):
				frank.moveLeft = True
			elif (keys_pressed[K_RIGHT]):
				frank.moveRight = True
			elif (keys_pressed[K_DOWN]):
				frank.moveDown = True
			elif (keys_pressed[K_UP]):
				frank.moveUp = True

			maze.moveMonsters()
			maze.draw(screen)
			frank.updatePosition(maze)
			frank.draw(screen, maze, checkQuestion)

			waitingForAnswer = maze.hitQuestion

			pygame.display.update()
			status = maze.gameStatus(frank.X, frank.Y)

			if status == "WIN":
				sound.playWon()
				wonlabel = pygame.font.SysFont("monospace", 50).render("YOU WIN!", 1, (0, 0, 255))
				label = theme.font.render("2x left. Stop at 14. 1x right. Stop at 29.", 1, (0,0,0))
				screen.blit(theme.questionBackground, (50, 50))
				screen.blit(wonlabel, (150, 150))
				screen.blit(label, (150, 250))
				pygame.display.update()
				waitingForExit = True

			elif status == "LOSE":
				sound.playLost()
				waitingForExit = True

	if startSound and started:
		sound.playBackground()
		startSound = False