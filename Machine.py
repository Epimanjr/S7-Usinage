#! /usr/bin/env python
# -*- coding: utf8 -*-
import os
import sys

class Machine: #Création de notre objet Machine

    """ Une machine est défini par son nom, et une liste de pièces traitables par la machine.
    """
    def __init__(self, nom, liste): # Construit une machine
        self.nom = nom
        self.liste = liste

    # Méthode qui démarre la machine
    def demarrerMachine(self):
        # Réceception de la pièce
        self.recevoirPiece()
        # Vérification de la pièce
        if self.verifierPiece():
            # Traitement
            self.traiterPiece()
            # Stockage dans l'entrepôt
            self.stockerPiece()
        else:
            # Renvoie à l'autre machine
            pass


    # Méthode qui renvoie la pièce à l'autre machine
    def renvoyerPiece(self):
        pass
    
    # Méthode qui récupère une pièce.
    def recevoirPiece(self):
        # Récupère une pièce dans la file
        # Mise à jour de la pièce courante
        pass

    # Méthode qui traite une pièce.
    def traiterPiece(self):
        # Traitement
        # Fin Traitement
        self.traite = True

    # Méthode qui stocke une pièce dans l'entrepôt
    def stockerPiece(self):
        # Vérification
        if self.traite == True:
            # Stockage dans l'entrepôt
            pass

    # Méthode qui vérifie qu'une pièce est traitable par cette machine.
    def verifierPiece(self):
        for pieces in self.liste:
            if pieces == self.pieceCourante.nom:
                return True
        return False

    # Méthode qui affiche d'une machine.
    def afficher(self):
        print("Bonjour, je suis la machine " + self.nom + " et j'accepte les pièces " + str(self.liste))


# Construction des deux machines
machineA = Machine("mA", ["pA", "pB"]);
machineB = Machine("mB", ["pB", "pC"]);
# Affichage
machineA.afficher();
machineB.afficher();
