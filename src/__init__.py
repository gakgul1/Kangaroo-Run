import pygame
import json
import random
from Kangaroo import Kangaroo
from Cactus import Cactus
from BackGround import Background
from Cloud import Cloud


pygame.init()

'''Font'''
myfont = pygame.font.Font("../assets/font.ttf", 20)
titlefont = pygame.font.Font("../assets/font.ttf", 50)

'''Background'''
w = 1080
h = 540
background = pygame.image.load('../assets/backdrop.png')
background_size = (w,h)
background_rect = (w,h)
screen = pygame.display.set_mode([w,h])
x = 0

pygame.display.set_caption('Kangaroo Run')
white = (255, 255, 255)

'''Score'''
score = 0
highscore = 0

scorefile = open("../assets/scores.txt","r")
highscore = int(scorefile.read())
scorefile.close()

'''Objects'''
kang = Kangaroo()
kangSprite = pygame.sprite.RenderPlain(kang)

cact = Cactus()
cactSprite = pygame.sprite.RenderPlain(cact)

cact2 = Cactus()
cactSprite2 = pygame.sprite.RenderPlain(cact2)

cact3 = Cactus()
cactSprite3 = pygame.sprite.RenderPlain(cact3)

cloud = Cloud()
cloudSprite = pygame.sprite.RenderPlain(cloud)

cloud2 = Cloud()
cloudSprite2 = pygame.sprite.RenderPlain(cloud)
cloud2.x += random.randrange(50)
cloud2.y += random.randrange(50)



'''Music'''
pygame.mixer.init(22050,-16,2,4096)
pygame.mixer.music.load("../assets/song.mp3")
pygame.mixer.music.set_volume(.5)
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

done = False
start = False
game_over = False
pause = False
pauseCount = 1

'''Game Loop'''
while not done:
	pygame.display.update()
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			'''Jump'''
			if event.key == pygame.K_SPACE:
				kang.jump()
			'''Restart'''
			if event.key == pygame.K_r:
				kang.reinit()
				cact.reinit()
				cact2.reinit()
				cact3.reinit()
				cloud.reinit()
				cloud2.reinit()	
				x = 0
				score = 0
				pause = False
				pauseCount = 1
				game_over = False
			'''Quit'''
			if event.key == pygame.K_q:
				done = True
			'''Pause'''
			if event.key == pygame.K_p:
				pauseCount += 1
				if pauseCount % 2 == 0:
					kang.freezeKang()
					cact.freezeCact()
					cact2.freezeCact()
					cact3.freezeCact()
					cloud.freezeCloud()
					cloud2.freezeCloud()
					pause = True
				elif pauseCount % 2 == 1:
					cact.resumeCact()
					cact2.resumeCact()
					cact3.resumeCact()
					kang.resumeKang()
					cloud.resumeCloud()
					cloud2.resumeCloud()
					pause = False
			'''Start'''
			if event.key == pygame.K_s:
				start = True

	'''Moving Background'''
	if not pause and not game_over and start:
		x -= 2
	screen.blit(background,(x,0))
	if x < -w * 9.8:
		x = 0
	
	'''Title Screen'''
	if not start:
		textstart = myfont.render("Press S to Start", 0, white)
		screen.blit(textstart, (460, 130))
		texttitle = titlefont.render("Kangaroo Run", 0, (240, 0, 0))
		screen.blit(texttitle, (400, 75))

	'''Collision'''
	if kang.rect.colliderect(cact.rect) or kang.rect.colliderect(cact2.rect) or kang.rect.colliderect(cact3.rect):
		kang.collide()
		game_over = True

	'''Game Over Screen'''
	if game_over:
		kang.freezeKang()
		cact.freezeCact()
		cact2.freezeCact()
		cact3.freezeCact()
		cloud.freezeCloud()
		cloud2.freezeCloud()

		textgo = myfont.render("Game Over", 0, white)
		screen.blit(textgo, (475, 150))
		textre = myfont.render("Press R to Restart", 0, white)
		screen.blit(textre, (430, 180))
		textqu = myfont.render("Press Q to Quit", 0, white)
		screen.blit(textqu, (440, 210))
		'''New Highscore'''
		if score > highscore:
			highscore = score
			scorefile = open("../assets/scores.txt", "w")
			scorefile.write(str(highscore))
			scorefile.close()
		
	'''Pause Screen'''
	if pause:
		texths = myfont.render("Press H For High Scores", 0, white)
		screen.blit(texths, (10, 10))
		textps = myfont.render("Press P To Resume", 0, white)
		screen.blit(textps, (425, 10))

	'''Displays Score'''
	label = myfont.render("Score: {0}".format(score), 0, white)
	texths = myfont.render("High Score: {0}".format(highscore), 0, white)
	screen.blit(label, (900, 10))
	screen.blit(texths, (850, 40))
	if not game_over and not pause and start:
		score += 1

	'''Loads all objects after start'''
	if start:
		kang.draw(screen)
		kangSprite.update()

		cact.draw(screen)
		cactSprite.update()

		if(score > 850):
			cact2.v = cact.v
			cact2.draw(screen)
			cactSprite2.update()

		if(score > 1850):
			cact3.v = cact.v
			cact3.draw(screen)
			cactSprite3.update()

		cloud.draw(screen)
		cloudSprite.update()

		cloud2.draw(screen)
		cloudSprite2.update()

	pygame.display.flip()
	pygame.display.update()
