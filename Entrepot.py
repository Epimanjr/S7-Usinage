#! /usr/bin/env python
# -*- coding: utf8 -*-
import os
import sys
from tkinter import * 

class Entrepot: #Création de l'objet Entrepôt

    # Contruction de l'Entrepôt, qui comporte une taille maximale, et 3 listes de pièces qui ont été traitées
    # Respectivement notées piecesA, piecesB et piecesC. 
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

    # Méthode qui récupère les pièces traitées par les machines (qui ont été modifiées en rA/rB/rC précedemment), et incrémente le compteur lié
    def recuperationPiece(self,Piece,compteurA,compteurB,compteurC):
        if Piece.type == 'rA':
            entrepot.increaseA()
        elif Piece.type == 'rB':
            entrepot.increaseB()
        elif Piece.type == 'rC':
            entrepot.increaseC()

    # Affichage graphique du stocks de pièces finies au sein de l'entrepôt
    def affichageGraphique(self,compteurA,compteurB,compteurC,taille_max):
        #CrÃ©ation de la fenêtre "resume_entrepot"
        resume_entrepot = Tk()
        resume_entrepot.title("Entrepôt")
        #Spécification de la fenêtre, et séparation en 3 labels distincts pour séparer les 3 types de pièces
        p = PanedWindow(resume_entrepot, orient=HORIZONTAL)
        p.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
        # Label des pièces A
        p.add(Label(p, text="\n Le nombre de pièces de type A qui ont été traitées est de : " + str(compteurA) + "\n \nTaux de remplissage : " + str((compteurA/taille_max)*100) + "%\n", background='blue', anchor=CENTER))
        # Label des pièces B
        p.add(Label(p, text="\n Le nombre de pièces de type B qui ont été traitées est de : " + str(compteurB) + "\n \nTaux de remplissage : " + str((compteurB/taille_max)*100) + "%\n", background='red', anchor=CENTER))
        # Label des pièces C
        p.add(Label(p, text="\n Le nombre de pièces de type C qui ont été traitées est de : " + str(compteurC) + "\n \nTaux de remplissage : " + str((compteurC/taille_max)*100) + "%\n", background='lightgreen', anchor=CENTER))
        p.pack()
    
# Construction de l'entrepôt nommé "entrepot", et qui comporte comme seul paramètre sa taille (calculée auparavent, le 10 n'est qu'un exemple).
entrepot = Entrepot(10);
comptA=0;
comptB=0;
comptC=0;
# Appel à la fonction de réception d'une pièce
# entrepot.recuperationPiece(comptA,comptB,comptC)
# Affichage d'une fiche résumé à un moment donné :
entrepot.affichageGraphique(comptA,comptB,comptC,entrepot.tailleMax)
