#! /usr/bin/python
# -*-coding:utf-8 -*

# Code Python du jeu Zcasino, un jeu de roulette de casino.
#
# La regle du jeu est :
#	- Le joueur mise sur un numéro compris entre 0 et 49 (50 numéros en tout). En choisissant son numéro, il y dépose la somme qu'il souhaite miser.
#	- La roulette est constituée de 50 cases allant naturellement de 0 à 49. Les numéros pairs sont de couleur noire, les numéros impairs sont de couleur rouge. Le croupier lance la roulette, lâche la bille et quand la roulette s'arrête, relève le numéro de la case dans laquelle la bille s'est arrêtée. C'est le numéro gagnant.
#	- Si le numéro gagnant est celui sur lequel le joueur a misé (probabilité de 1/50, plutôt faible), le croupier lui remet 3 fois la somme misée.
#	- Sinon, le croupier regarde si le numéro misé par le joueur est de la même couleur que le numéro gagnant (s'ils sont tous les deux pairs ou tous les deux impairs). Si c'est le cas, le croupier lui remet 50 % de la somme misée. 
#	- Si ce n'est pas le cas, le joueur perd sa mise.
#
# On notera que les sommes sont arrondites.

from random import randrange
from math import ceil 

# Declaration des variables initiales
argent = 1000	# Somme initiale du joueur
continuerPartie = True	# Booleen de la boucle de jeu

print("""Bienvenu(e) au Casino de Valo ! Vous avez""",argent,"""€""")
print("""Vous vous installez à une roulette.""")
print("""Souhaitez vous connaître les règles du jeux ?""")
testRegle = input()

print("""Les règles du jeu sont""")

while continuerPartie:
	
	Print
	
	
	
	
	print("""Voulez vous continuez ? o/n""")	# Test si joueur souhaite ou non continuer à jouer
	testContinuerPartie = input()
	
	if testContinuerPartie == """n""" or test_testContinuerPartie == """N""":
		
		print("""Vous quittez le casino avec""",argent,"""€. Revenez quand vous le voulez !""")
		continuerPartie = False

	
