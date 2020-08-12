class Balle:
    """Modelisation de la balle du jeu"""
    def __init__(self, rayon:int, couleur:str, position_0:tuple, vitesse=(10, 10)):
        """
            Initialise les variables liées à la balle.
            :param rayon: (int) le rayon de la balle
            :param couleur: (str)   La couleur de la balle
            :param position_0: (tuple) determine les positions initiales de la balle
            :return : (None)
            :CU : None
        """
        self.position_balle_x, self.position_balle_y = position_0
        self.vitesse_x, self.vitesse_y = vitesse
        self.rayon = rayon
        self.couleur_balle = couleur

    def move_y(self, vitesse):
        """
            Fais bouger la balle suivant l'axe y.
            :param vitesse: (int) la vitesse de deplacement de la balle
            :return : (None)
            :CU: aucun
        """

        self.position_balle_y += vitesse

    def move_x(self, vitesse):
        """
            Fais bouger la balle suivant l'axe x.
            :param vitesse: (int) la vitesse de deplacement de la balle
            :return : (None)
            :CU: aucun
        """
        self.position_balle_x += vitesse

