import sys
import pygame
import numpy as np
import random
from kohonen import Kohonen
import time


margin=5
width, height = 45, 21.5

def button(column,row, margin, txt="", color=(150, 150, 150)):
	pygame.draw.rect(screen, color,
				[(margin + width) * column + margin,
				(margin + height) * row + margin,
				width,
				height])
	label = myfont.render(txt , 1, (255,255,255))
	screen.blit(label, ((margin + width) * column + 2*margin  , (margin + height) * row + margin) )

def kohonen_animation(kohonen, data):
	for i in range(400):
		kohonen.train_step(data)
 
		draw_menu(data)
		lista = []
		for x in range(kohonen.shape[0]):
			for y in range(kohonen.shape[1]):
				lista.append(kohonen.som[x, y])
				if x < kohonen.shape[0]-1:
					pygame.draw.line(screen, (255,0,0), kohonen.som[x, y] , kohonen.som[x+1, y], 5)
				if y < kohonen.shape[1]-1:
					pygame.draw.line(screen, (255,0,0), kohonen.som[x, y] , kohonen.som[x, y+1], 5)
				pygame.draw.circle(screen, (255, 0, 0), kohonen.som[x, y], 5)
		pygame.display.flip()
		if is_closed_window():
			pygame.quit()
			exit()
		pygame.time.delay(50)

def is_closed_window():
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True
	return False

		
def draw_circle(point, color):
	pygame.draw.circle(screen, color, (point[0], point[1]), 5)

def draw_menu(points):
	big_font = pygame.font.SysFont('Open Sans', 50)
	screen.fill((255, 255, 255))
	pygame.draw.rect(screen, (40, 150, 20),
				[50,
				50,
				400,
				400])
	button(6,18,5, txt="run" )
	button(5,18,5, txt="clear" )
	button(4,17,5, txt="^" )
	button(4,18,5, txt="v" )
	button(2,17,5, txt="^" )
	button(2,18,5, txt="v" )
	label_h = big_font.render(str(som_h) , 1, (0,0,0))
	label_w = big_font.render(str(som_w) , 1, (0,0,0))
	screen.blit(label_h, ((margin + width) * 1 + 3*margin  , (margin + height) * 17 + 2*margin) )
	screen.blit(label_w, ((margin + width) * 3 + 3*margin  , (margin + height) * 17 + 2*margin) )
	for point in points:
		draw_circle(point, (0,0,0))
	pygame.display.flip()




pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Open Sans', 24)
screen = pygame.display.set_mode([500, 550])
som_h = 5
som_w = 5

def main(alpha0=0.5, sigma=1.2):
	global som_h
	global som_w
	points = []
	screen.fill((255, 255, 255))
	pygame.display.flip()
	running = True
	draw_menu(points)
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				column = pos[0] // (width + margin)
				row = pos[1] // (height + margin)
				if row == 18 and column == 6:
					koh = Kohonen(som_h,som_w,2,alpha0=alpha0, sigma=sigma)
					koh.som *= [400, 400]
					koh.som += [50, 50]
					kohonen_animation(koh, points)
				elif row == 18 and column == 5:
					points=[]
					draw_menu(points)
				elif row == 17 and column == 4:
					som_w += 1
					draw_menu(points)
				elif row == 18 and column == 4:
					som_w -= 1
					draw_menu(points)
				elif row == 17 and column == 2:
					som_h += 1
					draw_menu(points)
				elif row == 18 and column == 2:
					som_h -= 1
					draw_menu(points)
				elif pos[0] >= 50 and pos[1] >= 50 and pos[0] <= 450 and pos[1] <= 450:
					points.append((pos[0], pos[1]))
					draw_menu(points)
				#pygame.display.flip()
		
                
	pygame.quit()

if __name__ == "__main__":
	if len(sys.argv) >= 3:
		alfa0 = float(sys.argv[1])
		sigma = float(sys.argv[2])
		main(alfa0,sigma)
	elif len(sys.argv) == 2:
		alfa0 = float(sys.argv[1])
		main(alfa0)
	else:
		main()
