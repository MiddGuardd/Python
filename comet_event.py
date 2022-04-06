import pygame
from comet import Comet

#Créer une classe pour gérer l'évènement
class CometFallEvent:
	#Lors du chargement on va créer un compteur 
	def __init__(self, game):
		self.percent = 0
		self.percent_speed = 5
		self.game = game
		self.fall_mode = False

		#Définir un groupe de sprites
		self.all_comets = pygame.sprite.Group()

	def add_percent(self):
		self.percent += self.percent_speed/100

	def is_full_loaded(self):
		return self.percent >= 100

	def reset_percent(self):
		self.percent = 0

	def meteor_fall(self):
		#Boucle pour les valeurs entre 1 & 10
		for i in range(1, 10):
			#Apparaitre une première boule de feu
			self.all_comets.add(Comet(self))

	def attempt_fall(self):
		#La jauge est totalement chargée
		if self.is_full_loaded() and len(self.game.all_monsters) == 0 :
			print("pluie de comètes")
			self.meteor_fall()
			self.fall_mode = True

	def update_bar(self, surface):

		#Ajouter du pourcentage à la barre
		self.add_percent()


		#Barre noire en arrière plan
		 #Ici on dessine un rectangle avec la surface, puis la couleur (RGB) puis la position [x, y puis la largeur puis la hauteur]
		pygame.draw.rect(surface, (0, 0, 0), [0, surface.get_height()-20, surface.get_width(), 10])
		#Barre rouge de l'évènement
		pygame.draw.rect(surface, (187, 11, 11), [0, surface.get_height()-20, (surface.get_width()/100)*self.percent, 10])