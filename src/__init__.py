import pygame
from Kangaroo import Kangaroo
from BackGround import Background
from Cactus import Cactus

#test 2

pygame.init()
#Sets Up Screen
screen = pygame.display.set_mode((1080, 540))
pygame.display.set_caption('Kangaroo Run')
white = (255, 255, 255)
black = (0, 0, 0)
button_light = (205, 200, 177)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(white)

backGround = Background('../assets/background.png')


screen.blit(background, (0,0))
pygame.display.flip()
screen.blit(backGround.image, backGround.rect)

kang = Kangaroo()
kangSprite = pygame.sprite.RenderPlain(kang)

cact = Cactus()
cactSprite = pygame.sprite.RenderPlain(cact)

largeText = pygame.font.Font("yoshi.ttf",60)
smallText = pygame.font.Font("yoshi.ttf",18)

mouse = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()


clock = pygame.time.Clock()


def game_loop():
	done = False
	while not done:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					kang.jump()
					cactSprite.add(cact)
			
		#kang.handlekeys()
		#screen.blit(kang, (0,0))

		screen.blit(backGround.image, (0,0))
		screen.blit(backGround.image, backGround.rect)
		kang.draw(screen)
		cact.draw(screen)
	
		kangSprite.update()
		#kangSprite.draw(screen)
		cactSprite.update()
		pygame.display.update()
		pygame.display.flip()

def text_objects(text, font):
	textSurface = font.render(text, True, white)
	return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,i_color,a_color,action=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if(x + w > mouse[0] > x and y + h > mouse[1] > y):
		pygame.draw.rect(screen, a_color,(x,y, w,h))
		if(click[0] == 1 and action != None):
			if(action == "play"):
				game_loop()
			if(action == "quit"):
				pygame.display.quit()
	else:
		pygame.draw.rect(screen, i_color,(x,y, w,h))

	
	TextSurf, TextRect = text_objects(msg,smallText)
	TextRect.center = ((x+(w/2)),(y+(h/2)))
	screen.blit(TextSurf, TextRect)
	

def game_intro():
	intro = True

	while(intro):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		TextSurf, TextRect = text_objects("Kangaroo Run", largeText)
		TextRect.center = ((1080/2),(540/2))
		screen.blit(TextSurf, TextRect)

		button("[CLICK HERE TO BEGIN]",420,300,240,39,black,button_light,"play")
		button("[QUIT]",860,440,140,40,black,button_light,"quit")
		
		pygame.display.update()
		clock.tick(15)
		
game_intro()
