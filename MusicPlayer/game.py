import pygame

pygame.init()

size = [640, 480]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()

cupcakeImg = pygame.image.load('cupcake.png')
cupcakeImg = pygame.transform.scale(cupcakeImg, (200, 200))

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

	if cupcakeDraw.collidepoint(pos)& pressed1==1:
		print("You have opened a chest!")
	pygame.display.update()
	clock.tick(60)

pygame.quit()