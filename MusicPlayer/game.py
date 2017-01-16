import pygame

pygame.init()
pygame.mixer.init()

size = [640, 480]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()

cupcakeImg = pygame.image.load('cupcake.png')
cupcakeImg = pygame.transform.scale(cupcakeImg, (200, 200))

pygame.mixer.music.load('nevereverland.mp3')

isMusicPlaying = False
isPressing = False

def drawImage(image, x, y):
	cupcakeDraw = screen.blit(image, (x,y))
	return cupcakeDraw


done = False
while done == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		# print(event)

	
	screen.fill((255, 255, 255))
	cupcakeDraw = drawImage(cupcakeImg, 50, 50)

	pos = pygame.mouse.get_pos()
	(pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()

	if pressed1 == 0:
		isPressing = False

	if cupcakeDraw.collidepoint(pos) and pressed1==1 and isPressing == False:
		print("You have opened a chest!")
		isPressing = True
		if isMusicPlaying:
			pygame.mixer.music.stop()
			isMusicPlaying = False
		else:
			pygame.mixer.music.play(-1)
			isMusicPlaying = True

	pygame.display.update()
	clock.tick(60)

pygame.quit()