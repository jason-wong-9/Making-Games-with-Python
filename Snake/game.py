#Me and Jason's Excellent Snake Game
#1/29/2017
#our goal is to make a classic snake game. A snake will appear on screen, it will be controllable with the arrow keys, and it will grow bigger each time it eats an apple. the snake dies if it touches itself.


from enum import Enum
class Direction(Enum):
	UP = 1
	LEFT = 2
	DOWN = 3
	RIGHT = 4

#importing pygame and the mixer
import pygame
pygame.init()

#setting screen size, border, and caption
size = [ 640, 480 ]
screen = pygame.display.set_mode( size )
pygame.display.set_caption ( 'Justin and Jasons Snake game' )
clock = pygame.time.Clock ()

SNAKE_HEAD_COLOR = (124, 252, 0)
SNAKE_HEAD_WIDTH = 30
SNAKE_HEAD_HEIGHT = 30

SNAKE_BODY_COLOR = (255, 0, 0)
SNAKE_BODY_WIDTH = 30
SNAKE_BODY_HEIGHT = 30

SNAKE_SPEED = 15
SNAKE_X = 0
SNAKE_Y = 0
SNAKE_INITIAL_DIRECTION = Direction.DOWN

def drawSnakePart(x, y, isHead):
	if isHead :
		pygame.draw.rect(screen, SNAKE_HEAD_COLOR, (x, y, SNAKE_HEAD_WIDTH, SNAKE_HEAD_HEIGHT))
	else:
		pygame.draw.rect(screen, SNAKE_BODY_COLOR, (x, y, SNAKE_BODY_WIDTH, SNAKE_BODY_HEIGHT))


#all the fps and quit info is here.
done = False
while done == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	screen.fill((255, 255, 255))
	drawSnakePart(SNAKE_X, SNAKE_Y, True)
	if SNAKE_INITIAL_DIRECTION == Direction.UP:
		SNAKE_Y = SNAKE_Y - SNAKE_SPEED
	elif SNAKE_INITIAL_DIRECTION == Direction.LEFT:
		SNAKE_X = SNAKE_X - SNAKE_SPEED
	elif SNAKE_INITIAL_DIRECTION == Direction.DOWN:
		SNAKE_Y = SNAKE_Y + SNAKE_SPEED
	else:
		SNAKE_X = SNAKE_X + SNAKE_SPEED
	pygame.display.update()
	clock.tick(8)

pygame.quit()