import pygame, sys, time


class Plateau:
	""" Modelisation de la fenetre du jeu """
	def __init__(self, dimension:tuple, background_color:str, palette, balle, title="Brick game"):
		
		### caracteristiques de la fenetre
		self.taille_x, self.taille_y = dimension
			# Graphique
		self.screen = pygame.display.set_mode(dimension)
		pygame.display.set_caption(title)
 		
		### Gestion du Jeu
		self.est_lancee_balle = False
		self.est_tombe_balle = False
		self.score = 0

		## composant palette


		## composant boule

		### reaction infinie au maintient d'une touche
		pygame.key.set_repeat(1,20)
		while not self.est_tombe_balle:
			pygame.display.flip()
			self.screen.fill(background_color)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:

					### Gestion du deplacement de la palette 
					# J'avoue avoir fait un peu de bricolage sur ces conditions, pour le moment elles marchent bien
					ne_sortira_pas_à_droite = palette.position_x + palette.vitesse <= self.taille_x - palette.longueur //2
					ne_sortira_pas_à_gauche = palette.position_x + palette.vitesse >= palette.longueur // 2
					
					if event.key == pygame.K_RIGHT:
						if ne_sortira_pas_à_droite:
							palette.move_right()
					elif event.key == pygame.K_LEFT:
						if ne_sortira_pas_à_gauche:
							palette.move_left()

					### Gestion du mouvement de la balle
					elif event.key == pygame.K_SPACE :
						self.est_lancee_balle = True
						

			### Gestion du mouvement de la balle	
			if self.est_lancee_balle:				
				# la balle chage de direction x, si elle tape les bords
				if balle.position_x - balle.rayon <= 0  or balle.position_x + balle.rayon >=  self.taille_x:
					balle.vitesse_x = - balle.vitesse_x

				# elle chage de direction y s'il elle tape le bord superieur ou la palette
				tape_bord_superieur = balle.position_y - balle.rayon <= 0
				tappe_palette = balle.position_y + balle.rayon == palette.position_y and  (balle.position_x - palette.position_x + balle.rayon <= abs(palette.longueur//2) or balle.position_x - palette.position_x - balle.rayon <= abs(palette.longueur//2) )
				if tape_bord_superieur or tappe_palette:
					balle.vitesse_y = - balle.vitesse_y
				elif balle.position_y + balle.rayon == self.taille_y - balle.rayon and not palette.position_x - palette.longueur <= balle.position_x <= palette.position_x + palette.longueur:
					self.est_tombe_balle = True
					print(self.score)
					sys.exit()


				if tappe_palette:
					self.score += 1

				balle.move_y(balle.vitesse_y)
				balle.move_x(balle.vitesse_x)
				
				
				

				time.sleep(0.01 )

			

			## dessin de la palette sur la fenetre
			pygame.draw.rect(self.screen, palette.color, 
				((palette.position_x - palette.longueur//2, palette.position_y), (palette.longueur, 5)))

			## Dessin de la balle sur la fenetre
			pygame.draw.circle(self.screen, balle.color, (balle.position_x, balle.position_y), balle.rayon)
			
			print(palette.position_x, palette.position_x, balle.position_x ) # debogage
			


if __name__ == "__main__":
	from Jeu import *
	from Plateau import *
	from Balle import *
	from Palette import *
	import time

	### variable d'initialisation
	# Couleur
	color_white = (255, 255, 255)
	color_blue = (0, 0, 255)
	color_red = (255, 0, 0)
	color_black = (0, 0, 0)
	# dimension ecran
	dim_ecran = (500, 500)

	# dimension pallete
	l_palette = 50
	x_palette = dim_ecran[0] // 2
	y_palette = dim_ecran[1] - 15

	# creation d'un objet palette
	
	palette = Palette(l_palette, color_black, (x_palette, y_palette), 2)
	# creation d'un objet balle
	balle = Balle(rayon = 10, couleur = color_red, position_0 = (250, 100), vitesse=(1, 1))
	# creation d'un objet plateau
	Plateau(dim_ecran, color_white, palette, balle)
	pygame.init()