if __name__ == '__main__':
	from Jeu import *
	from Plateau import *
	from Balle import *
	from Palette import *
	import time

	# color 
	color_white = (255, 255, 255)
	color_blue = (0, 0, 255)
	color_red = (255, 0, 0)

	

	
	
	### Nom du joueur
	nom = input("Entrez votre pseudo de joueur : ")

	try:
	    assert nom[0].isalpha(), "Le nom doit debuter par un caractere alphabetique"
	    assert len(nom) >= 3, "Pseudo trop court. 3 caracteres au moins"
	except Exception as e:
		raise ValueError(e)
		
	else:
		print("Amusez vous bien " + nom)
	##
	time.sleep(5)
	# creation d'un objet palette
	palette = Palette(50, color_blue, (250, 485), 10)
	# creation d'un objet balle
	balle = Balle(rayon = 10, couleur = color_red, position_0 = (250, 100), vitesse=(20, 10))
	# creation d'un objet plateau
	plateau = Plateau((500, 500), color_white, palette, balle)
	jeu = Jeu(nom, plateau)
	#jeu.commencer(P)