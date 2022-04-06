#On crée ici la fenêtre du jeu

import pygame #on utilise pygame
import math
from game import Game
pygame.init()

#définir une clock
clock = pygame.time.Clock()
FPS = 120

pygame.display.set_caption("Jeu") #On définit le titre de la fenêtre
screen = pygame.display.set_mode((1080, 720)) #La taille de la fenêtre en largeur par hauteur

running = True # Si elle est vraie alors le jeu tourne, sinon il se ferme

background = pygame.image.load('assets/bg.jpg')

#Importer la bannièere
banner=pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/4)

#Importer le bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3.33)
play_button_rect.y = math.ceil(screen.get_height()/2)


game = Game(screen)


while running:

	#Tant que le jeu tourne, on applique l'arrière plan et le joueur sur la fenêtre
	screen.blit(background, (0, -200))

	#Vérifier si le jeu a commencé ou non
	if game.is_playing == True:
		#On démare la partie
		game.update(screen)
	#Si le jeu n'a pas commencé
	else:
		screen.blit(play_button, play_button_rect)
		screen.blit(banner, banner_rect)
	
	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()

		#On détecte un input clavier
		elif event.type == pygame.KEYDOWN:
			game.pressed[event.key] = True

			if event.key == pygame.K_SPACE:
				game.player.launch_projectile()

		elif event.type == pygame.KEYUP:
			game.pressed[event.key] = False

		elif event.type == pygame.MOUSEBUTTONDOWN:
			#On vérifie si on clique sur le bouton
			if play_button_rect.collidepoint(event.pos):
				game.start()
				#jouer le son
				game.sound_manager.play('click')
	#fixer le nombre de fps sur ma clock
	clock.tick(FPS)
