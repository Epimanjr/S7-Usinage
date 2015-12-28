#! /usr/bin/env python
# -*- coding: utf8 -*-
import os
import sys
# import nécessaire à la création de l'interface graphique
from tkinter import *

class Entrepot: #Création de l'objet Entrepôt

    # Contruction de l'Entrepôt, qui comporte une taille maximale.
    def __init__(self, tailleMax): # Construit un entrepôt
        self.tailleMax = tailleMax

    def increaseA(self):
        # Fonction servant à incrémenter la valeur du compteur A afin que sa valeur puisse être mise à jour pour l'ensemble de la procédure.
        global comptA # Python recherche la valeur du compteur en dehors de l'espace local de la fonction.
        comptA += 1

    def increaseB(self):
        # Fonction servant à incrémenter la valeur du compteur B.
        global comptB
        comptB += 1

    def increaseC(self):
        # Fonction servant à incrémenter la valeur du compteur C.
        global comptC
        comptC += 1

    # Méthode qui récupère les pièces traitées par les machines (qui ont été modifiées en résultats de type rA/rB/rC précedemment), et incrémente le compteur lié
    def actualiserInterface(self):
        global typ
        if typ == 'rA':
            entrepot.increaseA()
        elif typ == 'rB':
            entrepot.increaseB()
        elif typ == 'rC':
            entrepot.increaseC()
        else:
            print('Pièce qui non reconnue')
        Texte.set("\n Le nombre de pièces de type A qui ont été traitées est de : " + str(comptA) + "\n \nTaux de remplissage : " + str((comptA/entrepot.tailleMax)*100) + "%\n")
        Texte2.set("\n Le nombre de pièces de type B qui ont été traitées est de : " + str(comptB) + "\n \nTaux de remplissage : " + str((comptB/entrepot.tailleMax)*100) + "%\n")
        Texte3.set("\n Le nombre de pièces de type C qui ont été traitées est de : " + str(comptC) + "\n \nTaux de remplissage : " + str((comptC/entrepot.tailleMax)*100) + "%\n")
        
    def initialisationInterface(self):
        Texte.set("\n Le nombre de pièces de type A qui ont été traitées est de : " + str(comptA) + "\n \nTaux de remplissage : " + str((comptA/entrepot.tailleMax)*100) + "%\n")
        Texte2.set("\n Le nombre de pièces de type B qui ont été traitées est de : " + str(comptB) + "\n \nTaux de remplissage : " + str((comptB/entrepot.tailleMax)*100) + "%\n")
        Texte3.set("\n Le nombre de pièces de type C qui ont été traitées est de : " + str(comptC) + "\n \nTaux de remplissage : " + str((comptC/entrepot.tailleMax)*100) + "%\n")


# ----- MAIN PROGRAM ----- #

# Construction de l'entrepôt nommé "entrepot", et qui comporte comme seul paramètre sa taille (calculée auparavent, le 10 n'est qu'un exemple).
entrepot = Entrepot(10);
comptA=0;
comptB=0;
comptC=0;
#type choisi dans le compteur
typ="rA"

# Création de la fenêtre principale (main window)
fenetreEntrepot = Tk()
fenetreEntrepot.title('Entrepôt')

# Création d'un widget Button (bouton Actualiser)
BoutonLancer = Button(fenetreEntrepot, text ='Actualiser', command = entrepot.actualiserInterface)
# Positionnement du widget avec la méthode pack()
BoutonLancer.pack(side = BOTTOM, padx = 5, pady = 5)

# Création d'un widget Button (bouton Quitter)
BoutonQuitter = Button(fenetreEntrepot, text ='Quitter', command = fenetreEntrepot.destroy)
BoutonQuitter.pack(side = BOTTOM, padx = 5, pady = 5)

Texte = StringVar()
Texte2 = StringVar()
Texte3 = StringVar()
entrepot.initialisationInterface()

#Spécification de la fenêtre, et séparation en 3 labels distincts pour séparer les 3 types de pièces
p = PanedWindow(fenetreEntrepot, orient=HORIZONTAL)
p.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
# Label des pièces A
p.add(Label(p, textvariable=Texte, background='blue', anchor=CENTER))
# Label des pièces B
p.add(Label(p, textvariable=Texte2, background='red', anchor=CENTER))
# Label des pièces C
p.add(Label(p, textvariable=Texte3, background='lightgreen', anchor=CENTER))

Mafenetre.mainloop()
