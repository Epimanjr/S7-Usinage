#! /usr/bin/env python
# -*- coding: utf8 -*-
import os
import sys
# import n�cessaire � la cr�ation de l'interface graphique
import tkinter

class Entrepot: #Cr�ation de l'objet Entrep�t

    # Contruction de l'Entrep�t, qui comporte une taille maximale.
    def __init__(self, tailleMax): # Construit un entrep�t
        self.tailleMax = tailleMax

    def increaseA(self):
        # Fonction servant � incr�menter la valeur du compteur A afin que sa valeur puisse �tre mise � jour pour l'ensemble de la proc�dure.
        global comptA # Python recherche la valeur du compteur en dehors de l'espace local de la fonction.
        comptA += 1

    def increaseB(self):
        # Fonction servant � incr�menter la valeur du compteur B.
        global comptB
        comptB += 1

    def increaseC(self):
        # Fonction servant � incr�menter la valeur du compteur C.
        global comptC
        comptC += 1

    # M�thode qui r�cup�re les pi�ces trait�es par les machines (qui ont �t� modifi�es en r�sultats de type rA/rB/rC pr�cedemment), et incr�mente le compteur li�
    def recuperationPiece(self,Piece,compteurA,compteurB,compteurC):
        if Piece.type == 'rA':
            entrepot.increaseA()
        elif Piece.type == 'rB':
            entrepot.increaseB()
        elif Piece.type == 'rC':
            entrepot.increaseC()

    # Affichage graphique du stocks des r�sultats au sein de l'entrep�t
    def affichageGraphique(self,compteurA,compteurB,compteurC,taille_max):
        #Création de la fen�tre "resume_entrepot"
        resume_entrepot = Tk()
        resume_entrepot.title("Entrep�t")
        #Sp�cification de la fen�tre, et s�paration en 3 labels distincts pour s�parer les 3 types de pi�ces
        p = PanedWindow(resume_entrepot, orient=HORIZONTAL)
        p.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
        # Label des pi�ces A
        p.add(Label(p, text="\n Le nombre de pi�ces de type A qui ont �t� trait�es est de : " + str(compteurA) + "\n \nTaux de remplissage : " + str((compteurA/taille_max)*100) + "%\n", background='blue', anchor=CENTER))
        # Label des pi�ces B
        p.add(Label(p, text="\n Le nombre de pi�ces de type B qui ont �t� trait�es est de : " + str(compteurB) + "\n \nTaux de remplissage : " + str((compteurB/taille_max)*100) + "%\n", background='red', anchor=CENTER))
        # Label des pi�ces C
        p.add(Label(p, text="\n Le nombre de pi�ces de type C qui ont �t� trait�es est de : " + str(compteurC) + "\n \nTaux de remplissage : " + str((compteurC/taille_max)*100) + "%\n", background='lightgreen', anchor=CENTER))
        p.pack()
    
# Construction de l'entrep�t nomm� "entrepot", et qui comporte comme seul param�tre sa taille (calcul�e auparavent, le 10 n'est qu'un exemple).
entrepot = Entrepot(10);
comptA=0;
comptB=0;
comptC=0;
# Appel � la fonction de r�ception d'un r�sultat
# entrepot.recuperationPiece(resultat,comptA,comptB,comptC)
# Affichage d'une fiche r�sum� � un moment donn� :
entrepot.affichageGraphique(comptA,comptB,comptC,entrepot.tailleMax)
