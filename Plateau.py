import pygame, sys


class Plateau:
	""" Modelisation de la fenetre du jeu """
	def __init__(self, dimension:tuple, background_color:str, palette1, balle1, title="Brick game"):
		
		### caracteristiques de la fenetre
		self.taille_fenetre_x, self.taille_fenetre_y = dimension
			# Graphique
		self.screen = pygame.display.set_mode(dimension)
		pygame.display.set_caption(title)
 		
		### Gestion du Jeu
		self.game_over = False
		self.est_lancee_balle = False

		## composant palette


		## composant boule

		### reaction infinie au maintient d'une touche
		pygame.key.set_repeat(1,20)
		while True:
			pygame.display.flip()
			self.screen.fill(background_color)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:

					### Gestion du deplacement de la palette 
					# J'avoue avoir fait un peu de bricolage sur ces conditions, pour le moment elles marchent bien
					ne_sortira_pas_à_droite = palette1.position_palette_x + palette1.longueur + palette1.vitesse <= self.taille_fenetre_x
					ne_sortira_pas_à_gauche = 0 <= palette1.position_palette_x - palette1.longueur//2 + palette1.vitesse
					
					if event.key == pygame.K_RIGHT:
						if ne_sortira_pas_à_droite:
							palette1.move_right()
					elif event.key == pygame.K_LEFT:
						if ne_sortira_pas_à_gauche:
							palette1.move_left()

					### Gestion du mouvement de la balle
					elif event.key == pygame.K_SPACE :
						self.est_lancee_balle = True
						

			### Gestion du mouvement de la balle	
			if self.est_lancee_balle:
				position_x = balle1.position_balle_x #+ balle1.rayon
				position_y = balle1.position_balle_y #+ balle1.rayon
				
				# la balle chage de direction x, si elle tape les bords
				if balle1.rayon >= position_x or position_x >= self.taille_fenetre_x - balle1.rayon:
					balle1.vitesse_x = - balle1.vitesse_x

				# elle chage de direction y s'il elle tape le bord superieur ou la palette
				tape_bord_superieur = balle1.rayon >= position_y
				tappe_palette = balle1.position_balle_y + balle1.rayon == self.taille_fenetre_y - balle1.rayon and palette1.position_palette_x - palette1.longueur <= balle1.position_balle_x <= palette1.position_palette_x + palette1.longueur
				if tape_bord_superieur or tappe_palette:
					balle1.vitesse_y = - balle1.vitesse_y

				balle1.move_y(balle1.vitesse_y)
				balle1.move_x(balle1.vitesse_x)
				
				print(palette1.position_palette_x, palette1.position_palette_x)
				

				time.sleep(0.1)

			

			## dessin de la palette sur la fenetre
			pygame.draw.rect(self.screen, palette1.color_palette, 
				(palette1.position_palette_x, palette1.position_palette_y, palette1.longueur, 5))

			## Dessin de la balle sur la fenetre
			pygame.draw.circle(self.screen, balle1.couleur_balle, (balle1.position_balle_x, balle1.position_balle_y), balle1.rayon)
			
			#print(palette1.position_palette_x, palette1.position_palette_y)
			


if __name__ == "__main__":
	"""
		Debogage 
	"""
	import time
	###
	from Palette import *
	from Balle import *
	# color 
	color_white = (255, 255, 255)
	color_blue = (0, 0, 255)
	color_red = (255, 0, 0)

	# creation d'un objet palette
	palette1 = Palette(50, color_blue, (250, 485), 10)
	# creation d'un objet balle
	balle1 = Balle(rayon = 10, couleur = color_red, position_0 = (250, 100), vitesse=(10, 10))

	
	Plateau((500, 500), color_white, palette1, balle1)
	pygame.init()