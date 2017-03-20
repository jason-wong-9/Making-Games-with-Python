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
from random import randint
from food import Food
pygame.init()

#setting screen size, border, and caption
size = [ 660, 480 ]
screen = pygame.display.set_mode( size )
pygame.display.set_caption ( 'Justin and Jasons Snake game' )
clock = pygame.time.Clock ()

SNAKE_HEAD_COLOR = (124, 252, 0)
SNAKE_HEAD_WIDTH = 30
SNAKE_HEAD_HEIGHT = 30

SNAKE_BODY_COLOR = (255, 0, 0)
SNAKE_BODY_WIDTH = 30
SNAKE_BODY_HEIGHT = 30

SNAKE_SPEED = 30
SNAKE_X = 0
SNAKE_Y = 0
SNAKE_DIRECTION = Direction.DOWN
food = None


def drawSnakePart(x, y, isHead):
	if isHead :
		pygame.draw.rect(screen, SNAKE_HEAD_COLOR, (x, y, SNAKE_HEAD_WIDTH, SNAKE_HEAD_HEIGHT))
	else:
		pygame.draw.rect(screen, SNAKE_BODY_COLOR, (x, y, SNAKE_BODY_WIDTH, SNAKE_BODY_HEIGHT))

def generateFoodLocation():
	x = randint(0, size[0]/30 - 1) * 30 + 15
	y = randint(0, size[1]/30 - 1) * 30 + 15
	return (x, y)

def drawFood(x, y):
	pygame.draw.circle(screen, Food.COLOR, (food.x, food.y), Food.RADIUS, 2)

def collide():
	return food is not None and SNAKE_X == food.x - 15 and SNAKE_Y == food.y - 15


#all the fps and quit info is here.
done = False
while done == False:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				SNAKE_DIRECTION = Direction.LEFT
			elif event.key == pygame.K_UP:
				SNAKE_DIRECTION = Direction.UP
			elif event.key == pygame.K_RIGHT:
				SNAKE_DIRECTION = Direction.RIGHT
			elif event.key == pygame.K_DOWN:
				SNAKE_DIRECTION = Direction.DOWN
		elif event.type == pygame.QUIT:
			done = True
	
	screen.fill((255, 255, 255))
	drawSnakePart(SNAKE_X, SNAKE_Y, True)

	if food is None or collide():
		(foodX,foodY) = generateFoodLocation()
		food = Food(foodX, foodY)

	drawFood(foodX, foodY)
	
	if SNAKE_DIRECTION == Direction.UP:
		SNAKE_Y = SNAKE_Y - SNAKE_SPEED
	elif SNAKE_DIRECTION == Direction.LEFT:
		SNAKE_X = SNAKE_X - SNAKE_SPEED
	elif SNAKE_DIRECTION == Direction.DOWN:
		SNAKE_Y = SNAKE_Y + SNAKE_SPEED
	else:
		SNAKE_X = SNAKE_X + SNAKE_SPEED
	
	pygame.display.update()
	if SNAKE_X < 0 or SNAKE_X > size[0]-SNAKE_BODY_WIDTH or SNAKE_Y < 0 or SNAKE_Y > size[1]-SNAKE_BODY_HEIGHT:
		done = True
	clock.tick(5)

pygame.quit()